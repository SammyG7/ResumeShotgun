## @file menu.py
#  @author Gavin Jameson
#  @author Sam Gorman
#  @brief Allows the user to easily view and set new values for a user profile
#  @date Apr 2, 2022

from menuMessages import *
from sites import SITESLIST, userToURL
from pDef import DEFAULT
from time import sleep
import wx
from pdfReader import pdfReader

## @brief Changes state dictating what menu is shown
def __changeMenu(newMenu = -2):
    if newMenu == -1:
        displayError("input")
        return False
    elif newMenu == -2:
        clearScreen()
        return True
    else:
        clearScreen()
        global menu
        menu = newMenu
        return True

## @brief Processes integer inputs to only allow numbers within a given range; 
#  sets them to -1 if they are not
#  @param value Inteegr to verify
#  @param mx Maximum allowed integer
#  @param mn Minimum allowed integer
#  @return Integer equal to value if it is within mx and mn, otherwise -1
def __limit(value, mx = 9, mn = 1):
    return value if value >= mn and value <= mx else -1

## @brief Prompts user for a menu selection and processes result
#  @param forceInt (optional) Boolean True if the input(s) must be of type integer 
#  @param multiple (optional) Boolean True if multiple choices should be returned 
#  @return Integer for menu choice if one choice is desired, a list of
#  integers if multiple are desired, and -1 if there is an error or no
#  input
def __promptInput(forceInt = True, multiple = False):
    msg = wrappedString("Input choices separated by commas:") if multiple else wrappedString("Input choice:")
    userInput = input(msg)
    processedInput = []
    for choice in userInput.split(","):
        try:
            choice = int(choice.replace(" ","")) if forceInt else choice.strip()
            processedInput.append(choice)
        except ValueError:
            pass
    if len(processedInput) > 0:
        return processedInput if multiple else processedInput[0]
    else:
        return -1

## @brief Creates window to browse for file
#  @return String indicating path to file selected
def __browse():
    app = wx.App()
    
    ## Create Dialog
    dlg = wx.FileDialog(None, message = "Choose Resume",
                wildcard = "*.pdf", style=wx.FD_OPEN|wx.FD_CHANGE_DIR)

    ## Pull Up Window
    dlg.ShowModal()

    return dlg.GetPath()
    

## @brief Runs menu, allowing user to tweak preferences
#  @param profile userProfile object to manipulate
def run(profile):
    
    global menu
    menu = 0
    #resume = pdfReader(profile.getResumePath())
    
    clearScreen()

    #print(resume.path)
    #print(profile)
    
    while menu >= 0:
        ## Main
        if menu == 0:
            displayMenuMain()
            while not __changeMenu(__limit(__promptInput(), mx = 4, mn = 0)): pass
            ## only occurs when going "back" on main, aka exit
            if menu == 0: menu = -1
        ## Main/Resume
        elif menu == 1:
            displayMenuResume(profile.getResumePath())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(0)
                    updated = True
                elif choice == "1": # Manual Browse Window
                    profile.setResumePath(__browse())
                    __changeMenu()
                    updated = True
                elif choice == "2": # Dsiplay Current Resume
                    # Implement Display Resume
                    displayError("missing")
                elif profile.setResumePath(choice):
                    __changeMenu()
                    updated = True
                else:
                    displayError("file")
        ## Main/Personal
        elif menu == 2:
            displayMenuPersonal()
            updated = False
            while not updated:
                choice = __limit(__promptInput(), mx = 8, mn = 0)
                if choice > 0: choice += 10
                updated = __changeMenu(choice)
        ## Main/Search
        elif menu == 3:
            displayMenuSearch()
            updated = False
            while not updated:
                choice = __limit(__promptInput(), mx = 4, mn = 0)
                if choice > 0: choice += 20
                updated = __changeMenu(choice)
        ## Main/Sites
        elif menu == 4:
            displayMenuSites(profile.getSite(), SITESLIST)
            updated = False
            while not updated:
                choice = __promptInput()
                if choice == 0:
                    __changeMenu(0)
                    updated = True
                elif profile.setSite(choice-1):
                    __changeMenu()
                    updated = True
                else:
                    displayError("input")
        ## Main/Personal/First
        elif menu == 11:
            displayMenuFirstName(profile.getFirstName())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(2)
                    updated = True
                elif len(choice) > 0:
                    profile.setFirstName(choice.strip())
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Personal/Last
        elif menu == 12:
            displayMenuLastName(profile.getLastName())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(2)
                    updated = True
                elif len(choice) > 0:
                    profile.setLastName(choice.strip())
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Personal/Email
        elif menu == 13:
            displayMenuEmail(profile.getEmail())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(2)
                    updated = True
                elif len(choice) > 0:
                    if "@" in choice and "." in choice:
                        profile.setEmail(choice.strip())
                        __changeMenu()
                        updated = True
                    else: displayError("input")
                else:
                    displayError("empty")
        ## Main/Personal/Phone
        elif menu == 14:
            displayMenuPhone(profile.getPhone())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(2)
                    updated = True
                elif profile.setPhone(choice):
                    __changeMenu()
                    updated = True
                else:
                    displayError("input")
        ## Main/Personal/Organisation
        elif menu == 15:
            displayMenuOrganisation(profile.getOrganisation())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(2)
                    updated = True
                elif len(choice) > 0:
                    profile.setOrganisation(choice.strip())
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Personal/Socials
        elif menu == 16:
            displayMenuSocials(profile.getSocials())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False, multiple = True)
                if len(choice) == 1 and choice[0] == "1":
                    profile.setSocials(DEFAULT["socials"][0])
                    __changeMenu()
                    updated = True
                elif len(choice) == 1 and choice[0] == "0":
                    __changeMenu(2)
                    updated = True
                elif len(choice) == 1:
                    #if "." in choice and "/" in choice:   disabled for easier removal of links
                    profile.setSocials(choice[0].strip(), toggleMode = True)
                    __changeMenu()
                    updated = True
                    #else:
                        #displayError("input")
                elif len(choice) > 1:
                    for site in choice[1:]:
                        profile.setSocials(userToURL(choice[0].strip(), site.strip()), toggleMode = True)
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Personal/Grad
        elif menu == 17:
            displayMenuGradDate(profile.getGradDate())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False, multiple = True)
                if len(choice) == 1 and choice[0] == "0":
                    __changeMenu(2)
                    updated = True
                elif len(choice) > 0:
                    if profile.setGradDate(choice):
                        __changeMenu()
                        updated = True
                    else: displayError("input")
                else:
                    displayError("empty")
        ## Main/Personal/Uni
        elif menu == 18:
            displayMenuUniversity(profile.getUniversity())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(2)
                    updated = True
                elif len(choice) > 0:
                    profile.setUniversity(choice.strip())
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Search/Title
        elif menu == 21:
            displayMenuJobTitle(profile.getJobTitle())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False)
                if choice == "0":
                    __changeMenu(3)
                    updated = True
                elif len(choice) > 0:
                    profile.setJobTitle(choice.strip())
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Search/Location
        elif menu == 22:
            displayMenuLocation(profile.getLocation())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False, multiple = True)
                if len(choice) == 1 and choice[0] == "0":
                    __changeMenu(3)
                    updated = True
                elif len(choice) > 0:
                    if profile.setLocation(choice):
                        __changeMenu()
                        updated = True
                    else: displayError("input")
                else:
                    displayError("empty")
        ## Main/Search/Keywords
        elif menu == 23:
            displayMenuKeywords(profile.getKeywords())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False, multiple = True)
                if len(choice) == 1 and choice[0] == "1":
                    profile.setKeywords(DEFAULT["keywords"][0])
                    __changeMenu()
                    updated = True
                elif len(choice) == 1 and choice[0] == "0":
                    __changeMenu(3)
                    updated = True
                elif len(choice) > 0:
                    profile.setKeywords(choice, toggleMode = True)
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Search/Auto-Login
        elif menu == 24:
            displayMenuAutoLogin(profile.getAutoLogin(convert = False))
            updated = False
            while not updated:
                choice = __promptInput()
                if choice == 0:
                    __changeMenu(3)
                    updated = True
                elif choice == 1:
                    profile.setAutoLogin(True)
                    __changeMenu()
                    updated = True
                elif choice == 2:
                    profile.setAutoLogin(False)
                    __changeMenu()
                    updated = True
                else:
                    displayError("input")
        ## ERROR
        else:
            displayMenuPlaceholder("FORBIDDEN MENU :O")
            sleep(3)
            __changeMenu(0)

# missing things to add: QOL review all, see whats missing


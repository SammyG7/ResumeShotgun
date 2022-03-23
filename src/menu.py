## @file menu.py
#  @author Gavin Jameson
#  @brief Allows the user to easily view and set new values for a user profile
#  @date Mar 18, 2022

from menuMessages import *
from sites import SITESLIST
from time import sleep

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

## @brief Runs menu, allowing user to tweak preferences
#  @param profile userProfile object to manipulate
def run(profile):
    
    global menu
    menu = 0
    
    clearScreen()
    
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
                choice = limit(promptInput(), mx = 9, mn = 0)
                if choice > 0: choice += 10
                updated = __changeMenu(choice)
        ## Main/Keywords
        elif menu == 3:
            displayMenuKeywords(profile.getKeywords())
            updated = False
            while not updated:
                choice = __promptInput(forceInt = False, multiple = True)
                if len(choice) == 1 and choice[0] == "1":
                    profile.setKeywords([])
                    __changeMenu()
                    updated = True
                elif len(choice) == 1 and choice[0] == "0":
                    __changeMenu(0)
                    updated = True
                elif len(choice) > 0:
                    profile.setKeywords(choice, toggleMode = True)
                    __changeMenu()
                    updated = True
                else:
                    displayError("empty")
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
            displayMenuPlaceholder("Main/Personal/First")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Last
        elif menu == 12:
            displayMenuPlaceholder("Main/Personal/Last")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Email
        elif menu == 13:
            displayMenuPlaceholder("Main/Personal/Email")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Phone
        elif menu == 14:
            displayMenuPlaceholder("Main/Personal/Phone")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Organisation
        elif menu == 15:
            displayMenuPlaceholder("Main/Personal/Org")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Socials
        elif menu == 16:
            displayMenuPlaceholder("Main/Personal/Socials")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Location
        elif menu == 17:
            displayMenuPlaceholder("Main/Personal/Location")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Grad
        elif menu == 18:
            displayMenuPlaceholder("Main/Personal/Grad")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Uni
        elif menu == 19:
            displayMenuPlaceholder("Main/Personal/Uni")
            time.sleep(3)
            changeMenu(2)
        ## Main/Personal/Uni
        else:
            displayMenuPlaceholder("FORBIDDEN MENU :O")
            time.sleep(3)
            changeMenu(0)


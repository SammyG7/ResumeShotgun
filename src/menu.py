## @file menu.py
#  @author Gavin Jameson
#  @brief Allows the user to easily view and set new values for a user profile
#  @date Mar 17, 2022

from menuMessages import *
from sites import SITESLIST
from time import sleep

## @brief Gets location of resume
#  @return String corresponding to location of resume file
def getResumePath():
    return resumePath

## @brief Gets keywords
#  @return List of strings specified as keywords for searching
def getKeywords():
    return keywords

## @brief Changes state dictating what menu is shown
#  @param newMenu (optional) Integer for new menu state number (default does not change menu)
#  @return True if menu was updated (same menu page or not), False if
#  invalid input was given
def changeMenu(newMenu = -2):
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

## @brief Processes integer inputs to only allow numbers
#  within a given range; sets them to -1 if they are not
#  @param value Integer to process
#  @param mx (optional) Maximum allowed integer
#  @param mn (optional) Minimum allowed integer
#  @return Integer indicating the original input if it is within
#  the range, or -1 if it was not in the range
def limit(value, mx = 9, mn = 1):
    return value if value >= mn and value <= mx else -1

## @brief Prompts user for a menu selection and processes result
#  @param forceInt (optional) Boolean True if the input(s) must be of type integer 
#  @param multiple (optional) Boolean True if multiple choices should be returned 
#  @return Integer for menu choice if one choice is desired, a list of
#  integers if multiple are desired, and -1 if there is an error or no
#  input
def promptInput(forceInt = True, multiple = False):
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
            while not changeMenu(limit(promptInput(), mx = 5, mn = 0)): pass
            ## only occurs when going "back" on main, aka exit
            if menu == 0: menu = -1
        ## Main/Resume
        elif menu == 1:
            displayMenuResume(profile.getResumePath())
            updated = False
            while not updated:
                choice = promptInput(forceInt = False)
                if choice == "0":
                    changeMenu(0)
                    updated = True
                elif profile.setResumePath(choice):
                    changeMenu()
                    updated = True
                else:
                    displayError("file")
        ## Main/Personal
        elif menu == 2:
            displayMenuPlaceholder("Main/Personal")
            sleep(5)
            changeMenu(0)
        ## Main/Keywords
        elif menu == 3:
            displayMenuKeywords(profile.getKeywords())
            updated = False
            while not updated:
                choice = promptInput(forceInt = False, multiple = True)
                if len(choice) == 1 and choice[0] == "1":
                    profile.setKeywords([])
                    changeMenu()
                    updated = True
                elif len(choice) == 1 and choice[0] == "0":
                    changeMenu(0)
                    updated = True
                elif len(choice) > 0:
                    profile.setKeywords(choice, toggleMode = True)
                    changeMenu()
                    updated = True
                else:
                    displayError("empty")
        ## Main/Sites
        elif menu == 4:
            displayMenuSites(profile.getSite(), SITESLIST)
            updated = False
            while not updated:
                choice = promptInput()
                if choice == 0:
                    changeMenu(0)
                    updated = True
                elif profile.setSite(choice-1):
                    changeMenu()
                    updated = True
                else:
                    displayError("input")


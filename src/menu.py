from menuMessages import *
from os.path import isfile
from time import sleep

#### load all stored prefrences from YAML here ####

menu = 0
resumePath = ""

##
#  @brief Changes state dictating what menu is shown
#  @param Integer for new menu state number (default does not change menu)
#
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

##
#  @brief Processes integer inputs to only allow numbers
#  within a given range; sets them to -1 if they are not
#
def limit(value, mx = 9, mn = 1):
    return value if value >= mn and value <= mx else -1

##
#  @brief Prompts user for a menu selection and processes result
#  @param Boolean True if the input(s) must be of type integer (default True)
#  @param Boolean True if multiple choices should be returned (default False for
#  only one choice)
#  @return Integer for menu choice if one choice is desired, a list of
#  integers if multiple are desired, and -1 if there is an error or no
#  input
#
def promptInput(forceInt = True, multiple = False):
    msg = "Input choices separated\n by commas: " if multiple else "Input choice: "
    userInput = input(msg)
    processedInput = []
    for choice in userInput.split():
        try:
            choice = int(choice.replace(" ","")) if forceInt else choice.strip()
            processedInput.append(choice)
        except ValueError:
            pass
    if len(processedInput) > 0:
        return processedInput if multiple else processedInput[0]
    else:
        return -1

## ------------- Running loop ----------------
clearScreen()
## menu == 6 is the exit value in main menu
while menu != 6:
    ## Main
    if menu == 0:
        displayMenuMain()
        while not changeMenu(limit(promptInput(),6)): pass
    ## Main/Resume
    elif menu == 1:
        displayMenuResume(resumePath)
        updated = False
        while not updated:
            choice = promptInput(forceInt = False)
            if choice == "1":
                changeMenu(0)
                updated = True
            elif isfile(choice):
                resumePath = choice
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
        displayMenuPlaceholder("Main/Keywords")
        sleep(5)
        changeMenu(0)
    ## Main/Job
    elif menu == 4:
        displayMenuPlaceholder("Main/Job")
        sleep(5)
        changeMenu(0)
    ## Main/Sites
    elif menu == 5:
        displayMenuPlaceholder("Main/Sites")
        sleep(5)
        changeMenu(0)
        
                
#### save preferences to yaml here ####
            

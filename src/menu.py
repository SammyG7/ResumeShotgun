## ---------- imports ----------
from menuMessages import *
from os.path import isfile, join
from os import getcwd
from time import sleep
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

## ---------- functions ----------
##
#  @brief Gets location of resume
#  @return String corresponding to location of resume file
#
def getResumePath():
    return resumePath

##
#  @brief Gets keywords
#  @return List of strings specified as keywords for searching
#
def getKeywords():
    return keywords

##
#  @brief Changes state dictating what menu is shown
#  @param Integer for new menu state number (default does not change menu)
#  @return True if menu was updated (same menu page or not), False if
#  invalid input was given
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

## ---------- default variable values ----------
menu = 0
resumePath = ""
keywords = []

## ---------- set up variables from yaml ----------
if isfile("profile.yaml"):
    print("Loading profile...\n")
    profileFile = open("profile.yaml", "r")
    profile = yaml.load(profileFile, Loader=Loader)
    profileFile.close()
    try:
        ## resumePath
        try:
            if isfile(profile["resumePath"]): resumePath = profile["resumePath"]
            else:
                input("Resume can not be accessed, \n" +
                      "using blank value. \n\n" +
                      "([Enter] to continue)")
        except KeyError:
            input("Resume can not be found in profile, \n" +
                  "using blank value. \n\n" +
                  "([Enter] to continue)")
        ## keywords
        try:
            keywords = profile["keywords"]
        except KeyError:
            input("Keywords can not be found in profile, \n" +
                  "using blank value. \n\n" +
                  "([Enter] to continue)")
    except TypeError:
        input("Profile read error, \n" +
              "using blank values. \n\n" +
              "([Enter] to continue)")
else: 
    input("Profile not found, \n" +
          "using blank values. \n\n" +
          "([Enter] to continue)")

## ---------- the loop that runs it ----------
clearScreen()
## menu == 6 is the exit value in main menu
while menu >= 0:
    ## Main
    if menu == 0:
        displayMenuMain()
        while not changeMenu(limit(promptInput(), mx = 5, mn = 0)): pass
        ## only occurs when going "back" on main, aka exit
        if menu == 0: menu = -1
    ## Main/Resume
    elif menu == 1:
        displayMenuResume(resumePath)
        updated = False
        while not updated:
            choice = promptInput(forceInt = False)
            if choice == "0":
                changeMenu(0)
                updated = True
            elif isfile(choice):
                if isfile(join(getcwd(), choice)): resumePath = join(getcwd(), choice)
                else: resumePath = choice
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
        displayMenuKeywords(keywords)
        updated = False
        while not updated:
            choice = promptInput(forceInt = False, multiple = True)
            if len(choice) == 1 and choice[0] == "1":
                keywords = []
                changeMenu()
                updated = True
            elif len(choice) == 1 and choice[0] == "0":
                changeMenu(0)
                updated = True
            elif len(choice) > 0:
                for word in choice:
                    if word.replace(" ", "") != "":
                        word = word.lower()
                        try: keywords.remove(word)
                        except ValueError: keywords.append(word)
                changeMenu()
                updated = True
            else:
                displayError("empty")
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
        
## ---------- save profile ----------
print("Saving profile...\n")
profileFile = open("profile.yaml", "w")
yaml.dump({
    "resumePath": resumePath,
    "keywords": keywords
    }, profileFile, Dumper = Dumper)
profileFile.close()
input("Finished! \n\n" +
      "([Enter] to close)")

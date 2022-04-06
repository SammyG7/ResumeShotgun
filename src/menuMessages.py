## @file menuMessages.py
#  @author Gavin Jameson
#  @author Sam Gorman
#  @brief interface messages for menu
#  @date Apr 2, 2022

from os import name, system
from pDef import DEFAULT, MONTHS

# Widths are 30 characters max
# displayMenu ... is manually enforced,
# other messages use wrappedString

## @brief Displays text for main menu options
def displayMenuMain():
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main                       \n" +
          "==============================\n" +
          " 1) Upload Resume \n" +
          " 2) Personal Info \n" +
          " 3) Search Preferences \n" +
          " 4) Sites \n" +
          "\n" +
          " 0) Save and Start \n" +
          "\n")
    
## @brief Displays text for resume menu options
#  @param path String for current path to resume file
def displayMenuResume(path):
    if path == DEFAULT["resumePath"][0]: path = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Resume                \n" +
          "==============================\n" +
          " Current resume: \n" +
          " " + path + "\n" +
          "\n" +
          wrappedString("To select a new resume, " +
                        "input the path to the pdf or " +
                        "select an option below.") + "\n" +
          "\n" +
          " 1) Manually Choose File \n" +
          " 2) Display Resume \n" +
          " 3) Automatically Pull Info From Resume \n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for personal info menu options
def displayMenuPersonal():
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal              \n" +
          "==============================\n" +
          " 1) First Name \n" +
          " 2) Last Name \n" +
          " 3) Email \n" +
          " 4) Phone \n" +
          " 5) Organisation \n" +
          " 6) Socials \n" +
          " 7) Location \n" +
          " 8) gradDate \n" +
          " 9) University \n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for first name menu (profile submenu) options
#  @param path String for first name
def displayMenuFirstName(name):
    if name == DEFAULT["firstName"][0]: name = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/First        \n" +
          "==============================\n" +
          " Current first name: \n" +
          " " + name + "\n" +
          "\n" +
          wrappedString("Input text to " +
                        "update the first name.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for last name menu (profile submenu) options
#  @param path String for last name
def displayMenuLastName(name):
    if name == DEFAULT["lastName"][0]: name = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/Last         \n" +
          "==============================\n" +
          " Current last name: \n" +
          " " + name + "\n" +
          "\n" +
          wrappedString("Input text to " +
                        "update the last name.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for email menu (profile submenu) options
#  @param path String for email
def displayMenuEmail(email):
    if email == DEFAULT["email"][0]: email = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/Email        \n" +
          "==============================\n" +
          " Current email: \n" +
          " " + email + "\n" +
          "\n" +
          wrappedString("Input text to " +
                        "update the email.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for phone menu (profile submenu) options
#  @param path String for phone number
def displayMenuPhone(phone):
    if phone == DEFAULT["phone"][0]: phone = "N/A"
    else: phone = phone[0:3] + " " + phone[3:6] + " " + phone[6:]
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/Phone        \n" +
          "==============================\n" +
          " Current phone: \n" +
          " " + phone + "\n" +
          "\n" +
          wrappedString("Input text to " +
                        "update the phone number.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for organisation menu (profile submenu) options
#  @param path String for organisation name
def displayMenuOrganisation(name):
    if name == DEFAULT["organisation"][0]: name = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/Organisation \n" +
          "==============================\n" +
          " Current organisation: \n" +
          wrappedString(name) + "\n" +
          "\n" +
          wrappedString("Input text to " +
                        "update the organisation.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for location menu (profile submenu) options
#  @param path Tuple indicating location
def displayMenuLocation(loc):
    if loc == DEFAULT["location"][0]: loc = ("N/A", "N/A", "N/A")
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/Location     \n" +
          "==============================\n" +
          " Current location: \n" +
          " City: {0}".format(loc[0]) + "\n" +
          ((" State/Prov.: {0}".format(loc[1]) + "\n") if (loc[1] != "") else "") +
          " Country: {0}".format(loc[2]) + "\n" +
          "\n" +
          wrappedString("Input either city then country, or " +
                        "city then state/province then country " +
                        "to update the location to search.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for graduation date menu (profile submenu) options
#  @param path Tuple indicating graduation date
def displayMenuGradDate(grad):
    if grad == DEFAULT["gradDate"][0]: grad = "N/A"
    else: grad = MONTHS[grad[0] - 1].capitalize() + " " + str(grad[1])
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/Grad         \n" +
          "==============================\n" +
          " Current grad date: \n" +
          " " + grad + "\n" +
          "\n" +
          wrappedString("Input month then year " +
                        "to update graduation date.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for university menu (profile submenu) options
#  @param path String for university name
def displayMenuUniversity(name):
    if name == DEFAULT["university"][0]: name = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Personal/University   \n" +
          "==============================\n" +
          " Current university: \n" +
          wrappedString(name) + "\n" +
          "\n" +
          wrappedString("Input text to " +
                        "update the unversity.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for job search menu options
def displayMenuSearch():
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Search                  \n" +
          "==============================\n" +
          " 1) Job Title \n" +
          " 2) Keywords \n" +
          " 3) Auto-Login \n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for job title menu (search submenu) options
#  @param path String for current path to resume file
def displayMenuJobTitle(title):
    if title == DEFAULT["jobTitle"][0]: title = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Search/Title          \n" +
          "==============================\n" +
          " Current job title: \n" +
          " " + title + "\n" +
          "\n" +
          wrappedString("Input text to " +
                        "update the job title.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for keywords menu (search submenu) options
#  @param keywords List of strings of current keywords
def displayMenuKeywords(keywords):
    if keywords == DEFAULT["keywords"][0]: keywords = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Search/Keywords       \n" +
          "==============================\n" +
          " Current keywords: \n" +
          wrappedString(keywords) + "\n" +
          "\n" +
          wrappedString("Input words (to do multiple, separate them " +
                        "by ',') to use as keywords in searches. Words that " +
                        "are not there will be added, words that are will " +
                        "be removed.") + "\n" +
          "\n" +
          " 1) Clear all keywords \n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for auto login menu (search submenu) options
#  @param site Boolean indicating current setting
def displayMenuAutoLogin(setting):
    if setting == DEFAULT["autoLogin"][0]: setting = "N/A"
    else: setting = "Use auto-login" if setting else "Do not use auto-login"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Search/Auto-Login     \n" +
          "==============================\n" +
          " Current: \n" +
          wrappedString(setting) + "\n" +
          "\n" +
          wrappedString("Input number corresponding to the option " +
                        "you want to use.") + "\n" +
          "\n" +
          " 1) Use auto-login \n" +
          " 2) Do not use auto-login \n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

## @brief Displays text for sites menu options
#  @param site String indicating current site
#  @param siteList List of strings of names of available sites
def displayMenuSites(site, siteList):
    siteString = ""
    for n in range(len(siteList)):
        siteString += " " + str(n+1) + ") " + siteList[n] + "\n"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Sites                 \n" +
          "==============================\n" +
          " Current site: \n" +
          " " + site + "\n" +
          "\n" +
          wrappedString("Input number corresponding to the site " +
                        "you want to use.") + "\n" +
          "\n" +
          siteString +
          "\n" +
          " 0) Go back \n" +
          "\n")



## @brief Displays text for unimplemented menu
#  @param menu (optional) String for menu location
def displayMenuPlaceholder(menu = "??"):
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > " + menu + "\n" +
          "==============================\n" +
          " THIS \n" +
          "        IS \n" +
          "             A \n" +
          "                  PLACEHOLDER \n" +
          "\n" +
          "Returning to main menu... \n" +
          "\n")

## @brief Clears console screen
def clearScreen():
    system("cls" if name == "nt" else "clear")

## @brief Adds newlines to a string or combines a list of values with newlines such that 
#  it does not exceed a given width
#  @details Each new line is padded with a space for optimal asthetics, that space character 
#  IS included in the width
#  @param raw String or list to wrap
#  @param width (optional) Integer for maximum width allowed
#  @return String with no line longer than the given width in characters (if possible)
def wrappedString(raw, width = 30):
    out = " "
    lineLength = 1
    if type(raw) is str:
        raw = raw.split(" ")
        for word in raw:
            ## if next word would be over width and something is there, newline
            if lineLength + len(word) > width and lineLength > 1:
                out += "\n " + word + " "
                lineLength = len(word) + 2
            ## add word to line
            else:
                out += word + " "
                lineLength += len(word) + 1
        return out
    elif type(raw) is list:
        for word in raw:
            ## if next word would be over width and something is there, newline
            if lineLength + len(word) > width and lineLength > 1:
                out += "\n " + word + ", "
                lineLength = len(word) + 3
            ## add word to line
            else:
                out += word + ", "
                lineLength += len(word) + 2
        return out[:-2]
    else:
        return ("This message should not show, " +
               "but is simply here to prevent an error " +
               "that would happen if it didn't")
                
## @brief Displays error messages
#  @details Error messages are separate from Python error messages; these messages
#  do not and should not stop execution, they should merely let the user know that
#  the program did not do what was expected of it for the reason given
#  @param error (optional) Error message type to display
def displayError(error = "general"):
    msgs = {
        "input": "Invalid input selected.",
        "file": "File could not be accessed.",
        "empty": "No input provided.",
        "missing": "This functionality does not exist.",
        "general": "Something went wrong. :o"
        }
    print(wrappedString("!! " + msgs[error]) + "\n")

## @brief Prompts user to confirm before continuing
def waitForUser():
    input("([Enter] to continue)\n")
        

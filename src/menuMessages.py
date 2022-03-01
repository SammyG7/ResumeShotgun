from os import name, system

## Widths are 30 characters max


##
#  @brief Displays text for main menu options
# 
def displayMenuMain():
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main                       \n" +
          "==============================\n" +
          " 1) Upload Resume \n" +
          " 2) Personal Info \n" +
          " 3) Keywords \n" +
          " 4) Job preferences \n" +
          " 5) Sites \n" +
          "\n" +
          " 0) Save and Start \n" +
          "\n")
    
##
#  @brief Displays text for resume menu options
#  @param path String for current path to resume file
# 
def displayMenuResume(path):
    if path == "": path = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Resume                \n" +
          "==============================\n" +
          " Current resume: \n" +
          " " + path + "\n" +
          "\n" +
          wrappedString("To select a new resume, " +
                        "input the path to the pdf.") + "\n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

##
#  @brief Displays text for keywords menu options
#  @param keywords List of strings of current keywords
# 
def displayMenuKeywords(keywords):
    if len(keywords) == 0: keywords = "N/A"
    print("==============================\n" +
          "        RESUME SHOTGUN        \n" +
          " > Main/Keywords              \n" +
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

##
#  @brief Displays text for sites menu options
#  @param site current site
# 
def displayMenuSites(site):
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
          " 1) Glassdoor \n" +
          " 2) Indeed \n" +
          "\n" +
          " 0) Go back \n" +
          "\n")

##
#  @brief Displays text for unimplemented menu
#  @param menu Optional string for menu location (default "??")
# 
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

## 
#  @brief Clears console screen
# 
def clearScreen():
    system("cls" if name == "nt" else "clear")

## 
#  @brief Adds newlines to a string or combines a list of values
#  with newlines such that it does not exceed a given width
#  @details Each new line is padded with a space for optimal asthetics,
#  that space character IS included in the width
#  @param raw String or list to wrap
#  @param width Optional integer for maximum width allowed (default 29)
#  @return String with no line longer than the given width in characters
#  (if possible)
# 
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
                
        

##
#  @brief Displays error messages
#  @param error Optional error message type to display
#  (defaults to general message)
#
def displayError(error = "general"):
    msgs = {
        "input": "Invalid input selected.",
        "file": "File could not be accessed.",
        "empty": "No input provided.",
        "general": "Something went wrong. :o"
        }
    print(wrappedString("!! " + msgs[error]) + "\n")


        

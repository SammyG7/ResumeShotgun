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
          " 6) Exit \n" +
          "\n")
    
##
#  @brief Displays text for resume menu options
#  @param String for current path to resume file
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
          " To select a new resume, input\n" +
          " the path to your pdf\n" +
          "\n" +
          " 1) Go back \n" +
          "\n")

##
#  @brief Displays text for unimplemented menu
#  @param String for menu location (default "??")
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
#  @brief Displays error messages
#  @param Error message to display (defaults to general message)
#
def displayError(error = "general"):
    msgs = {
        "input": "Invalid input selected.\n",
        "file": "File could not be accessed.\n",
        "general": "Something went wrong. :o \n"
        }
    print(" ! " + msgs[error])


        

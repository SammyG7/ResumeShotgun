## @file userProfile.py
#  @author Gavin Jameson
#  @brief profile module
#  @date Mar 1, 2022

from menuMessages import wrappedString as wS, waitForUser
from os.path import isfile, join
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

## @brief this class represents the preferences of a user for job searching 
class userProfile:

    ## @brief Constructor for userProfile
    #  @details Sets default values for profile
    def __init__(self):
        self.__resumePath = ""
        self.__keywords = []
        self.__site = "glassdoor"

    ## @brief Method attempts to load values from the given file to itself
    #  @param file (optional) A path to the saved profile
    def loadProfile(self, file = "profile.yaml"):
        if isfile(file):
            print(wS("Loading profile from " + file + "...") + "\n")
            profileFile = open(file, "r")
            profile = yaml.load(profileFile, Loader=Loader)
            profileFile.close()
            try:
                ## resumePath
                try:
                    if isfile(profile["resumePath"]): self.__resumePath = profile["resumePath"]
                    else:
                        print(wS("Resume can not be accessed, using blank value.") + "\n")
                        waitForUser()
                except KeyError:
                    print(wS("Resume can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## keywords
                try:
                    self.__keywords = profile["keywords"]
                except KeyError:
                    print(wS("Keywords can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## site
                try:
                    self.__site = profile["site"]
                except KeyError:
                    print(wS("Site can not be found in profile, using default value.") + "\n")
                    waitForUser()
            except TypeError:
                print(wS("Profile read error, using default values.") + "\n")
                waitForUser()
        else: 
            print(wS("Profile not found, using default values.") + "\n")
            waitForUser()

    ## @brief Method attempts to save its variable values to the given file
    #  @details Will overwrite the file if it exists already
    #  @param file (optional) A string indicating a path to the profile to write 
    def saveProfile(self, file = "profile.yaml"):
        print(wS("Saving profile to " file "...") + "\n")
        profileFile = open(file, "w")
        yaml.dump({
            "resumePath": self.getResumePath(),
            "keywords": self.getKeywords(),
            "site": self.getSite()
            }, profileFile, Dumper = Dumper)
        profileFile.close()
        print("Saved! \n")
        waitForUser()

    # ---------- getters ----------

    ## @brief Method gets path to resume file
    #  @return String indicating path to resume file
    def getResumePath(self):
        return self.__resumePath

    ## @brief Method gets keywords to use in searching
    #  @return List of strings indicating keywords
    def getKeywords(self):
        return self.__keywords

    ## @brief Method gets site that will be scraped
    #  @return String indicating name of site
    def getResumePath(self):
        return self.__site

    # ---------- setters ----------

    ## @brief Method tries to set path to resume file
    #  @details Method also checks if file exists, and if it does not it will not change it
    #  @param file A string indicating a path to a resume file
    #  @param appendWorking (optional) Append the working directory to the file if applicable
    #  @return Boolean True if file exists and successfully changes, False if not
    def setResumePath(self, file, appendWorking = True):
        if isfile(file):
            if appendWorking and isfile(join(getcwd(), file)):
                self.__resumePath = join(getcwd(), file)
            else: 
                self.__resumePath = file

    ## @brief Method sets keywords
    #  @param keywords A list of strings used as keywords
    #  @param toggleMode (optional) If true, instead of overwriting the class varible with 
    #  the parameter, it will add words to the class varable from the parameter that are not 
    #  there and remove ones that are
    def setKeywords(self, keywords, toggleMode = False):
        if toggleMode:
            for word in keywords:
                if word.replace(" ", "") != "":
                    word = word.lower()
                    try: self.__keywords.remove(word)
                    except ValueError: self.__keywords.append(word)
        else: 
            self.__keywords = keywords

    ## @brief CHECK
    def setSite(self, site):
        self.__site = site


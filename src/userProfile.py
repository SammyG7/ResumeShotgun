## @file userProfile.py
#  @author Gavin Jameson
#  @brief profile module
#  @date Mar 14, 2022

from menuMessages import wrappedString as wS, waitForUser
from sites import SITESLIST
from os import getcwd
from os.path import isfile, join
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

## @brief this class represents the preferences of a user for job searching 
class userProfile:

    ## @brief Constructor for userProfile
    #  @details Sets default values for profile
    def __init__(self):
        self.__keywords = []
        self.__site = "glassdoor"
        self.__firstName = ""
        self.__lastName = ""
        self.__email = ""
        self.__phone = ""
        self.__organisation = ""
        self.__resumePath = ""
        self.__socials = []
        self.__location = ()
        self.__grad = ()
        self.__university = ""

    ## @brief Method attempts to load values from the given file to itself
    #  @param userPrompts (optional) Boolean for if user should require confirmations
    #  @param file (optional) A string of the path to the saved profile
    def loadProfile(self, userPrompts = True, file = "profile.yaml"):
        if isfile(file):
            print(wS("Loading profile from " + file + "...") + "\n")
            profileFile = open(file, "r")
            profile = load(profileFile, Loader=Loader)
            profileFile.close()
            try:
                ## keywords
                try:
                    self.__keywords = profile["keywords"]
                except KeyError:
                    print(wS("Keywords can not be found in profile, using default value.") + "\n")
                    if userPrompt: waitForUser()
                ## site
                try:
                    self.__site = profile["site"]
                except KeyError:
                    print(wS("Site can not be found in profile, using default value.") + "\n")
                    if userPrompt: waitForUser()
                ## resumePath
                try:
                    if isfile(profile["resumePath"]): self.__resumePath = profile["resumePath"]
                    else:
                        print(wS("Resume can not be accessed, using blank value.") + "\n")
                        waitForUser()
                except KeyError:
                    print(wS("Resume can not be found in profile, using default value.") + "\n")
                    if userPrompt: waitForUser()
            except TypeError:
                print(wS("Profile read error, using default values.") + "\n")
                if userPrompt: waitForUser()
        else: 
            print(wS("Profile not found, using default values.") + "\n")
            if userPrompt: waitForUser()

    ## @brief Method attempts to save its variable values to the given file
    #  @details Will overwrite the file if it exists already
    #  @param userPrompts (optional) Boolean for if user should require confirmations
    #  @param file (optional) A string indicating a path to the profile to write 
    def saveProfile(self, userPrompts = True, file = "profile.yaml"):
        print(wS("Saving profile to " + file + "...") + "\n")
        profileFile = open(file, "w")
        dump(self.getProfileDict(), profileFile, Dumper = Dumper)
        profileFile.close()
        print("Saved! \n")
        if userPrompt: waitForUser()

    # ---------- getters ----------

    ## @brief Method gets keywords to use in searching
    #  @return List of strings indicating keywords
    def getKeywords(self):
        return self.__keywords

    ## @brief Method gets site that will be scraped
    #  @return String indicating name of site
    def getSite(self):
        return self.__site

    ## @brief Method gets first name
    #  @return String indicating first name
    def getFirstName(self):
        return self.__firstName

    ## @brief Method gets last name
    #  @return String indicating last name
    def getLastName(self):
        return self.__lastName

    ## @brief Method gets main contact email
    #  @return String indicating email address
    def getEmail(self):
        return self.__email

    ## @brief Method gets phone number
    #  @return String of numbers indicating phone number
    def getPhone(self):
        return self.__phone

    ## @brief Method gets current employment location
    #  @return String indicating place of employment
    def getOrganisation(self):
        return self.__organisation

    ## @brief Method gets path to resume file
    #  @return String indicating path to resume file
    def getResumePath(self):
        return self.__resumePath

    ## @brief Method gets social media links
    #  @return List of strings indicating URLs to social media profiles
    def getSocials(self):
        return self.__socials

    ## @brief Method gets city, state/province if applicable, and country of residence
    #  @return Tuple of 3 strings indicating city, state/province (empty string if none was provided),
    #  and country of residence
    def getLocation(self):
        return self.__location

    ## @brief Method gets graduation date
    #  @return Tuple of 2 integers indicating the month and year of graduation
    def getGrad(self):
        return self.__grad

    ## @brief Method gets university attended
    #  @return String indicating name of university
    def getUniversity(self):
        return self.__university

    ## @brief Method gets all values stored in profile
    #  @return Dictionary with string keys matching values in profile
    def getProfileDict(self):
        profile = {
            "keywords": self.getKeywords(),
            "site": self.getSite()
            "firstName": self.getFirstName(),
            "lastName": self.getLastName(),
            "email": self.getEmail(),
            "phone": self.getPhone(),
            "organisation": self.getOrganisation(),
            "resumePath": self.getResumePath(),
            "socials": self.getSocials(),
            "location": self.getLocation(),
            "grad": self.getGrad(),
            "university": self.getUniversity()
        }
        return profile

    # ---------- setters ----------

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

    ## @brief Method tries to set active site for scraping
    #  @details Method will not change the active site if it does not map to one in the list
    #  @param site Integer inicating index of site to swap to
    #  @return Boolean True if the site was updated, False if not
    def setSite(self, site):
        try: self.__site = SITESLIST[site]
        except IndexError: return False
        except TypeError: return False
        return True

    ## @brief Method tries to set path to resume file
    #  @details Method also checks if file exists, and if it does not it will not change it
    #  @param file A string indicating a path to a resume file
    #  @param appendWorking (optional) Append the working directory to the file if applicable
    #  @return Boolean True if file exists and updates, False if not
    def setResumePath(self, file, appendWorking = True):
        if isfile(file):
            if appendWorking and isfile(join(getcwd(), file)):
                self.__resumePath = join(getcwd(), file)
            else: 
                self.__resumePath = file
            return True
        else:
            return False


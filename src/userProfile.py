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

    ## @brief Dictionary of default variable states and if they need updating for use
    #  @details Tuple; index 0 is value, index 1 is if it requires changing
    DEFAULT = {
            "keywords": ([], False),
            "site": ("glassdoor", False),
            "firstName": ("", True),
            "lastName": ("", True),
            "email": ("", True),
            "phone": ("", True),
            "organisation": ("", False),
            "resumePath": ("", True),
            "socials": ([], False),
            "location": ((), True),
            "gradDate": ((), False),
            "university": ("", False)
        }

    ## @brief Constructor for userProfile
    #  @details Sets default values for profile
    #  @param userPrompts (optional) Boolean default class value for if user
    #  should require confirmations when performing tasks like saving/loading
    def __init__(self, userPrompts = True):
        self.__keywords = self.DEFAULT["keywords"][0]
        self.__site = self.DEFAULT["site"][0]
        self.__firstName = self.DEFAULT["firstName"][0]
        self.__lastName = self.DEFAULT["lastName"][0]
        self.__email = self.DEFAULT["email"][0]
        self.__phone = self.DEFAULT["phone"][0]
        self.__organisation = self.DEFAULT["organisation"][0]
        self.__resumePath = self.DEFAULT["resumePath"][0]
        self.__socials = self.DEFAULT["socials"][0]
        self.__location = self.DEFAULT["location"][0]
        self.__gradDate = self.DEFAULT["gradDate"][0]
        self.__university = self.DEFAULT["university"][0]
        self.__userPrompts = userPrompts

    ## @brief Method attempts to load values from the given file to itself
    #  @param userPrompts (optional) Boolean for if user should require confirmations
    #  @param file (optional) A string of the path to the saved profile
    def loadProfile(self, userPrompts = "", file = "profile.yaml"):
        if userPrompts == "": userPrompts = self.__userPrompts
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
                    if userPrompts: waitForUser()
                ## site
                try:
                    self.__site = profile["site"]
                except KeyError:
                    print(wS("Site can not be found in profile, using default value.") + "\n")
                    if userPrompts: waitForUser()
                ## resumePath
                try:
                    if isfile(profile["resumePath"]): self.__resumePath = profile["resumePath"]
                    else:
                        print(wS("Resume can not be accessed, using blank value.") + "\n")
                        if userPrompts: waitForUser()
                except KeyError:
                    print(wS("Resume can not be found in profile, using default value.") + "\n")
                    if userPrompts: waitForUser()
                print("Done! \n")
                if userPrompts: waitForUser()
            except TypeError:
                print(wS("Profile read error, using default values.") + "\n")
                if userPrompts: waitForUser()
        else: 
            print(wS("Profile not found, using default values.") + "\n")
            if userPrompts: waitForUser()

    ## @brief Method attempts to save its variable values to the given file
    #  @details Will overwrite the file if it exists already
    #  @param userPrompts (optional) Boolean for if user should require confirmations
    #  @param file (optional) A string indicating a path to the profile to write 
    def saveProfile(self, userPrompts = "", file = "profile.yaml"):
        if userPrompts == "": userPrompts = self.__userPrompts
        print(wS("Saving profile to " + file + "...") + "\n")
        profileFile = open(file, "w")
        dump(self.getProfileDict(), profileFile, Dumper = Dumper)
        profileFile.close()
        print("Saved! \n")
        if userPrompts: waitForUser()

    def isComplete(self, userPrompts = ""):
        if userPrompts == "": userPrompts = self.__userPrompts
        currentProfile = self.getProfileDict()
        msg = " "
        for key in self.DEFAULT:
            elem = self.DEFAULT[key]
            if elem[1] and elem[0] == currentProfile[key]:
                msg += key + ", "
        if msg == " ":
            print(wS("Profile ready!") + "\n")
            if userPrompts: waitForUser()
            return True
        else:
            print(wS("These fields still need an input:\n" + msg[:-2]) + "\n")
            if userPrompts: waitForUser()
            return False

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
    def getGradDate(self):
        return self.__gradDate

    ## @brief Method gets university attended
    #  @return String indicating name of university
    def getUniversity(self):
        return self.__university

    ## @brief Method gets all values stored in profile
    #  @return Dictionary with string keys matching values in profile
    def getProfileDict(self):
        profile = {
            "keywords": self.getKeywords(),
            "site": self.getSite(),
            "firstName": self.getFirstName(),
            "lastName": self.getLastName(),
            "email": self.getEmail(),
            "phone": self.getPhone(),
            "organisation": self.getOrganisation(),
            "resumePath": self.getResumePath(),
            "socials": self.getSocials(),
            "location": self.getLocation(),
            "gradDate": self.getGradDate(),
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


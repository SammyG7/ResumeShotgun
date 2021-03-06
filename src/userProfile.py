## @file userProfile.py
#  @author Gavin Jameson
#  @brief user profile module
#  @date Apr 2, 2022

from menuMessages import wrappedString as wS, waitForUser
from sites import SITESLIST
from pDef import DEFAULT, MONTHS
from os import getcwd
from os.path import isfile, join
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

## @brief This class represents the preferences of a user for job searching 
class userProfile:

    ## @brief Makes shallow copy of data
    @staticmethod
    def __cpy(thing):
        if type(thing) is tuple:
            return tuple(thing)
        if type(thing) is list:
            return list(thing)
        if type(thing) is str:
            return str(thing)
        else: return thing

    ## @brief Constructor for userProfile
    #  @details Sets default values for profile
    #  @param userPrompts (optional) Boolean default class value for if user
    #  should require confirmations when performing tasks like saving/loading
    def __init__(self, userPrompts = True):
        ## @brief Words used in searches to help locate better fitting jobs
        self.__keywords = self.__cpy(DEFAULT["keywords"][0])
        ## @brief Title of target job position
        self.__jobTitle = self.__cpy(DEFAULT["jobTitle"][0])
        ## @brief The site that will be scraped for URLs
        self.__site = self.__cpy(DEFAULT["site"][0])
        ## @brief User's first name
        self.__firstName = self.__cpy(DEFAULT["firstName"][0])
        ## @brief User's last name
        self.__lastName = self.__cpy(DEFAULT["lastName"][0])
        ## @brief User's email address
        self.__email = self.__cpy(DEFAULT["email"][0])
        ## @brief User's phone number
        self.__phone = self.__cpy(DEFAULT["phone"][0])
        ## @brief User's current workplace/affiliation
        self.__organisation = self.__cpy(DEFAULT["organisation"][0])
        ## @brief Path to resume file
        self.__resumePath = self.__cpy(DEFAULT["resumePath"][0])
        ## @brief List of links to user's social media pages
        self.__socials = self.__cpy(DEFAULT["socials"][0])
        ## @brief Area for job search
        self.__location = self.__cpy(DEFAULT["location"][0])
        ## @brief User's date of graudation from their program
        self.__gradDate = self.__cpy(DEFAULT["gradDate"][0])
        ## @brief User's university
        self.__university = self.__cpy(DEFAULT["university"][0])
        ## @brief Whether or not the program should automatically log into sites
        self.__autoLogin = self.__cpy(DEFAULT["autoLogin"][0])
        ## @brief Default value of whether or not confirmation messages should be shown
        self.__userPrompts = userPrompts
        ## @brief Location of profile
        self.__fileLoc = "profile.yaml"

    ## @brief Method attempts to load values from the given file to itself
    #  @param userPrompts (optional) Boolean for if user should require confirmations
    def loadProfile(self, userPrompts = ""):
        file = join(getcwd(), "profile.yaml")
        self.__fileLoc = file
        if userPrompts == "": userPrompts = self.__userPrompts
        if isfile(file):
            if userPrompts: print(wS("Loading profile from " + file + "...") + "\n")
            profileFile = open(file, "r")
            profile = load(profileFile, Loader=Loader)
            profileFile.close()
            try:
                ## keywords
                if "keywords" in profile: self.__keywords = profile["keywords"]
                elif userPrompts:
                    print(wS("Keywords can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## jobTitle
                if "jobTitle" in profile: self.__jobTitle = profile["jobTitle"]
                elif userPrompts:
                    print(wS("Job title can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## site
                if "site" in profile: self.__site = profile["site"]
                elif userPrompts:
                    print(wS("Site can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## firstName
                if "firstName" in profile: self.__firstName = profile["firstName"]
                elif userPrompts:
                    print(wS("First name can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## lastName
                if "lastName" in profile: self.__lastName = profile["lastName"]
                elif userPrompts:
                    print(wS("Last name can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## email
                if "email" in profile: self.__email = profile["email"]
                elif userPrompts:
                    print(wS("Email can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## phone
                if "phone" in profile: self.__phone = profile["phone"]
                elif userPrompts:
                    print(wS("Phone can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## organisation
                if "organisation" in profile: self.__organisation = profile["organisation"]
                elif userPrompts:
                    print(wS("Organisation can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## resumePath
                if "resumePath" in profile:
                    if isfile(profile["resumePath"]): self.__resumePath = profile["resumePath"]
                    elif userPrompts:
                        print(wS("Resume can not be accessed, using default value.") + "\n")
                        waitForUser()
                elif userPrompts:
                    print(wS("Resume can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## socials
                if "socials" in profile: self.__socials = profile["socials"]
                elif userPrompts:
                    print(wS("Socials can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## location
                if "location" in profile: self.__location = profile["location"]
                elif userPrompts:
                    print(wS("Location can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## gradDate
                if "gradDate" in profile: self.__gradDate = profile["gradDate"]
                elif userPrompts:
                    print(wS("Graduation date can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## university
                if "university" in profile: self.__university = profile["university"]
                elif userPrompts:
                    print(wS("University can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## autoLogin
                if "autoLogin" in profile: self.__autoLogin = profile["autoLogin"]
                elif userPrompts:
                    print(wS("Auto Login setting can not be found in profile, using default value.") + "\n")
                    waitForUser()
                ## -- FINISHED --
                if userPrompts: 
                    print("Done! \n")
                    waitForUser()
            except TypeError:
                if userPrompts: 
                    print(wS("Profile read error, using default values.") + "\n")
                    waitForUser()
        else: 
            if userPrompts: 
                print(wS("Profile not found, using default values.") + "\n")
                waitForUser()

    ## @brief Method attempts to save its variable values to the given file
    #  @details Will overwrite the file if it exists already
    #  @param userPrompts (optional) Boolean for if user should require confirmations 
    def saveProfile(self, userPrompts = ""):
        file = self.__fileLoc
        if userPrompts == "": userPrompts = self.__userPrompts
        if userPrompts: print(wS("Saving profile to " + file + "...") + "\n")
        profileFile = open(file, "w")
        dump(self.getProfileDict(), profileFile, Dumper = Dumper)
        profileFile.close()
        if userPrompts:
            print("Saved! \n")
            waitForUser()

    ## @brief Method verifies that all profile elements were changed that are required
    #  for a base job application
    #  @param userPrompts (optional) Boolean for if user should require confirmations
    #  @return Boolean if required changes have been made
    def isComplete(self, userPrompts = ""):
        if userPrompts == "": userPrompts = self.__userPrompts
        currentProfile = self.getProfileDict()
        msg = " "
        for key in DEFAULT:
            elem = DEFAULT[key]
            if elem[1] and elem[0] == currentProfile[key]:
                msg += key + ", "
        if msg == " ":
            if userPrompts:
                print(wS("Profile ready!") + "\n")
                waitForUser()
            return True
        else:
            if userPrompts:
                print(wS("These fields still need an input:\n" + msg[:-2]) + "\n")
                waitForUser()
            return False

    # ---------- getters ----------

    ## @brief Method gets keywords to use in searching
    #  @return List of strings indicating keywords
    def getKeywords(self):
        return self.__keywords

    ## @brief Method gets job title to use in searching
    #  @return String indicating job title
    def getJobTitle(self):
        return self.__jobTitle

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

    ## @brief Method gets organisation name
    #  @return String indicating organisation
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

    ## @brief Method gets city, state/province if applicable, and country of job
    #  @return Tuple of 3 strings indicating city, state/province (empty string if none was provided),
    #  and country of job
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

    ## @brief Method gets whether or not website logins should be automated
    #  @param convert (optional) Boolean if blank value should be converted to False
    #  @return String indicating name of university
    def getAutoLogin(self, convert = True):
        if convert:
            return False if self.__autoLogin == DEFAULT["autoLogin"][0] else self.__autoLogin
        return self.__autoLogin

    ## @brief Method gets all values stored in profile
    #  @return Dictionary with string keys matching values in profile
    def getProfileDict(self):
        profile = {
            "keywords": self.getKeywords(),
            "jobTitle": self.getJobTitle(),
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
            "university": self.getUniversity(),
            "autoLogin": self.getAutoLogin(convert = False)
        }
        return profile

    # ---------- setters ----------
    # if an input can be of the correct type but can be easily validated on whether or not
    # it is of the correct format, it will be - those setters will all have a return boolean
    # indicating if it was changed (validated) = True, or not changed (not valid) = False

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
                    if word in self.getKeywords(): self.__keywords.remove(word)
                    else: self.__keywords.append(word)
        else: 
            self.__keywords = keywords

    ## @brief Method sets job title
    #  @param name String indicating job title
    def setJobTitle(self, title):
        self.__jobTitle = title

    ## @brief Method tries to set active site for scraping
    #  @details Method will not change the active site if it does not map to one in the list
    #  @param site Integer inicating index of site to swap to
    #  @return Boolean True if the site was updated, False if not
    def setSite(self, site):
        if 0 <= site < len(SITESLIST):
            self.__site = SITESLIST[site]
            return True
        return False

    ## @brief Method sets first name
    #  @param name String indicating name
    def setFirstName(self, name):
        self.__firstName = name

    ## @brief Method sets last name
    #  @param name String indicating name
    def setLastName(self, name):
        self.__lastName = name

    ## @brief Method tries to set email
    #  @details Method will not change the value if the new input is invalid
    #  @param email String indicating email
    #  @return Boolean True if email was updated, False if not
    def setEmail(self, email):
        if "@" in email and "." in email:
            self.__email = email
            return True
        return False

    ## @brief Method tries to set phone number
    #  @details Method will not change the value if the new input is invalid;
    #  accepts different formats including those with brackets or dashes; do not include
    #  country codes
    #  @param phone String of numbers indicating email
    #  @return Boolean True if email was updated, False if not
    def setPhone(self, phone):
        phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        if len(phone) == 10 and phone.isnumeric():
            self.__phone = phone
            return True
        return False

    ## @brief Method sets organisation
    #  @param org String indicating organisation name
    def setOrganisation(self, org):
        self.__organisation = org

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

    ## @brief Method sets social links
    #  @details When toggleMode = True, only the site name is required to remove an element
    #  @param link A string representing a link
    #  @param toggleMode (optional) If true, instead of overwriting the class varible with 
    #  the parameter, it will add words to the class varable from the parameter that are not 
    #  there and remove ones that are
    def setSocials(self, link, toggleMode = False):
        if toggleMode:
            if link.replace(" ", "") != "":
                removed = False
                for soc in self.getSocials():
                    if link in soc:
                        self.__socials.remove(soc)
                        removed = True
                if not removed: self.__socials.append(link)
        else: 
            self.__socials = DEFAULT["socials"][0] if link == DEFAULT["socials"][0] else [link]

    ## @brief Method sets location
    #  @details If 2 inputs received, it will be stored as a length 3 with a blank value
    #  between the two inputted values so indexing always access the same
    #  kind of location (i.e. country at 2)
    #  @param loc A length 2 or 3 list of strings indicating locations in the form
    #  [city, state/province, country] or [city, country]
    #  @return Boolean True if location was updated, False if not
    def setLocation(self, loc):
        if len(loc) == 2: self.__location = (loc[0], "", loc[1])
        elif len(loc) == 3: self.__location = (loc[0], loc[1], loc[2])
        else: return False
        return True            

    ## @brief Method tries to set grad date
    #  @param grad A length 2 list of strings indicating a month (as name or int) and year
    #  @return Boolean True if date was updated, False if not
    def setGradDate(self, grad):
        if len(grad) == 2 and grad[1].isnumeric():
            if grad[0].isnumeric() and int(grad[0]) > 0 and int(grad[0]) < 13:
                self.__gradDate = (int(grad[0]), int(grad[1]))
                return True
            elif grad[0].lower() in MONTHS:
                self.__gradDate = (MONTHS.index(grad[0].lower()) + 1, int(grad[1]))
                return True
        return False
                
    
    ## @brief Method sets university
    #  @param name String indicating university name
    def setUniversity(self, name):
        self.__university = name
    
    ## @brief Method sets auto login setting
    #  @param val Boolean indicating if auto login should be done
    def setAutoLogin(self, val):
        self.__autoLogin = val


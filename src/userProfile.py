## @file userProfile.py
#  @author Gavin Jameson
#  @brief profile module
#  @date Mar 1, 2022

from menuMessages import wrappedString as wS, waitForUser
from os.path import isfile
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

## @brief this class represents the preferences of a user for job searching 
class userProfile:

    ## @brief constructor for userProfile
    #  @details sets default values for profile
    def __init__(self):
        self.__resumePath = ""
        self.__keywords = []
        self.__site = "glassdoor"

    ## @brief method attempts to load values from the given file to itself
    #  @param file (optional) a path to the saved profile
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

    ## @brief method attempts to save its variable values to the given file
    #  @details will overwrite the file if it exists already
    #  @param file (optional) a path to the profile to write 
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

    ## @brief a method for getting the front top left corner of the box
    #  @return a tuple of three real numbers indicating the location of the front top left corner
    def getFrontTopLeftCorner(self):
        return self.__frontTopLeftCorner

    ## @brief a method for setting the front top left corner of the box
    #  @param newCorner (x, y, z) where x,y,z are real numbers indicating coordinate of the front top left corner
    def setFrontTopLeftCorner(self, newCorner):
        self.__frontTopLeftCorner = newCorner


    ## @brief a method for getting the dimensions of the box
    #  @return a tuple of three real numbers indicating the width, height and depth of the box
    def getDimensions(self):
        return self.__dimensions

    ## @brief a method for getting the dimensions of the box
    #  @param newSize (width, height, depth) where x,y,z are real numbers and
    #  x,y,z are greater than or equal to 0, indicating side lengths
    def setDimensions(self, newSize):
        self.__dimensions = newSize

    ## @brief a method for getting the dimensions of a face
    #  @param face an integer corresponding to the face to get dimensions from; face is one of [0, 1, 2]
    #  @return a tuple of two real numbers indicating the dimensions that define the specified face
    #  @throws ValueError if the face specified does not map to the cube
    def getDimensionsOfFace(self, face):
        if face == Box3D.FRONT:
            width,height = self.__dimensions[0],self.__dimensions[1] # w,h
        elif face == Box3D.TOP:
            width,height = self.__dimensions[0],self.__dimensions[2] # w,d
        elif face == Box3D.SIDE:
            width,height = self.__dimensions[1],self.__dimensions[2] # h,d
        else:
            raise ValueError("Invalid `face` argument")
        return width,height

    ## @brief a method for getting the area of a face
    #  @param face an integer corresponding to the face to get dimensions from; face is one of [0, 1, 2]
    #  @return a real number indicating the area of a face
    def getAreaOfFace(self, face):
        width,height = self.getDimensionsOfFace(face)
        return width * height

    ## @brief a method for getting the perimeter of a face
    #  @param face an integer corresponding to the face to get dimensions from; face is one of [0, 1, 2]
    #  @return a real number indicating the perimeter of a face
    def getPerimeterOfFace(self, face):
        width,height = self.getDimensionsOfFace(face)
        return 2 * (width + height)

    ## @brief a method for getting the volume of the box
    #  @return a real number indicating the volume of the box
    def getVolume(self):
        width,height,depth = self.__dimensions
        return width * height * depth

    ## @brief a method for getting the surface area of the box
    #  @return a real number indicating the surface area of the box
    def getSurfaceArea(self):
        surfaceArea = 0
        for face in (Box3D.FRONT, Box3D.TOP, Box3D.SIDE):
            surfaceArea += (2 * self.getAreaOfFace(face))
        return surfaceArea
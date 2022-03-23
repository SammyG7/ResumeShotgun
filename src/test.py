## @file test.py
#  @author Gavin Jameson
#  @brief Testing for modules
#  @date Mar 23, 2022

import unittest
from userProfile import *
import menu

## @brief Tests
class templateTest(unittest.TestCase):

    ## @brief runs before every test
    def setUp(self):
        pass

    ## @brief tests X
    def testAEqual(self):
        self.assertEqual(1, 1)

    ## @brief tests X
    #  @details catches thrown error
    def testBException(self):
        with self.assertRaises(IndexError):
            a = [][0]

## @brief Setup for userProfile module
class userProfileBase(unittest.TestCase):

    ## @brief Runs before every test
    def setUp(self):
        self.profile = userProfile(userPrompts = False)

    ## @brief Fills in profile with non-default values
    def loadFull(self):
        self.profile.loadProfile(file = "test1.yaml")

    ## @brief Creates saved profile file for test purposes
    def makeFullProfile(self):
        # self.profile.set--
        # self.profile.saveProfile("test1.yaml")
        pass

## @brief Tests for userProfile module
class userProfileTest(userProfileBase):
    
    ## @brief tests X
    def testAEqual(self):
        self.loadFull()
        self.profile.getResumePath()
        self.assertEqual(1, 1)

    ## @brief tests X
    #  @details catches thrown error
    def testBException(self):
        with self.assertRaises(IndexError):
            a = [][0]

## @brief Allows manual tests for menu module
class menuTest(userProfileBase):
    
    ## @brief Sets states for manual keyword menu testing
    def testKeywords(self):
        menu.run(self.profile)
        self.assertEqual(input("RESULT --\n" +
                               "Keywords tests: "), "y")

if __name__ == '__main__':
    unittest.main()    

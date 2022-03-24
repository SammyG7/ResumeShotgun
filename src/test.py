## @file test.py
#  @author Gavin Jameson
#  @brief Testing for modules
#  @date Mar 23, 2022

import unittest
from userProfile import *
from menuMessages import waitForUser
from indeed import Indeed
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

## @brief Sends message about info needed for manual test
#  and waits for confirmation
#  @param subject String indicating information about testing
def __testBrief(subject):
    print("-- PLEASE CHECK --\n" + subject)
    waitForUser()

## @brief Interfaces with manual assertion of test
#  @param subject String indicating information about testing
#  @return Boolean True if tester indicated test passed, False if not
def __testResult(subject):
    return "y" == input("-- RESULT --\n" + subject + "\n(y/n): ")

## @brief Allows manual tests for menu module
class menuTest(userProfileBase):
    
    ## @brief Sets states for manual keyword menu testing
    def testKeywords(self):
        subj = "Keywords menu, resetting, toggling"
        __testBrief(subj)
        menu.run(self.profile)
        self.assertTrue(__testResult(subj))

class indeedTest(unittest.TestCase):

    ## @brief Tests for valid input but no results
    def test_noResults(self):
        search = Indeed("foo", "bar")
        search.getJob()
        size = len(search.jobs)
        self.assertEqual(0, size)


    ## @brief Tests for an invalid keyword
    def test_invalidSearch1(self):
        try:
            Indeed(123,"bar")
        except TypeError:
            self.assertTrue(True)

    ## @brief Tests for an invalid location
    def test_invalidSearch2(self):
        try:
            Indeed("Engineer",321)
        except TypeError:
            self.assertTrue(True)

    ## @brief Tests for an valid keyword and location with all results on single page
    def test_getJobsSinglePage(self):
        s2 = Indeed("Engineer", "Huntsville")
        s2.getJob()
        size2 = len(s2.jobs)
        self.assertEqual(15, size2)
    
    ## @brief Tests for an valid keyword and location with all results multiple pages
    def test_getJobsSinglePage(self):
        s3 = Indeed("Engineer", "Collingwood")
        s3.run()
        size3 = len(s3.jobs)
        self.assertEqual(45, size3)       

    ## @brief Tests for an valid keyword and location with all results multiple pages
    def test_getJobsMultiplePages(self):
        s4 = Indeed("Engineer", "Collingwood")
        s4.run()
        size4 = len(s4.jobs)
        self.assertEqual(45, size4)

    pass
if __name__ == '__main__':
    unittest.main()    

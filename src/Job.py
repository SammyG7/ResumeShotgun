## @file Job.py
#  @author Jeremy Langner
#  @brief Module that creates job class with various methods
#  @date March 23, 2022

class Job:

    title = ""
    company = ""
    link = ""

    ## @brief Constructs a job using.
    def __init__(self):
        self.title = ""
        self.company = ""
        self.link = ""

    ## @brief Setter method for Job title.
    #  @param newTitle represents the new title to be set.
    def setTitle(self, newTitle):
        self.title = newTitle

    ## @brief Setter method for Job companyh.
    #  @param newTitle represents the new company to be set.
    def setCompany(self, newCompany):
        self.company = newCompany

    ## @brief Setter method for Job link.
    #  @param newTitle represents the new link to be set.
    def setLink(self, newLink):
        self.link = newLink
## @file pDef.py
#  @author Gavin Jameson
#  @brief General information about the user profile module that needs to be accessed in numerous places
#  @date Mar 31, 2022

## @brief Dictionary of default variable states and if they need updating for use
#  @details Tuple; index 0 is value, index 1 is if it requires changing
DEFAULT = {
    "keywords": ([], False),
    "jobTitle": ("", True),
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
    "university": ("", False),
    "autoLogin": (None, False) # not a boolean so changes can be detected, getter converts blank to False
}

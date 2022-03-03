## @file sites.py
#  @author Gavin Jameson
#  @brief sites "dictionary"
#  @date Mar 2, 2022

## @brief List of strings indicating supported sites
#  @details In order of implementation, arbitrarily chosen to be this way
SITESLIST = ["glassdoor", "indeed"]

## @brief Dictionary to link site name to correct file for scraping links
GETLINKSFILE = {
	"glassdoor": "get_links_glassdoor.py",
	"indeed": "get_links_indeed.py"
}

SOCIALS = ["github", "linkedin", "youtube", "twitter"]

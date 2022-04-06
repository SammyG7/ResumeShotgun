## @file sites.py
#  @author Gavin Jameson
#  @brief sites "dictionary"
#  @date Mar 2, 2022

## @brief List of strings indicating supported sites
#  @details In order of implementation, arbitrarily chosen to be this way
SITESLIST = ["glassdoor", "indeed"]

## @brief Dictionary to swap site name to correct file for scraping links
GETLINKSFILE = {
	"glassdoor": "get_links_glassdoor.py",
	"indeed": "get_links_indeed.py"
}

## @brief Dictionary to swap name of site to a formattable string
#  indicating URL
__SOCIALLINKS = {
    "github": "github.com/{0}",
    "linkedin": "linkedin.com/in/{0}",
    "twitter": "twitter.com/{0}"
}

## @brief Method converts website name and username to URL
#  @param username String indicating username on site
#  @param site String indicating title of site
#  @return String indicating URL of user's profile on the site
def userToURL(username, site):
    url = ""
    if site in __SOCIALLINKS:
        url = __SOCIALLINKS[site].format(username)
    return url

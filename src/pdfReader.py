## @file pdfReader.py
#  @author Sam Gorman
#  @brief PDF Interpretor
#  @date Mar 17, 2022

## @brief This class represents a PDF document  
#  @details Assumes all inputs are of the correct type
class PDF:

    ## @brief Constructor for PDF
    #  @details Defines a PDF based on a file path
    #  @param path: String value which describes the file path to the desired document
    def __init__(self, path):
        pass

    ## @brief Displays the document to the user in an interactive window
    def display(self):
        pass

    ## @brief Searches the PDF for a specified keyword
    #  @param key: String value which is searched for
    #  @return Boolean value based on whether or not the key could be found
    def search(self, key):
        pass

    ## @brief Splits the PDF document into two seperate PDF objects
    #  @param page: Integer value defining at which page the PDF should be split
    #  @return Tuple of PDF objects
    def split(self, page):
        pass

    ## @brief Merges two PDF objects into a single object
    #  @param pdf: PDF object that will be merged with current PDF
    #  @return PDF object
    def merge(self, pdf):
        pass

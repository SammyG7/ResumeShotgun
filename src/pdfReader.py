## @file pdfReader.py
#  @author Sam Gorman
#  @brief PDF Interpretor
#  @date Mar 17, 2022

import fitz # pymuPDF
import wx # GUI
import sys
import re

## @brief This class represents a PDF document  
#  @details Assumes all inputs are of the correct type
class pdfReader:
    ## @brief Constructor for pdfReader
    #  @details Defines a PDF based on a file path
    #  @param path: String value which describes the file path to the desired document
    def __init__(self, path = None, testBool = False):# Add param for has correct imports
        self.path = path
        self.app = wx.App()
        self.doc = None
        self.links = []
        self.expectedlinks = {}
        
        try: # Try instead of if for invalid paths
            self.plaintext = self.getText()
            self.getAllLinks()
            self.setKnownLinks()
        except:
            self.plaintext = None

    ## @brief Gets the current path to PDF
    #  @return String representing the path
    def getPath(self):
        return self.path

    ## @brief Creates window to browse for file
    def browse(self):
        ## Create Dialog
        dlg = wx.FileDialog(None, message = "Choose a file to display",
                    wildcard = "*.pdf", style=wx.FD_OPEN|wx.FD_CHANGE_DIR)

        ## Pull Up Window
        dlg.ShowModal()

        self.path = dlg.GetPath()

    ## @brief Displays the document to the user in an interactive window
    def showPDF(self):
        self.doc = fitz.open(self.path) # create Document object

        self.dl_array = [0] * len(self.doc)
        self.last_page = -1            # memorize last page displayed
        self.link_rects = []           # store link rectangles here
        self.link_texts = []           # store link texts here
        self.current_idx = -1          # store entry of found rectangle
        self.current_lnks = []         # store entry of found rectangle

        self.TextToPage = wx.TextCtrl(self, wx.ID_ANY, u"1", defPos, wx.Size(40, -1), 
                             wx.TE_RIGHT|wx.TE_PROCESS_ENTER)

        self.doc.close()

    ## @brief Transforms the pdf to plaintext
    #  @return String on plaintext
    def getText(self):
        text = ''
        
        with fitz.open(self.path) as doc:
            for page in doc:
                text+= page.get_text()

        return text
        #print(text)
        #print("Musk" in text)
        #print("Sam" in text)

    ## @brief Checks user imports
    #  @return Boolean value based on whether or not the import could be found
    def checkImports(self):
        imports = sys.modules.keys()
       
        return 'wx' in a

    ## @brief Searches the PDF for a specified keyword
    #  @param key: String value which is searched for
    #  @return Boolean value based on whether or not the key could be found
    def search(self, key):
        return key in self.plaintext

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

    def getAllLinks(self):
        l = self.links
        l.extend(re.findall("htt.*\S|www.*\S", self.plaintext))
        self.links = list(set(l)) # Remove Duplicates

    def setKnownLinks(self):
        for link in self.links:
            if "github" in link:
                self.expectedlinks["git"] = link
            elif "linkedin" in link:
                self.expectedlinks["linkedin"] = link
                
        









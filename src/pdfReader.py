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
class pdfReader(wx.Dialog):
    ## @brief Constructor for pdfReader
    #  @details Defines a PDF based on a file path
    #  @param path: String value which describes the file path to the desired document
    def __init__(self, path = None, testBool = False):# Add param for has correct imports
        self.path = path
        self.app = wx.App()
        self.doc = None
        self.links = []
        self.expectedinfo = {}
        self.expectedinfo["links"] = {}
        self.expectedinfo["languages"] = {}
        #self.display = Display(path)
        
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
        defPos = wx.DefaultPosition
        defSiz = wx.DefaultSize
        zoom   = 1.2                        # zoom factor of display
        wx.Dialog.__init__ (self, None, id = wx.ID_ANY,
            title = u"Display with PyMuPDF: ",
            pos = defPos, size = defSiz,
            style = wx.CAPTION|wx.CLOSE_BOX|
                    wx.DEFAULT_DIALOG_STYLE)
        self.doc = fitz.open(self.path) # create Document object

        self.dl_array = [0] * len(self.doc)
        self.last_page = -1            # memorize last page displayed
        self.link_rects = []           # store link rectangles here
        self.link_texts = []           # store link texts here
        self.current_idx = -1          # store entry of found rectangle
        self.current_lnks = []         # store entry of found rectangle

        self.matrix = fitz.Matrix(zoom, zoom)
        
        self.TextToPage = wx.TextCtrl(self, wx.ID_ANY, u"1", defPos, wx.Size(40, -1), 
                             wx.TE_RIGHT|wx.TE_PROCESS_ENTER)

        self.PDFimage = wx.StaticBitmap(self, wx.ID_ANY, self.pdf_show(1),
                           defPos, defSiz, style = 0)

        self.szr10 = wx.BoxSizer(wx.VERTICAL)
        szr20 = wx.BoxSizer(wx.HORIZONTAL)
        #szr20.Add(self.ButtonNext, 0, wx.ALL, 5)
        #szr20.Add(self.ButtonPrevious, 0, wx.ALL, 5)
        szr20.Add(self.TextToPage, 0, wx.ALL, 5)
        #szr20.Add(self.statPageMax, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        #szr20.Add( self.links, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        #szr20.Add(self.paperform, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # sizer ready, represents top dialog line
        self.szr10.Add(szr20, 0, wx.EXPAND, 5)
        self.szr10.Add(self.PDFimage, 0, wx.ALL, 5)
        # main sizer now ready - request final size & layout adjustments
        self.szr10.Fit(self)
        self.SetSizer(self.szr10)
        self.Layout()
        # center dialog on screen
        self.Centre(wx.BOTH)

        # Bind buttons and fields to event handlers
        #self.ButtonNext.Bind(wx.EVT_BUTTON, self.NextPage)
        #self.ButtonPrevious.Bind(wx.EVT_BUTTON, self.PreviousPage)
        #self.TextToPage.Bind(wx.EVT_TEXT_ENTER, self.GotoPage)
        ##self.PDFimage.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        ##self.PDFimage.Bind(wx.EVT_MOTION, self.move_mouse)
        ##self.PDFimage.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

        self.doc.close()

    ## @brief Transforms the pdf to plaintext
    #  @return String on plaintext
    def getText(self):
        text = ''
        with fitz.open(self.path) as doc:
            for page in doc:
                text+= page.get_text()

        #print(text)
        return text
        #print(text)
        #print("Musk" in text)
        #print("Sam" in text)

    def setPath(self):
        self.path = path

        try: # Try instead of if for invalid paths
            self.plaintext = self.getText()
            self.getAllLinks()
            self.setKnownLinks()
        except:
            self.plaintext = None

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
                self.expectedinfo["links"]["git"] = True
            else:
                self.expectedinfo["links"]["git"] = False
            if "linkedin" in link:
                self.expectedinfo["links"]["linkedin"] = True
            else:
                self.expectedinfo["links"]["linkedin"] = False

        # Email
        # 

    def setKnownLanguages(self):
        if "python" in self.plaintext or "Python" in self.plaintext:
            self.expectedinfo["languages"]["python"] = True
        else:
            self.expectedinfo["languages"]["python"] = False
            
        if "java" in self.plaintext or "Java" in self.plaintext:
            self.expectedinfo["languages"]["java"] = True
        else:
            self.expectedinfo["languages"]["Java"] = False

        if "go" in self.plaintext or "Go" in self.plaintext:
            self.expectedinfo["languages"]["go"] = True
        else:
            self.expectedinfo["languages"]["go"] = False

        if "c++" in self.plaintext or "C++" in self.plaintext:
            self.expectedinfo["languages"]["c++"] = True
        else:
            self.expectedinfo["languages"]["c++"] = False

        if "javascript" in self.plaintext or "JavaScript" in self.plaintext:
            self.expectedinfo["languages"]["javascript"] = True
        else:
            self.expectedinfo["languages"]["javascript"] = False

    def pdf_show(self, pg_nr):
        pno = int(pg_nr) - 1
        if self.dl_array[pno] == 0:
            self.dl_array[pno] = self.doc[pno].get_displaylist()
        dl = self.dl_array[pno]
        pix = dl.get_pixmap(matrix = self.matrix, alpha = False)
        bmp = wx.Bitmap.FromBuffer(pix.w, pix.h, pix.samples)
        r = dl.rect
        #paper = FindFit(r.x1, r.y1)
        #self.paperform.Label = "Page format: " + paper
        '''
        if self.links.Value:
            self.current_lnks = self.doc[pno].get_links()
            self.pg_ir = dl.rect.irect
        '''
        pix = None
        return bmp

'''
class Display(wx.Dialog):
    def __init__(self, path):
        self.dl_array = [0] * len(self.doc)
        self.last_page = -1            # memorize last page displayed
        self.link_rects = []           # store link rectangles here
        self.link_texts = []           # store link texts here
        self.current_idx = -1          # store entry of found rectangle
        self.current_lnks = []         # store entry of found rectangle
'''

## Test
p = pdfReader("Resumes/BobBobberResume.pdf")
print(p.plaintext)
p.showPDF()
##p.setKnownLanguages()
##print(p.expectedinfo)

## Auto Cover Letter
# Template cover letter with insert company, insert location, etc
# 
#
#
#
                
        









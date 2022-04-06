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
        self.expectedinfo = {}
        self.expectedinfo["links"] = {}
        self.expectedinfo["languages"] = {}
        
        try: # Try instead of if for invalid paths
            if(path != None and path != ''):
                self.plaintext = self.getText()
                self.getAllLinks()
                self.setKnownLinks()
                self.setKnownLanguages()
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
        app = wx.App()
        dlg = PDFdisplay(None, self.path)
        rc = dlg.ShowModal()

    ## @brief Transforms the pdf to plaintext
    #  @return String on plaintext
    def getText(self):
        text = ''
    
        with fitz.open(self.path) as doc:
            for page in doc:
                text+= page.get_text()

        return text

    def setPath(self, path):
        self.path = path

        try: # Try instead of if for invalid paths
            self.plaintext = self.getText()
            self.getAllLinks()
            self.setKnownLinks()
            self.setKnownLanguages()
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
                self.expectedinfo["links"]["git"] = [True, link]
            else:
                self.expectedinfo["links"]["git"] = [False, '']
            if "linkedin" in link:
                self.expectedinfo["links"]["linkedin"] = [True, link]
            else:
                self.expectedinfo["links"]["linkedin"] = [False, '']
            if "@" in link:
                self.expectedinfo["links"]["email"] = [True, link]
            else:
                self.expectedinfo["links"]["email"] = [False, '']
                

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

class PDFdisplay(wx.Dialog):
    def __init__(self, parent, filename):
        defPos = wx.DefaultPosition
        defSiz = wx.DefaultSize
        zoom   = 1.2                        # zoom factor of display
        wx.Dialog.__init__ (self, parent, id = wx.ID_ANY,
            title = u"Display with PyMuPDF: ",
            pos = defPos, size = defSiz,
            style = wx.CAPTION|wx.CLOSE_BOX|
                    wx.DEFAULT_DIALOG_STYLE)

        #======================================================================
        # display an icon top left of dialog, append filename to title
        #======================================================================
##        if do_icon:
##            self.SetIcon(ico_pdf.img.GetIcon())      # set a screen icon
        self.SetTitle(self.Title + filename)
        self.SetBackgroundColour(wx.Colour(240, 230, 140))

        #======================================================================
        # open the document with MuPDF when dialog gets created
        #======================================================================
        self.doc = fitz.open(filename) # create Document object
        if self.doc.needs_pass:         # check password protection
            self.decrypt_doc()
        if self.doc.is_encrypted:       # quit if we cannot decrpt
            self.Destroy()
            return
        self.dl_array = [0] * len(self.doc)
        self.last_page = -1            # memorize last page displayed
        self.link_rects = []           # store link rectangles here
        self.link_texts = []           # store link texts here
        self.current_idx = -1          # store entry of found rectangle
        self.current_lnks = []         # store entry of found rectangle

        #======================================================================
        # define zooming matrix for displaying PDF page images
        # we increase images by 20%, so take 1.2 as scale factors
        #======================================================================
        self.matrix = fitz.Matrix(zoom, zoom)    # will use a constant zoom

        '''
        =======================================================================
        Overall Dialog Structure:
        -------------------------
        szr10 (main sizer for the whole dialog - vertical orientation)
        +-> szr20 (sizer for buttons etc. - horizontal orientation)
          +-> button forward
          +-> button backward
          +-> field for page number to jump to
          +-> field displaying total pages
        +-> PDF image area
        =======================================================================
        '''

        # forward button
        self.ButtonNext = wx.Button(self, wx.ID_ANY, u"forw",
                           defPos, defSiz, wx.BU_EXACTFIT)
        # backward button
        self.ButtonPrevious = wx.Button(self, wx.ID_ANY, u"back",
                           defPos, defSiz, wx.BU_EXACTFIT)
        #======================================================================
        # text field for entering a target page. wx.TE_PROCESS_ENTER is
        # required to get data entry fired as events.
        #======================================================================
        self.TextToPage = wx.TextCtrl(self, wx.ID_ANY, u"1", defPos, wx.Size(40, -1), 
                             wx.TE_RIGHT|wx.TE_PROCESS_ENTER)
        # displays total pages and page paper format
        self.statPageMax = wx.StaticText(self, wx.ID_ANY,
                              "of " + str(len(self.doc)) + " pages.",
                              defPos, defSiz, 0)
        self.links = wx.CheckBox( self, wx.ID_ANY, u"show links",
                           defPos, defSiz, wx.ALIGN_LEFT)
        self.links.Value = True
        self.paperform = wx.StaticText(self, wx.ID_ANY, "", defPos, defSiz, 0)
        # define the area for page images and load page 1 for primary display
        self.PDFimage = wx.StaticBitmap(self, wx.ID_ANY, self.pdf_show(1),
                           defPos, defSiz, style = 0)
        #======================================================================
        # the main sizer of the dialog
        #======================================================================
        self.szr10 = wx.BoxSizer(wx.VERTICAL)
        szr20 = wx.BoxSizer(wx.HORIZONTAL)
        szr20.Add(self.ButtonNext, 0, wx.ALL, 5)
        szr20.Add(self.ButtonPrevious, 0, wx.ALL, 5)
        szr20.Add(self.TextToPage, 0, wx.ALL, 5)
        szr20.Add(self.statPageMax, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        szr20.Add( self.links, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        szr20.Add(self.paperform, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
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
        self.ButtonNext.Bind(wx.EVT_BUTTON, self.NextPage)
        self.ButtonPrevious.Bind(wx.EVT_BUTTON, self.PreviousPage)
        self.TextToPage.Bind(wx.EVT_TEXT_ENTER, self.GotoPage)
        self.PDFimage.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        self.PDFimage.Bind(wx.EVT_MOTION, self.move_mouse)
        self.PDFimage.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

#==============================================================================
# Button handlers and other functions
#==============================================================================
    def OnLeftDown(self, evt):
        if self.current_idx < 0 or not self.links.Value:
            evt.Skip()
            return
        lnk = self.current_lnks[self.current_idx]
        if lnk["kind"] == fitz.LINK_GOTO:
            self.TextToPage.Value = str(lnk["page"] + 1)
            self.GotoPage(evt)
        elif lnk["kind"] == fitz.LINK_URI:
            import webbrowser
            try:
                webbrowser.open_new(self.link_texts[self.current_idx])
            except:
                pass
        elif lnk["kind"] == fitz.LINK_GOTOR:
            import subprocess
            try:
                subprocess.Popen(self.link_texts[self.current_idx])
            except:
                pass
        elif lnk["kind"] == fitz.LINK_NAMED:
            if lnk["name"] == "FirstPage":
                self.TextToPage.Value = "1"
            elif lnk["name"] == "LastPage":
                self.TextToPage.Value = str(len(self.doc))
            elif lnk["name"] == "NextPage":
                self.TextToPage.Value = str(int(self.TextToPage.Value) + 1)
            elif lnk["name"] == "PrevPage":
                self.TextToPage.Value = str(int(self.TextToPage.Value) - 1)
            self.GotoPage(evt)
        evt.Skip()
        return

    def move_mouse(self, evt):                   # show hand if in a rectangle
        if not self.links.Value:                 # do not process links
            evt.Skip()
            return
        if len(self.link_rects) == 0:
            evt.Skip()
            return
        pos = evt.GetPosition()
        self.current_idx = self.cursor_in_link(pos)   # get cursor link rect
        
        if self.current_idx >= 0:                     # if in a hot area
            cursor_hand  = wx.Cursor(wx.CURSOR_HAND)
            self.PDFimage.SetCursor(cursor_hand)
            phoenix = True
            if phoenix:
                self.PDFimage.SetToolTip(self.link_texts[self.current_idx])
            else:
                self.PDFimage.SetToolTipString(self.link_texts[self.current_idx])
        else:
            cursor_norm  = wx.Cursor(wx.CURSOR_DEFAULT)
            self.PDFimage.SetCursor(cursor_norm)
            self.PDFimage.UnsetToolTip()

        evt.Skip()
        return

    def OnMouseWheel(self, evt):
        # process wheel as paging operations
        d = evt.GetWheelRotation()               # int indicating direction
        if d < 0:
            self.NextPage(evt)
        elif d > 0:
            self.PreviousPage(evt)
        return

    def NextPage(self, event):                   # means: page forward
        page = self.getint(self.TextToPage.Value) + 1 # current page + 1
        page = min(page, self.doc.page_count)     # cannot go beyond last page
        self.TextToPage.Value = str(page)        # put target page# in screen
        self.NeuesImage(page)                    # refresh the layout
        event.Skip()

    def PreviousPage(self, event):               # means: page back
        page = self.getint(self.TextToPage.Value) - 1 # current page - 1
        page = max(page, 1)                      # cannot go before page 1
        self.TextToPage.Value = str(page)        # put target page# in screen
        self.NeuesImage(page)
        event.Skip()

    def GotoPage(self, event):                   # means: go to page number
        page = self.getint(self.TextToPage.Value)     # get page# from screen
        page = min(page, len(self.doc))          # cannot go beyond last page
        page = max(page, 1)                      # cannot go before page 1
        self.TextToPage.Value = str(page)        # make sure it's on the screen
        self.NeuesImage(page)
        event.Skip()

#==============================================================================
# Read / render a PDF page. Parameters are: pdf = document, page = page#
#==============================================================================
    def NeuesImage(self, page):
        if page == self.last_page:
            return
        cursor_norm  = wx.Cursor(wx.CURSOR_DEFAULT)
        self.PDFimage.SetCursor(cursor_norm)
        self.PDFimage.UnsetToolTip()
        self.last_page = page
        self.link_rects = []
        self.link_texts = []
        bitmap = self.pdf_show(page)        # read page image
        if self.links.Value and len(self.current_lnks) > 0:     # show links?
            self.draw_links(bitmap, page)   # modify the bitmap
        self.PDFimage.SetBitmap(bitmap)     # put it in screen
        self.szr10.Fit(self)
        self.Layout()
        # image may be truncated, so we need to recalculate hot areas
        if len(self.current_lnks) > 0:
            isize = self.PDFimage.Size
            bsize = self.PDFimage.Bitmap.Size
            dis_x = (bsize[0] - isize[0]) / 2.
            dis_y = (bsize[1] - isize[1]) / 2.
            zoom_w = float(bsize[0]) / float(self.pg_ir.width)
            zoom_h = float(bsize[1]) / float(self.pg_ir.height)
            for l in self.current_lnks:
                r = l["from"]
                wx_r = wx.Rect(int(r.x0 * zoom_w - dis_x),
                           int(r.y0 * zoom_h) - dis_y,
                           int(r.width * zoom_w),
                           int(r.height * zoom_h))
                self.link_rects.append(wx_r)
                
        return

    def cursor_in_link(self, pos):
        for i, r in enumerate(self.link_rects):
            if r.Contains(pos):
                return i
        return -1
        
    def draw_links(self, bmp, pno):
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetPen(wx.Pen("BLUE", width=1))
        dc.SetBrush(wx.Brush("BLUE", style=wx.BRUSHSTYLE_TRANSPARENT))
        pg_w = self.pg_ir.x1 - self.pg_ir.x0
        pg_h = self.pg_ir.y1 - self.pg_ir.y0
        zoom_w = float(bmp.Size[0]) / float(pg_w)
        zoom_h = float(bmp.Size[1]) / float(pg_h)
        for lnk in self.current_lnks:
            r = lnk["from"].irect
            wx_r = wx.Rect(int(r.x0 * zoom_w),
                           int(r.y0 * zoom_h),
                           int(r.width * zoom_w),
                           int(r.height * zoom_h))
            dc.DrawRectangle(wx_r[0], wx_r[1], wx_r[2]+1, wx_r[3]+1)
            if lnk["kind"] == fitz.LINK_GOTO:
                txt = "page " + str(lnk["page"] + 1)
            elif lnk["kind"] == fitz.LINK_GOTOR:
                txt = lnk["file"]
            elif lnk["kind"] == fitz.LINK_URI:
                txt = lnk["uri"]
            else:
                txt = "unkown destination"
            self.link_texts.append(txt)
        dc.SelectObject(wx.NullBitmap)
        dc = None
        return

    def pdf_show(self, pg_nr):
        pno = int(pg_nr) - 1
        if self.dl_array[pno] == 0:
            self.dl_array[pno] = self.doc[pno].get_displaylist()
        dl = self.dl_array[pno]
        pix = dl.get_pixmap(matrix = self.matrix, alpha = False)
        bmp_buffer = wx.Bitmap.FromBuffer
        bmp = bmp_buffer(pix.w, pix.h, pix.samples)
        r = dl.rect
        #paper = FindFit(r.x1, r.y1)
        #print(paper)
        #self.paperform.Label = "Page format: " + paper
        if self.links.Value:
            self.current_lnks = self.doc[pno].get_links()
            self.pg_ir = dl.rect.irect
        pix = None
        return bmp

    def decrypt_doc(self):
        # let user enter document password
        pw = None
        dlg = wx.TextEntryDialog(self, 'Please enter password below:',
                 'Document needs password to open', '',
                 style = wx.TextEntryDialogStyle|wx.TE_PASSWORD)
        while pw is None:
            rc = dlg.ShowModal()
            if rc == wx.ID_OK:
                pw = str(dlg.GetValue().encode("utf-8"))
                self.doc.authenticate(pw)
            else:
                return
            if self.doc.is_encrypted:
                pw = None
                dlg.SetTitle("Wrong password. Enter correct one or cancel.")
        return

    def getint(self, v):
        try:
            return int(v)
        except:
            pass
        if type(v) not in stringtypes:
            return 0
        a = "0"
        for d in v:
            if d in "0123456789":
                a += d
        return int(a)

## Test
##p = pdfReader("Resumes/BobBobberResume.pdf")
##print(p.plaintext)
##p.showPDF()
##p.setKnownLanguages()
##print(p.expectedinfo)

## Auto Cover Letter
# Template cover letter with insert company, insert location, etc
# 
#
#
#
                
        









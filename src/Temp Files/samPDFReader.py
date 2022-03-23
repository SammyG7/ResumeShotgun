import fitz # pymuPDF
import wx # GUI

class pdfReader:
    def __init__(self, path = None):
        self.path = path
        self.app = wx.App()
        self.doc = None

    def getPath(self):
        return self.path

    def browse(self):
        ## Create Dialog
        dlg = wx.FileDialog(None, message = "Choose a file to display",
                    wildcard = "*.pdf", style=wx.FD_OPEN|wx.FD_CHANGE_DIR)

        ## Pull Up Window
        dlg.ShowModal()

        self.path = dlg.GetPath()

    def showPDF(self):
        self.doc = fitz.open(self.path) # create Document object

        self.dl_array = [0] * len(self.doc)
        self.last_page = -1            # memorize last page displayed
        self.link_rects = []           # store link rectangles here
        self.link_texts = []           # store link texts here
        self.current_idx = -1          # store entry of found rectangle
        self.current_lnks = []         # store entry of found rectangle

    def getText(self):
        text = ''
        
        with fitz.open(self.path) as doc:
            for page in doc:
                text+= page.get_text()
                
        print(text)
        print("Musk" in text)
        print("Sam" in text)

p1 = pdfReader("Test")
p2 = pdfReader()

print(p1.getPath())
print(p2.getPath())

p2.browse()

print(p2.getPath())
#p2.showPDF()

p2.getText();
        

import fitz # pymuPDF
import wx # GUI

dlg = wx.FileDialog(None, message = "Choose a file to display",
                    wildcard = wild, style=wx.FD_OPEN|wx.FD_CHANGE_DIR)

'''
FileDialog(parent, message=FileSelectorPromptStr,
           defaultDir="", defaultFile="",
           wildcard=FileSelectorDefaultWildcardStr, style=FD_DEFAULT_STYLE,
           pos=DefaultPosition, size=DefaultSize, name=FileDialogNameStr)
'''

import wx

def OnOpen(self, event):
    if self.contentNotSaved:
        if wx.MessageBox("Current content has not been saved! Proceed?", "Please confirm",
                         wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
            return

    # otherwise ask the user what new file to open
    with wx.FileDialog(self, "Open XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed their mind

        # Proceed loading the file chosen by the user
        pathname = fileDialog.GetPath()
        try:
            with open(pathname, 'r') as file:
                self.doLoadDataOrWhatever(file)
        except IOError:
            wx.LogError("Cannot open file '%s'." % newfile)

def samOpen():
    dlg = wx.FileDialog(None, message = "Choose a file to display",
                    wildcard = "*.pdf", style=wx.FD_OPEN|wx.FD_CHANGE_DIR)

    dlg.ShowModal() # Pulls up explorer window

    file = dlg.GetPath()

    print(file)

app = None
app = wx.App()

#OnOpen()
samOpen()
print("Done")

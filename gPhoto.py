import wx
from wx import xrc

class MyApp(wx.App):
    mPass = ""

    def OnInit(self):
        self.res = xrc.XmlResource('gui.xrc')
        self.init_frame()
        return True

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'frameMain')
        
        # self.favicon = wx.Icon('./ip.ico', wx.BITMAP_TYPE_ICO)
        # self.frame.SetIcon(self.favicon)        

        # Bind Controls
        # self.lblIP = xrc.XRCCTRL(self.frame, 'lblIP')
        # self.btnOK = xrc.XRCCTRL(self.frame, 'wxID_OK')
        # self.btnOK.SetDefault()

        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_EXIT'))
        
        mPass = self.getPassword()
        if not mPass:
            MyApp.Exit(self)
        else:
            print mPass
                
        self.frame.Show()

    def getPassword(self):
        # TODO: Allow for other users
        dialog = wx.TextEntryDialog(None,
        "Password for timcking",
        "Google Login", "", style=wx.OK|wx.CANCEL)
        
        if dialog.ShowModal() == wx.ID_OK:
            pw = dialog.GetValue()
            return pw
        else:
            return none
        
        dialog.Destroy()        
            
    def OnClose(self, evt):
        self.Close()    
        
    def OnExit(self, evt):
        self.Exit()    

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

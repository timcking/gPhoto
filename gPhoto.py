import wx
from wx import xrc

class MyApp(wx.App):

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
        # self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_OK'))
        
        # Do something before or after this
        self.frame.Show()

    def OnClose(self, evt):
        self.Exit()    

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

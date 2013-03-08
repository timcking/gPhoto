import wx
from wx import xrc
from gData import gData

class MyApp(wx.App):
    # Format for dictionary: {index: ('album_id')}
    dictAlbum = {}
    # Format for photo dict: {index: (photo_id, url, caption, addl_info)}
    dictPhoto = {}    
    
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
        self.listAlbums = xrc.XRCCTRL(self.frame, 'listAlbums')
        self.listPhotos = xrc.XRCCTRL(self.frame, 'listPhotos')
        self.btnClose = xrc.XRCCTRL(self.frame, 'wxID_CLOSE')

        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_CLOSE'))
        self.frame.Bind(wx.EVT_CLOSE, self.OnExitApp)
        self.listAlbums.Bind(wx.EVT_LISTBOX, self.OnListAlbumsListbox, id=xrc.XRCID('listAlbums'))
        
        mPass = self.getPassword()
        if not mPass:
            # ToDo
            pass
        else:
            print mPass
        
        # Instantiate
        photo = gData(mPass)
        # Load Album Data
        albums = photo.load_albums()        
        
        index_count = 0
        for album in albums.entry:
            self.listAlbums.Append('%s' % album.title.text)
            self.dictAlbum[index_count] = album.gphoto_id.text
            index_count += 1        
            # print 'title: %s, number of photos: %s, id: %s' % (album.title.text, album.numphotos.text, album.gphoto_id.text)
        
        self.frame.Show()

    def getPassword(self):
        # TODO: Allow for other users
        dialog = wx.TextEntryDialog(None,
        "Password for timcking",
        "Google Login", "", style=wx.OK|wx.CANCEL)
        
        if dialog.ShowModal() == wx.ID_OK:
            pw = dialog.GetValue()
            return pw
        #TODO: Button Cancel
        
        dialog.Destroy()        
        
    def OnListAlbumsListbox(self, event):
        # self.btnInfo.Enable(False)
        self.listPhotos.Clear()
        selected = self.listAlbums.GetSelection()
        
        # Get saved Album ID
        album_id = self.dictAlbum[selected]        
        # Load Photo Data    
        # albums = photo.load_albums()        
        # tmp = photo.load_photos(album_id)
        
        print "Album list clicked: " + album_id
            
    def OnClose(self, evt):
        self.Exit()
        
    def OnExitApp(self, event):
        self.Exit()
         
if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

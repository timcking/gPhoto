import wx
from wx import xrc
import time
from gData import gData
from wx.lib.dialogs import ScrolledMessageDialog

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
        # self.btnOK.SetDefault()
        self.listAlbums = xrc.XRCCTRL(self.frame, 'listAlbums')
        self.listPhotos = xrc.XRCCTRL(self.frame, 'listPhotos')
        self.btnInfo = xrc.XRCCTRL(self.frame, 'btnInfo')
        self.btnView = xrc.XRCCTRL(self.frame, 'btnView')
        self.btnClose = xrc.XRCCTRL(self.frame, 'wxID_CLOSE')

        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_CLOSE'))
        self.frame.Bind(wx.EVT_CLOSE, self.OnExitApp)
        self.listAlbums.Bind(wx.EVT_LISTBOX, self.OnListAlbumsListbox, id=xrc.XRCID('listAlbums'))
        self.listPhotos.Bind(wx.EVT_LISTBOX, self.OnListPhotosListbox, id=xrc.XRCID('listPhotos'))
        self.btnInfo.Bind(wx.EVT_BUTTON, self.OnBtnInfoButton, id=xrc.XRCID('btnInfo'))
        
        self.btnInfo.Enable(False)
        self.btnView.Enable(False)
        
        mPass = self.getPassword()
        if not mPass:
            # ToDo
            pass
        else:
            print mPass
        
        # Instantiate
        self.photoData = gData(mPass)
        # Load Album Data
        albums = self.photoData.load_albums()
        
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
        
    def OnBtnInfoButton(self, event):
        # Display additional info
        selected = self.listPhotos.GetSelection()
        info = photo_id, photo_url, photo_caption, addl_info = self.dictPhoto[selected]    
        dialog = ScrolledMessageDialog (self, info, 'Additional Information', pos=wx.DefaultPosition, size=(550, 400))
        result = dialog.ShowModal()   
        
        if result == wx.ID_OK: 
            dialog.Destroy()    
            
    def OnListPhotosListbox(self, event):
        self.btnInfo.Enable(True)
        self.btnView.Enable(True)
        
    def OnListAlbumsListbox(self, event):
        self.btnInfo.Enable(False)
        self.btnView.Enable(False)
        self.listPhotos.Clear()
        selected = self.listAlbums.GetSelection()
        
        # Get saved Album ID
        album_id = self.dictAlbum[selected]        
        print "Album list clicked: " + album_id
        
        # Load Photo Data    
        photos = self.photoData.load_photos(album_id)
        
        i = 0
        for photo in photos.entry:
            # These may be null
            try:
                camera = ('Camera: %s %s\n' % (photo.exif.make.text, photo.exif.model.text))
            except Exception:
                camera = ''
            
            try:
                fstop = ('FStop: %s\n' % (photo.exif.fstop.text))
            except Exception:
                fstop = ''
                
            try:
                # Need to remove last 3 digits of timestamp for valid epoch time
                epoch = int(photo.timestamp.text[0:-3])
                timestamp = ('Date: %s\n' % (time.ctime(epoch)))
            except Exception:
                timestamp = ''
                
            addl_info = timestamp + camera + fstop
            caption = photo.summary.text
            self.listPhotos.Append('%s' % caption)
            self.dictPhoto[i] = photo.gphoto_id.text, photo.content.src, caption, addl_info
            i += 1        
            
    def OnClose(self, evt):
        self.Exit()
        
    def OnExitApp(self, event):
        self.Exit()
         
if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

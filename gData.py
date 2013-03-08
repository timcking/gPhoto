import gdata.photos.service
import base64
import webbrowser
import time

class gData():
    gd_client = gdata.photos.service.PhotosService()
    
    def __init__(self, passwd):
        # ToDo: Handle login failure
        self.gd_client.email = 'timcking@gmail.com'
        self.gd_client.password = passwd
        self.gd_client.source = 'gPhoto'
        self.gd_client.ProgrammaticLogin()

    def load_albums(self):
        return self.gd_client.GetUserFeed(user='default')

    def load_photos(self, album_id):
        photos = gd_client.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album_id))
        
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
            # TODO: move to gphoto.py !!!
            # self.listPhotos.Append('%s' % caption)
            dictPhoto[i] = photo.gphoto_id.text, photo.content.src, caption, addl_info
            i += 1
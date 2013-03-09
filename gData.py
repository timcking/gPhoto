import gdata.photos.service
import base64
import webbrowser
import sys

class gData():
    gd_client = gdata.photos.service.PhotosService()
    
    def __init__(self, passwd):
        self.gd_client.email = 'timcking@gmail.com'
        self.gd_client.password = passwd
        self.gd_client.source = 'gPhoto'
        try:
            self.gd_client.ProgrammaticLogin()
        except Exception, err:
            # TODO: Show in UI
            sys.stderr.write('ERROR: %s\n' % str(err))            
            
    def load_albums(self):
        return self.gd_client.GetUserFeed(user='default')

    def load_photos(self, album_id):
        return self.gd_client.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album_id))
    

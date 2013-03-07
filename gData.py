import gdata.photos.service
import base64
import webbrowser
import time

class gData():
    gd_client = gdata.photos.service.PhotosService()
    
    def __init__(self, passwd):
        # Format for dictionary: {index: ('album_id')}
        self.dictAlbum = {}
        # Format for photo dict: {index: (photo_id, url, caption, addl_info)}
        self.dictPhoto = {}
        
        self.gd_client.email = 'timcking@gmail.com'
        self.gd_client.password = passwd
        self.gd_client.source = 'gPhoto'
        self.gd_client.ProgrammaticLogin()

        # return self.gd_client

    def load_albums(self):
        return self.gd_client.GetUserFeed(user='default')

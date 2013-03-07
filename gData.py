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

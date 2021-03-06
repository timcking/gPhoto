import gdata.photos.service

class gData():
    gd_client = gdata.photos.service.PhotosService()
    
    def __init__(self, user, passwd):
        self.gd_client.email = user
        self.gd_client.password = passwd
        self.gd_client.source = 'gPhoto'
    
    def login(self):
        try:
            self.gd_client.ProgrammaticLogin()
            return None
        except Exception, err:
            return str(err)
            
    def load_albums(self):
        return self.gd_client.GetUserFeed(user='default')

    def load_photos(self, album_id):
        return self.gd_client.GetFeed('/data/feed/api/user/default/albumid/%s?kind=photo' % (album_id))
    

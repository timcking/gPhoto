import gdata.photos.service
import base64
import webbrowser
import time

class gData():
    gd_client = gdata.photos.service.PhotosService()
    
    def __init__(self):
        # Format for dictionary: {index: ('album_id')}
        self.dictAlbum = {}
        # Format for photo dict: {index: (photo_id, url, caption, addl_info)}
        self.dictPhoto = {}

    def login(self):
        self.gd_client.email = 'timcking@gmail.com'
        # ToDo
        self.gd_client.password = "XXXX"
        self.gd_client.source = 'gPhoto'
        self.gd_client.ProgrammaticLogin()

        return self.gd_client

    def load_albums(self):
        gd_client = self.login()
        albums = gd_client.GetUserFeed(user='default')
        index_count = 0

        for album in albums.entry:
            self.listAlbums.Append('%s' % album.title.text)
            dictAlbum[index_count] = album.gphoto_id.text
            index_count += 1

        print 'title: %s, number of photos: %s, id: %s' % (album.title.text, album.numphotos.text,
               album.gphoto_id.text)
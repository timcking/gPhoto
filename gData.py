import gdata.photos.service
import base64
import webbrowser
import time

class gData():
	def __init__(self):
		# Format for dictionary: {index: ('album_id')}
		self.dictAlbum = {}
		# Format for photo dict: {index: (photo_id, url, caption, addl_info)}
		self.dictPhoto = {}

		gd_client = gdata.photos.service.PhotosService()
	
	def login():
		gd_client.email = 'timcking@gmail.com'
		# ToDo
		gd_client.password = "xxxx"
		gd_client.source = 'gPhoto'
		gd_client.ProgrammaticLogin()
		
		return gd_client

	def load_albums(self):
		gd_client = login()
		albums = gd_client.GetUserFeed(user='default')
		index_count = 0
		
		for album in albums.entry:
			self.listAlbums.Append('%s' % album.title.text)
			dictAlbum[index_count] = album.gphoto_id.text
			index_count += 1
		
		# print 'title: %s, number of photos: %s, id: %s' % (album.title.text, album.numphotos.text,
		#        album.gphoto_id.text)
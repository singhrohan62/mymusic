from django.http import HttpResponse
from .models import Album

def index(request):
	albums = Album.objects.all()
	html = ' '
	for album in albums:
		url = '/music/' + str(album.id) 
		html += '<a href=" '+ url + '">' + album.album_title + '</a><br>'
	return HttpResponse(html)

def details(request, album_id):
	return HttpResponse('<h2>Details for Album id : ' + str(album_id) + '</h2>')
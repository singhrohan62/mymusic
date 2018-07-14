
#from django.http import Http404
#from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView

class IndexView (generic.ListView):
	context_object_name = 'all_albums'
	template_name = 'music/index.html'

	def get_queryset(self):
		return Album.objects.all()


class DetailsView (generic.DetailView):
	model = Album
	template_name = 'music/detail.html'	

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title','genre','album_logo']
	template_name = 'music/album_form.html'
		

'''
def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums' : all_albums}
	return render(request,'music/index.html',context)

def details(request, album_id):
	album = get_object_or_404(Album, pk = album_id)
	return render(request, 'music/detail.html', {'album' : album})

def favourite(request,album_id):
	album = get_object_or_404(Album, pk = album_id)
	try:
		selected_song = album.song_set.get(pk = request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request,'music/detail.html',{'album' : album, 'error_msg' : "You did not select a valid song",})
	else:
		selected_song.isFavourite = True
		selected_song.save()
		return render(request, 'music/detail.html', {'album' : album})		'''


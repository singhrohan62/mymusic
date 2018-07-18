from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
	#music/
	path('', views.IndexView.as_view(), name='index'),

	#music/{album_id}/
	path('<pk>/', views.DetailsView.as_view(), name='details'),

	#music/add
	path('album/add', views.AlbumCreate.as_view(), name = 'album-add'),

	#music/album/{album_id}/
	path('album/<pk>/', views.AlbumUpdate.as_view(), name = 'album-update'),

	#music/<pk>/delete
	path('album/<pk>/delete', views.AlbumDelete.as_view(), name = 'album-delete')	

	#music/{album_id}/favourite/
	#path('<album_id>/favourite', views.favourite, name='favourite'),	---->>NOT USING FAVOURITE FEATURE NOW
]
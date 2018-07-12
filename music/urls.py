from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
	#music/
	path('', views.IndexView.as_view(), name='index'),

	#music/{album_id}/
	path('<pk>/', views.DetailsView.as_view(), name='details'),

	#music/{album_id}/favourite/
	#path('<album_id>/favourite', views.favourite, name='favourite'),	---->>NOT USING FAVOURITE FEATURE NOW
]
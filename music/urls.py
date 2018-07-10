from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
	#music/
	path('', views.index, name='index'),

	#music/{album_id}/
	path('<album_id>/', views.details, name='details'),
]
from django.urls import path
from .views import(
	index, 
	create, 
	read 
	)

app_name = "blogging"
urlpatterns = [
	path('', index.as_view(), name='index'), 
	path('create/', create.as_view(), name='update'), 
	path('<int:id>/', read.as_view(), name= 'read')
]
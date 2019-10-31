from django.urls import path
from search import views as srch

app_name = 'search'

urlpatterns = [
	path('',srch.index,name='index'),
	path('suggestions/',srch.search,name='search_suggestions')
]
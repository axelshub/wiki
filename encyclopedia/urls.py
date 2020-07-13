from django.urls import path
from . import views # URLs can now be linked to views

# urlpatterns is a list of all the URLs supported by this application
urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/<str:title>', views.entry, name='entry'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit')

]

 
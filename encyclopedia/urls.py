from django.urls import path

from . import views # URLs can now be linked to views

# urlpatterns is a list of all the URLs supported by this application
urlpatterns = [
    path("", views.index, name="index")
    path("<str: TITLE>", views.entry, name="entry")
]

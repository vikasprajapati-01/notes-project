from django.urls import path

from .import views

urlpatterns = [
    path("notes/", views.notes, name="notes"),
    path("notes/<slug:slug>", views.note_detail, name="note-detail"),
]

# To access notes data
# To get all the notes : HOSTNUMBER/notes
# To get a particular note : HOSTNUMBER/notes/note-slug
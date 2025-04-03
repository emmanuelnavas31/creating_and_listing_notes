from django.urls import path
from core.views import index, create_note, NoteList

urlpatterns = [
    path("", index, name="index"),
    path("crear/", create_note, name="create_note"),
    path("api/notas/", NoteList.as_view(), name="api_note"),
]

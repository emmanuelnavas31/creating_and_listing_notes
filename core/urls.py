from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('crear/', create_note, name='create_note'),
    path('api/notas/', NoteList.as_view(), name='api_note'),
]

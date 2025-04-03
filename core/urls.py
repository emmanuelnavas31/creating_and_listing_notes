from django.urls import path
from core.views import index, create_note, NoteList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("crear/", create_note, name="create_note"),
    path("api/notas/", NoteList.as_view(), name="api_note"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response

from core.forms import NotasForms
from core.models import Notas
from core.serializers import NotasSerializer

async def index(request):
    formulario = NotasForms()
    return render(request, 'notas/index.html', {'form': formulario})


def create_note(request):
    if request.method == 'POST':
        form = NotasForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡La nota se creó exitosamente!')
    return redirect('index')


class NoteList(APIView):
    def get(self, request):
        notas = Notas.objects.all().order_by('-created_at')
        serializador = NotasSerializer(notas, many=True)
        return Response(serializador.data)

from django import forms

from core.models import Notas


class NotasForms(forms.ModelForm):
    titulo = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "title",
                "placeholder": "Nombre de mi tarea",
            }
        )
    )
    categoria = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "categoria",
                "placeholder": "Categorizar mi tarea",
            }
        )
    )
    contenido = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "contenido",
                "placeholder": "Aquí escribo lo que debo hacer para culminar mi tarea.",
                "rows": "3"
            }
        )
    )
    class Meta:
        model = Notas
        fields = ['titulo', 'contenido', 'categoria']

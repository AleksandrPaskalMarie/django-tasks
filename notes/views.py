from django.shortcuts import render

from django.http import HttpResponse
from .models import Note
from django.shortcuts import get_object_or_404

# Список всех заметок
def notes_list(request):
    notes = Note.objects.all()
    html = "<h1>Список заметок</h1>"
    for note in notes:
        html += f"<p><a href='/notes/{note.id}'>{note.title}</a></p>"
    return HttpResponse(html)

# Детальная страница одной заметки
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return HttpResponse(f"<h1>{note.title}</h1><p>{note.body}</p>")

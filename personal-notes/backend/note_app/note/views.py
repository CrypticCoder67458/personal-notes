from django.shortcuts import render
from django.http import JsonResponse
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
def get_notes(request):
    notes=Note.objects.all()
    serialiazer=NoteSerializer(notes,many=True)
    return JsonResponse(serialiazer.data,safe=False)
from django.shortcuts import render
from .models import Deck


def home(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/index.html', {'decks': decks})

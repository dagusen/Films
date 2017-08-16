from django.shortcuts import render
from django.utils import timezone
from .models import Film, Actor, Genre
from django.views.generic import View
# Create your views here.

class FilmList(View):
	def get(self, request):
		film = Film.objects.all()
		actor = Actor.objects.all()
		genre = Genre.objects.all()
		context = {
		'film': film,
		'actor': actor,
		'genre': genre,
		}
		return render(request, "Film.html", context)

class ActorList(View):
	def get(self, request):
		actor = Actor.objects.all()
		context = {
		'actor': actor,
		}
		return render(request, "Actor.html", context)

class GenreList(View):
	def get(self, request):
		genre = Genre.objects.all()
		context = {
		'genre': genre,
		}
		return render(request, "Genre.html", context)
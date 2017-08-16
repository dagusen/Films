from django.shortcuts import render
from django.utils import timezone
from .models import Film, Actor, Genre
from django.views.generic import View, DetailView, ListView
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

# Film Detail View

class FilmDetailView(DetailView):

    model = Film
    template_name = "film_detail.html"

    def get_context_data(self, **kwargs):
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# Film List View
# class FilmListView(ListView):

    # model = Film
    # template_name = "film_List.html"

    # def get_context_data(self, **kwargs):
        # context = super(FilmListView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        # return context
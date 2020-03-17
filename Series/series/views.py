from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from .models import Series, Seasons


# Add more content
# Blog add

class SeriesListViews(ListView):
    model = Series
    template_name = "series/series.html"
    context_object_name = "series"
    paginate_by = 4


def seasons_func(request, pk):
    s = Series.objects.get(pk=pk)
    seasons = s.seasons_set.all()

    return render(request, 'series/season.html', {'seasons': seasons})


def episodes_func(request, pk):
    s = Seasons.objects.get(pk=pk)
    episodes = s.episodes_set.all()
    return render(request, 'series/episodes.html', {'episodes': episodes})


class SeriesForm(CreateView):
    success_url = '/'
    model = Series
    fields = ['name', 'content', 'image']
    template_name = 'series/form.html'


def about(request):
    return render(request, 'series/about.html')

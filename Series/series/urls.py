from django.urls import path
from .views import SeriesListViews, seasons_func, episodes_func, SeriesForm
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('post/', SeriesForm.as_view(), name='series-form'),
    path('', SeriesListViews.as_view(), name='series'),
    path('seasons/<int:pk>/', seasons_func, name='seasons'),
    path('episodes/<int:pk>/', episodes_func, name='episodes')
]

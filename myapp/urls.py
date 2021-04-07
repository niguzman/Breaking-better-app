from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('character/<str:name>', views.character, name='character'),
    path('breakingBad/<int:season>/', views.breakingBad, name='breakingBad'),
    path('betterCallSaul/<int:season>/', views.betterCallSaul, name='betterCallSaul'),
    path('episode/<int:episode_id>/', views.detailsEpisode, name='episode'),
    path('search/', views.search, name='search'),
]

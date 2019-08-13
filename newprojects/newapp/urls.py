from django.urls import path

from newapp.views import SearchResultsView
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    #path('search/', views.article_overview, name='search_resut'),
    # path('github/', views.github, name='github'),
    # path('github/client/', views.github_client, name='github_client'),
    # path('oxford/', views.oxford, name='oxford'),
]
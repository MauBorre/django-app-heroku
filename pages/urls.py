from django.urls import path

from .views import HomePageView
from articles.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
]

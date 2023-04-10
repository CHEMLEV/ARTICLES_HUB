from django.urls import path
from . import views
from .views import ArticlesListView, ArticleDetailsView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('home.html/', views.HomePageView, name = "home"),
    path("articles/", ArticlesListView.as_view(), name = "article_list"),
    path("article/<int:pk>/", ArticleDetailsView.as_view(), name = "article_detail"),
    path("article/new/", ArticleCreateView.as_view(), name = "article_new"),
    path("article/<int:pk>/edit", ArticleUpdateView.as_view(), name = "article_edit" ),
    path("article/<int:pk>/delete", ArticleDeleteView.as_view(), name = "article_delete" ),
    
]
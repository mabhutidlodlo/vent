from django.contrib import admin
from django.urls import path
from authentication import urls
from django.conf.urls import include, url
from . import views
urlpatterns = [
    path('article/', views.MyArticle.as_view(), name = 'my-article'),
    path('article/<int:pk>/', views.MyArticle.as_view(), name = 'my-article'),
    path('articles/', views.getAllArticles.as_view(), name = 'all-articles'),
    path('myComment/' ,views.MyComment.as_view(), name = 'my-comment'),
    path('myComment/<int:pk>/', views.MyComment.as_view(), name = 'my-comment'),
    path('allComments/<int:article>/', views.AllComments.as_view(), name = 'all-comments'),




]

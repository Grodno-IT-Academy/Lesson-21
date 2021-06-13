
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name ='home'),
    path('article/<int:article_id>/', article_page, name="article"),
]
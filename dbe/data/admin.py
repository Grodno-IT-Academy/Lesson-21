from django.contrib import admin
from .models import Article, Request

# Register your models here.
admin.site.register(Article)
admin.site.register(Request)
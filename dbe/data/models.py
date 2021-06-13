from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=244, default="Article Name")
    content = models.TextField(default="Content")
    count_views = models.IntegerField(default=0)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

class Request(models.Model):
    url = models.CharField(null=True, max_length=244)
    count = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.url + " count:" + str(self.count)
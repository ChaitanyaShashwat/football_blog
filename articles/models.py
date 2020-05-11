from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE_CHOICES = (
    ('ANALYSIS', 'Analysis'),
    ('NEWS', 'News'),
    ('TRANSFERS', 'Transfers'),
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100,default='No Description Available')
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True) # automatically put datestamp
    type = models.CharField(max_length=10,choices=TYPE_CHOICES)
    thumb = models.ImageField(upload_to='thumbnail_pics',blank=True)
    author = models.ForeignKey(User,on_delete = models.CASCADE,default=None)

def __str__(self):
    return self.title

from django.db import models

# Create your models here.
class Blog(models.Model): 
    title = models.CharField(max_length=255)
    text = models.TextField(null=False)
    image_url = models.URLField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
class History(models.Model):
    blog_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
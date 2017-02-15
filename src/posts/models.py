from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # auto_now_add True will updated when the variable is save initialy, just one time
    # auto_now will be saved any time is saved

    # If it was python 2 should be __unicode__
    def __str__(self):
        return self.title
        

from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255, default='Untiltled')
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    def __str__(self):
        return self.title

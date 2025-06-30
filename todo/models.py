from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
class Project(models.Model):
    tittle = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    technology = models.CharField(max_length=200)
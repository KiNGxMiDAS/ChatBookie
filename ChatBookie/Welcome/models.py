from django.db import models

# Create your models here.
# This model should 1st portray a representation of the 'HomePage' UI

class Match(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    # Define other fields as needed

    def __str__(self):
        return self.title


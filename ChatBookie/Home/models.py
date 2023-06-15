from django.db import models

# Create your models here.
'''
A Django model is a table in your database.

Django Models
Up until now in this tutorial, output has been static data from Python or HTML templates.

Now we will see how Django allows us to work with data, without having to change or upload files in the prosess.

In Django, data is created in objects, called Models, and is actually tables in a database.
'''
class Home(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

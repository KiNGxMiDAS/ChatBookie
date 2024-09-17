from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# A Django view is simply a Python function that takes http requests and returns http responses, like HTML documents e.g.


# Here, we will send a response back to the browser
# But, how do we execute the view? We must call the view via a URL
def Home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

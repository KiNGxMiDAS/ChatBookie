from  django.urls import path

from . import views

# Create your URLS here

#
# Within views.py, we sent a response back to the browser
# And we will execute the view by calling it here
#

urlpatterns = [
    path('Home/', views.Home, name='Home'),
]

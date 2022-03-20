from django.urls import path
from . import views
#from . import home


urlpatterns = [
    path('', views.home, name="home"),
    #path('', include('home.urls')),
]
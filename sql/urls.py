from django.urls import path
from . import views

app_name = 'sql'
urlpatterns = [
    
    # path('',views.home, name ='index')
    path('',views.home, name ='query')

    
    ]
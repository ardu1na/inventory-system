from django.urls import path
from django.contrib.auth.decorators import login_required
from inventory import views
urlpatterns = [
    
    
    path('', login_required(views.index), name='index')
]
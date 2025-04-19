from django.urls import path
from .views import homepage

app_name = 'items'
urlpatterns = [
    path('', homepage, name='homepage'),
]
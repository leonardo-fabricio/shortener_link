from django.urls import path
from .viewsets import *

urlpatterns = [
    path('encurtar-link/', LinkCreateViewSet.as_view()),
]
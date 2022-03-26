from django.urls import path
from .viewsets import *

urlpatterns = [
    path('encutar-link/', LinkCreateViewSet.as_view()),
]
from django.contrib import admin
from django.urls import include, path
from shortener.api.viewsets import LinkListViewSet
from shortener.views import return_for_domain

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shortener.api.urls')),
    path('<str:hash>/', LinkListViewSet.as_view()),
    path('',return_for_domain),
]

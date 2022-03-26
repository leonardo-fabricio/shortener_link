from django.conf import settings
from django.shortcuts import redirect
from rest_framework import generics,status
from .serializers import LinkSerializer
from .utils import *
from rest_framework.views import Response

class LinkCreateViewSet(generics.CreateAPIView):
    serializer_class = LinkSerializer

    def post(self, request, *args, **kwargs):
        link = Link.objects.filter(url = request.data['url'])
        if link:
            request.data['hash'] = link[0].hash
            request.data['short_link'] = link[0].short_link
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response({"detail":"Ocorreu um erro."}, status=status.HTTP_400_BAD_REQUEST)

        request.data['hash'] = unique_hash_generator()
        request.data['short_link'] = settings.SHORT_REDIRECT + "/" + request.data['hash']
        return self.create(request, *args, **kwargs)

class LinkListViewSet(generics.ListAPIView):
    serializer_class = LinkSerializer

    def get(self, request, *args, **kwargs):
        link = Link.objects.filter(hash = self.kwargs['hash'])
        if not link:
            return redirect(settings.RETURN_URL)

        return redirect(link[0].url)
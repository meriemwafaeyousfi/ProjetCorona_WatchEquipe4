from rest_framework import viewsets
from .serializers import *
from .models import *


class pubFacebookView(viewsets.ModelViewSet):
    serializer_class = pubFacebookSerializer
    queryset = pubFacebook.objects.all()


class pubYoutubeView(viewsets.ModelViewSet):
    serializer_class = pubYoutubeSerializer
    queryset = pubYoutube.objects.all()


class pubSiteWebView(viewsets.ModelViewSet):
    serializer_class = pubSiteWebSerializer
    queryset = pubSiteWeb.objects.all()
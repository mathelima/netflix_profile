from django.shortcuts import render

from netflix_profile.profiles.models import Profile
from rest_framework import viewsets
from rest_framework import permissions
from netflix_profile.profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = [permissions.IsAuthenticated]

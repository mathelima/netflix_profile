from netflix_profile.profiles.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    birthdate = models.DateField(null=False)
    icon_url = models.CharField(max_length=255)
    id_user = models.IntegerField(null=False)

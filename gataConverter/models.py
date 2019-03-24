from django.db import models


class Downloads(models.Model):
    total = models.IntegerField(default=0)
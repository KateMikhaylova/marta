from django.db import models


class Like(models.Model):

    count = models.IntegerField(default=0)

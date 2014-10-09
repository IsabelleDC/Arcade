from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='games')

    def __unicode__(self):
        return u"{}".format(self.name)

class Score(models.Model):
    point = models.IntegerField(max_length=30)
    user = models.ForeignKey(User, related_name='scores')

    def __unicode__(self):
        return u"{}".format(self.user)




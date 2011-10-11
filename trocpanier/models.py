import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Panier(models.Model):
    TypePanier = models.CharField(max_length=100)
    def __unicode__(self):
        return self.TypePanier

class Profil(models.Model):
    panier = models.ForeignKey(Panier)
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.panier.TypePanier

class DistriLieu(models.Model):
    lieu = models.CharField(max_length=255)
    def __unicode__(self):
        return self.lieu

class Distribution(models.Model):
    date = models.DateField()
    lieu = models.ForeignKey(DistriLieu)
    def __unicode__(self):
        return "%s - %s" % (self.date,self.lieu)

class Echange(models.Model):
    adherent = models.ForeignKey(User, related_name="adherent")
    intermittent = models.ForeignKey(User, related_name="intermittent", null=True, blank=True)
    distribution = models.ForeignKey(Distribution)
    def __unicode__(self):
        return "[%s][%s][%s]" % (self.distribution,self.adherent,self.intermittent)
    def echange_courant(self):
        return self.distribution.date() >= datetime.date.today()



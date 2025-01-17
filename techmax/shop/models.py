from django.db import models
from django.contrib.auth.models import User

class Kunde(models.Model):
    benutzer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    # Standardtext, der im Browser und im Admin Panel ausgegeben wird
    def __str__(self):
        return self.name

class Artikel(models.Model):
    name = models.CharField(max_length=200, null=True)
    beschreibung = models.TextField(null=True, blank=True)
    preis = models.IntegerField(default=0, null=True, blank=True)
    bild = models.ImageField(upload_to='produkte/', null=True, blank=True)

     # Standardtext, der im Browser und im Admin Panel ausgegeben wird
    def __str__(self):
        return self.name

class Bestellung(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.SET_NULL, null=True, blank=True)
    bestelldatum = models.DateTimeField(auto_now_add=True)
    erledigt = models.BooleanField(default=False, null=True, blank=True)
    auftrags_id = models.CharField(max_length=200, null=200)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_gesamtpreis(self):
        bestellteartiktels = self.bestellteartikel_set.all()
        gesamtpreis = sum(artikel.get_summe for artikel in bestellteartiktels)
        return gesamtpreis
    
    @property
    def get_gesamtmenge(self):
        bestellteartiktels = self.bestellteartikel_set.all()
        gesamtmenge = sum(artikel.menge for artikel in bestellteartiktels)
        return gesamtmenge
    
class BestellteArtikel(models.Model):
    artikel = models.ForeignKey(Artikel, on_delete=models.SET_NULL, null=True, blank=True)
    bestellung = models.ForeignKey(Bestellung, on_delete=models.SET_NULL, null=True, blank=True)
    menge = models.IntegerField(default=0, null=True, blank=True)
    datum = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.artikel.name
    
    @property
    def get_summe(self):
        summe = self.artikel.preis * self.menge
        return summe
    
class Adresse(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.SET_NULL, null=True, blank=True)
    bestellung = models.ForeignKey(Bestellung, on_delete=models.SET_NULL, null=True, blank=True)
    adresse = models.CharField(max_length=200, null=True)
    plz = models.CharField(max_length=200, null=True)
    stadt = models.CharField(max_length=200, null=True)
    land = models.CharField(max_length=200, null=True)
    datum = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.adresse
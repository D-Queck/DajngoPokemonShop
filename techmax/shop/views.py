from django.shortcuts import render
from . models import *


# Technischer Ablauf: URL (wird aufgerufen) ---> View (wird aufgerufen) ---> template (HTML, wird) 
# Datenbankabfragen werden in den Views verarbeitet

def shop(request):
    # hier werden die in den Models definierten und im Admincenter angelegten Artikel, an die views übergeben
    artikels = Artikel.objects.all
    context = {'artikels':artikels}
    return render(request, 'shop/shop.html', context)

def warenkorb(request):
    if request.user.is_authenticated:
        kunde = request.user.kunde
        bestellung, created = Bestellung.objects.get_or_create(kunde=kunde, erledigt=False)
        artikels = bestellung.bestellteartikel_set.all()
    else:
        artikels = []
        bestellung = []
    
    context = {'artikels':artikels, "bestellung":bestellung}
    return render(request, 'shop/warenkorb.html', context)

def kasse(request):
    if request.user.is_authenticated:
        kunde = request.user.kunde
        bestellung, created = Bestellung.objects.get_or_create(kunde=kunde, erledigt=False)
        artikels = bestellung.bestellteartikel_set.all()
    else:
        artikels = []
        bestellung = []
    
    context = {'artikels':artikels, "bestellung":bestellung}
    return render(request, 'shop/kasse.html', context)


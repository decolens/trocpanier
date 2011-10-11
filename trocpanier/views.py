import datetime

from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required

from django.core.urlresolvers import reverse

from trocpanier.models import Profil, Distribution, Echange

# Create your views here.

def index(request):
    paniers = Echange.objects.filter(distribution__date__gte=datetime.date.today())
#    panier = Echange.objects.all()
    return render(request,'index.html', {'paniers': paniers})

@login_required
def depot(request):
    return render(request,'depot.html')

@login_required
def reserver(request):
    return render(request,'reserver.html')

def lister(request):
    return render(request, 'liste.html')

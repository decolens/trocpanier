from django.form import ModelForm
from trocpanier.models import Profil

class ProfilForm(ModelForm):
    class Meta:
        model = Profil

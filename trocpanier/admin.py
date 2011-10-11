from django.contrib.admin.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

from trocpanier.models import *

class ProfilInLine(admin.TabularInline):
    model = Profil
    radio_fields = {"panier": admin.HORIZONTAL }

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None,              { 'fields' : ('username','password', 'is_active','first_name', 'last_name', 'email', 'is_staff')}),
#        (_('Personal info'), {'fields' : ('first_name', 'last_name', 'email', 'is_staff')}),
#        (_('Permissions'), {'fields': ('is_active',)}),
        (_('Groups'), {'fields' : ('groups',)}),
        )
    inlines = [ProfilInLine]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        }
#    filter_vertical=('groups',)
    list_display = ('username', 'is_active', 'first_name', 'last_name', 'email', 'profil')
    list_editable= ('is_active', 'first_name', 'last_name', 'email')
    list_filter= ('is_active', 'profil' )

class MyUser(User):
    class Meta:
        proxy = True
        permissions = (
            ("can_view", "Can see available tasks"),
            ("can_change_status", "Can change the status of tasks"),
            ("can_close", "Can remove a task by setting its status as closed"),
            )



admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)

admin.site.register(DistriLieu)

admin.site.register(Distribution)
admin.site.register(Echange)
admin.site.register(Panier)

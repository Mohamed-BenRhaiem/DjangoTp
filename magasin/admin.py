from django.contrib import admin

from .models import Categorie, Commande, Fournisseur, Produit, ProduitNC
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)
# Register your models here.

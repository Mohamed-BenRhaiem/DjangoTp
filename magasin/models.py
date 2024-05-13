from datetime import date
from django.db import models

# Create your models here.

class Categorie(models.Model):
   TYPE_CHOICES=[('Alimenatire','Alimenatire'),('Mb','Meuble'),('Sn','Sanitaire'),('Vs','Vaisselle'),('Vt','Vetement'),('Jx','Jouets'),('Lg','Ligne de Maison'),('Bj','Bijoux'),('Dc','Décor')]
   name=models.CharField(max_length=50,default='Alimentaire',choices=TYPE_CHOICES)

   def __str__(self):
      return f"{self.name}"

class Fournisseur(models.Model):
   nom=models.CharField(max_length=100)
   adresse=models.TextField()
   email=models.EmailField()
   telephone=models.CharField(max_length=8)

   def __str__(self) -> str:
      return f"{self.nom}"



class Produit(models.Model):
     libellé=models.CharField(max_length=100)
     desciption=models.TextField(default='Non définie')
     prix=models.DecimalField(max_digits=10,decimal_places=3)
     TYPE_CHOICES=[('em','Emballé'),('fr','Frais'),('cs','Conserve')]
     type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
     img=models.ImageField(blank=True)
     categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
     fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)
     def __str__(self):
      return f"{self.libellé} - {self.desciption} - {self.prix} - {self.type}"

class Commande(models.Model):
   dateCde=models.DateField(null=True,default=date.today)
   totalCde=models.DecimalField(max_digits=10,decimal_places=3)
   produits=models.ManyToManyField('Produit')
   def __str__(self):
      s=self.produits.get()
      return f"{self.dateCde} - {self.totalCde} - {s}"
   

class ProduitNC(Produit):
   duree_garantie=models.CharField(max_length=100)
   def __str__(self):
      return f"{self.duree_garantie}"
   

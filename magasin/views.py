from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fournisseur, Produit,Commande,Categorie
from .forms import FournisseurForm, ProduitForm, CommandeForm
from magasin.serializers import CategorySerializer,ProduitSerializer
from django.shortcuts import redirect ,render
from .forms import ProduitForm, FournisseurForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

def index(request):   
    return redirect('allProducts')


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('categorie_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

class CategoryAPIView(APIView):
 def get(self, *args, **kwargs):
    categories = Categorie.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
 
class ProduitAPIView(APIView):
 def get(self, *args, **kwargs):
    categories = Produit.objects.all()
    serializer = ProduitSerializer(categories, many=True)
    return Response(serializer.data)




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Hello {username}, Your account has been created successfully!')
            return redirect('index') 
        else:
            # Render the registration form again with errors
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


@login_required
def addProvider(request):
    if request.method == "POST" :
        form = FournisseurForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('Four')
    else :
        form = FournisseurForm() 
    return render(request,'magasin/ajoutFournisseur.html',{'form':form})


def allProducts(request):
    list=Produit.objects.all() 
    return render(request,'magasin/vitrine.html',{'list':list})

@login_required
def Fournisseurs(request) :
    liste=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'liste':liste})

@login_required
def addProduct(request) :
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('allProducts')
    else :
        form = ProduitForm() #créer formulaire vide 
    return render(request,'magasin/majProduits.html',{'form':form})

@login_required
def com(request):
    commandes= Commande.objects.all()
    return render(request,'magasin/commande.html',{'commandes':commandes})

@login_required
def addCommande(request):
    if request.method == "POST":
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('commandes')
    else:
        form = CommandeForm()
        return render(request,'magasin/ajoutCommande.html',{'form':form})

@login_required
def mesProduits(request):
    if request.method=="GET":
        libelle_param = request.GET.get('libellé')
        if libelle_param:
            list = Produit.objects.filter(libellé =libelle_param.capitalize())
            return render(request, 'magasin/mesProduits.html', {'list': list})
        
    list = Produit.objects.all()
    return render(request,'magasin/mesProduits.html',{'list':list})

@login_required
def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        Produit.objects.filter(id=product_id).delete()
        return redirect('mesProduits')
    return redirect('mesProduits')
@login_required
def modify_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        modified_name = request.POST.get('modified_name')
        modified_description = request.POST.get('modified_description')
        modified_price = request.POST.get('modified_price')
        
        # Fetch the product object from the database
        product = Produit.objects.get(id=product_id)
        
        # Update the product details
        product.libellé = modified_name
        product.description = modified_description
        product.prix = modified_price
        # You can update other fields similarly
        
        # Save the updated product
        product.save()
        
        # Redirect to a success page or any other appropriate URL
        return redirect('mesProduits')
    

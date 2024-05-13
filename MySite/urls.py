from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from magasin.views import ProductViewset

from . import views
router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin',include('magasin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index,name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

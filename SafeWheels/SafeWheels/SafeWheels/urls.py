"""SafeWheels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from safewheel.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('rampa/', rampa, name='rampa'),
    path('barras/', barras, name='barras'),
    path('banheiros/', banheiros, name='banheiros'),
    path('arquitetonica/', arquitetonica, name='arquitetonica'),
    path('transporte/', transporte, name='transporte'),
    path('digital/', digital, name='digital'),
    path('registrar-estabelecimento/', registrarEstabelecimento, name='registrarEstabelecimento'),
    path('ver-estabelecimento/<id>', verEstabelecimento, name='verEstabelecimento'),
    path('update-estabelecimento/<id>', updateEstabelecimento, name='updateEstabelecimento'),
    path('delete/<id>', deletarEstabelecimento, name='deletarEstabelecimento'),
    path('estabelecimentos-cadastrados/', estabelecimentosCadastrados, name='estabelecimentosCadastrados'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forgot/', forgot, name='forgot'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
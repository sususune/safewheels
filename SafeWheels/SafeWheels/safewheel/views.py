from asyncio.windows_events import NULL
from audioop import reverse
from email.policy import default
from http.client import HTTPResponse
from tkinter import Entry
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authlogin
from django.contrib import messages
from .models import Estabelecimentos

def index(request):
    return render(request, 'safewheel/index.html')

def rampa(request):
    estabelecimentos = Estabelecimentos.objects.filter(rampa_para_acesso=True)
    return render(request, 'safewheel/rampa.html', {"estabelecimentos": estabelecimentos})

def barras(request):
    estabelecimentos = Estabelecimentos.objects.filter(barras_de_apoio=True)
    return render(request, 'safewheel/barras.html', {"estabelecimentos": estabelecimentos})

def banheiros(request):
    estabelecimentos = Estabelecimentos.objects.filter(banheiro_adapt=True)
    return render(request, 'safewheel/banheiros.html', {"estabelecimentos": estabelecimentos})

def arquitetonica(request):
    estabelecimentos = Estabelecimentos.objects.filter(acess_arquit=True)
    return render(request, 'safewheel/arquitetonica.html', {"estabelecimentos": estabelecimentos})

def transporte(request):
    estabelecimentos = Estabelecimentos.objects.filter(acess_transporte=True)
    return render(request, 'safewheel/transporte.html', {"estabelecimentos": estabelecimentos})

def digital(request):
    estabelecimentos = Estabelecimentos.objects.filter(acess_digital=True)
    return render(request, 'safewheel/digital.html', {"estabelecimentos": estabelecimentos})

def estabelecimentosCadastrados(request):
    estabelecimentos = Estabelecimentos.objects.all
    return render(request, 'safewheel/estabelecimentos-cadastrados.html', {"estabelecimentos": estabelecimentos})

def registrarEstabelecimento(request, id=NULL):
    if request.method == "GET":
        return render(request, 'safewheel/registrar-estabelecimento.html')
    else:
        nomeE = request.POST.get('nomeE')
        local = request.POST.get('local')
        desc = request.POST.get('desc')
        horario = request.POST.get('horario')
        imagens = request.FILES.get('imagens')
        rampa_para_acesso = request.POST.get('check1')
        if(rampa_para_acesso == 'on'): rampa_para_acesso = True
        else: rampa_para_acesso = False
        barras_de_apoio = request.POST.get('check2')
        if(barras_de_apoio == 'on'): barras_de_apoio = True
        else: barras_de_apoio = False
        banheiro_adapt = request.POST.get('check3')
        if(banheiro_adapt == 'on'): banheiro_adapt = True
        else: banheiro_adapt = False
        acess_transporte = request.POST.get('check4')
        if(acess_transporte == 'on'): acess_transporte = True
        else: acess_transporte = False
        acess_arquit = request.POST.get('check5')
        if(acess_arquit == 'on'): acess_arquit = True
        else: acess_arquit = False
        acess_comunic = request.POST.get('check6')
        if(acess_comunic == 'on'): acess_comunic = True
        else: acess_comunic == False
        acess_digital = request.POST.get('check7')
        if(acess_digital == 'on'): acess_digital = True
        else: acess_digital = False
        acess_instrument = request.POST.get('check8')
        if(acess_instrument == 'on'): acess_instrument = True
        else: acess_instrument = False
        acess_program = request.POST.get('check9')
        if(acess_program == 'on'): acess_program = True
        else: acess_program = False
        acess_metod = request.POST.get('check10')
        if(acess_metod == 'on'): acess_metod = True
        else: acess_metod = False

        Estabelecimentos.objects.create(nome=request.user, nomeE=nomeE, local=local, desc=desc, horario=horario, imagens=imagens, rampa_para_acesso=rampa_para_acesso,
        barras_de_apoio=barras_de_apoio, banheiro_adapt=banheiro_adapt, acess_transporte=acess_transporte, acess_arquit=acess_arquit, acess_comunic=acess_comunic,
        acess_digital=acess_digital, acess_instrument=acess_instrument, acess_program=acess_program, acess_metod=acess_metod)
        estabelecimentos = Estabelecimentos.objects.all()
        return redirect('estabelecimentosCadastrados')

def updateEstabelecimento(request, id):
    estabelecimentos = get_object_or_404(Estabelecimentos, id=id)

    if request.method == "GET":
        return render(request, 'safewheel/update-estabelecimento.html', {"estabelecimentos": estabelecimentos})
    else:
        nomeE =  request.POST.get('nomeE')
        local = request.POST.get('local')
        desc = request.POST.get('desc')
        horario = request.POST.get('horario')
        imagens = request.FILES.get('imagens')
        rampa_para_acesso = request.POST.get('check1')
        if(rampa_para_acesso == 'on'): rampa_para_acesso = True
        else: rampa_para_acesso = False
        barras_de_apoio = request.POST.get('check2')
        if(barras_de_apoio == 'on'): barras_de_apoio = True
        else: barras_de_apoio = False
        banheiro_adapt = request.POST.get('check3')
        if(banheiro_adapt == 'on'): banheiro_adapt = True
        else: banheiro_adapt = False
        acess_transporte = request.POST.get('check4')
        if(acess_transporte == 'on'): acess_transporte = True
        else: acess_transporte = False
        acess_arquit = request.POST.get('check5')
        if(acess_arquit == 'on'): acess_arquit = True
        else: acess_arquit = False
        acess_comunic = request.POST.get('check6')
        if(acess_comunic == 'on'): acess_comunic = True
        else: acess_comunic == False
        acess_digital = request.POST.get('check7')
        if(acess_digital == 'on'): acess_digital = True
        else: acess_digital = False
        acess_instrument = request.POST.get('check8')
        if(acess_instrument == 'on'): acess_instrument = True
        else: acess_instrument = False
        acess_program = request.POST.get('check9')
        if(acess_program == 'on'): acess_program = True
        else: acess_program = False
        acess_metod = request.POST.get('check10')
        if(acess_metod == 'on'): acess_metod = True
        else: acess_metod = False

        estabelecimentos.nomeE = nomeE
        estabelecimentos.local = local
        estabelecimentos.desc = desc
        estabelecimentos.horario = horario
        estabelecimentos.imagens = imagens
        estabelecimentos.rampa_para_acesso = rampa_para_acesso
        estabelecimentos.barras_de_apoio = barras_de_apoio
        estabelecimentos.banheiro_adapt = banheiro_adapt
        estabelecimentos.acess_transporte = acess_transporte
        estabelecimentos.acess_arquit = acess_arquit
        estabelecimentos.acess_comunic = acess_comunic
        estabelecimentos.acess_digital = acess_digital
        estabelecimentos.acess_instrument = acess_instrument
        estabelecimentos.acess_program = acess_program
        estabelecimentos.acess_metod = acess_metod

        estabelecimentos.save()

        return redirect('estabelecimentosCadastrados')


def verEstabelecimento(request, id):
    estabelecimentos = get_object_or_404(Estabelecimentos, id=id)
    return render(request, 'safewheel/ver-estabelecimento.html', {"estabelecimentos": estabelecimentos})

def deletarEstabelecimento(request, id):
    estabelecimentos = get_object_or_404(Estabelecimentos, id=id)
    estabelecimentos.delete()

    return redirect('estabelecimentosCadastrados')

def login(request):
    if request.method == "GET":
        return render(request, 'safewheel/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            authlogin(request, user)

            return redirect('index')
        else:
            return HttpResponse('Usuario não Encontrado')

def register(request):
    if request.method == "GET":
        return render(request, 'safewheel/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password0 = request.POST.get('password0')
        password1 = request.POST.get('password1')

        user = User.objects.filter(username=username).first()

        if password0 != password1:
            return HttpResponse('Senhas não estão Iguais')
        if user:
            return HttpResponse('Este Usuario já existe')
        else:
            user = User.objects.create_user(username=username, email=email, password=password0)
            user.save()
            messages.success(request, f"Sua conta foi criada com sucesso, {username}")

            return redirect('login')

def forgot(request):
    if request.method == "GET":
        return render(request, 'safewheel/forgot.html')
    else:
            email = request.POST['forgotemail']
    return HttpResponse('Email de confirmação foi enviado com sucesso para '+ str(email))
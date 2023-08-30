from django.shortcuts import render
import math

# Create your views here.

def index(request):
    context = {
        'titulo': "Operaciones matemáticas",
    }
    return render(request, 'matematicas/formulario1.html', context)


def enviar(request):
    oper = request.POST['operacion']
    context = {
        'titulo': "Resultado",
        'num1': request.POST['num1'],
        'num2': request.POST['num2'],
        'operacion': request.POST['operacion'],
    }
    if oper == 'suma':
        context['resultado'] = int(request.POST['num1']) + int(request.POST['num2'])
    elif oper == 'resta':
        context['resultado'] = int(request.POST['num1']) - int(request.POST['num2'])
    elif oper == 'multiplicacion':
        context['resultado'] = int(request.POST['num1']) * int(request.POST['num2'])

    return render(request, 'matematicas/respuesta1.html', context)

def index2(request):
    context = {
        'titulo': "CALCULO DE UN VOLUMEN DE UN CILINDRO",
    }
    return render(request, 'matematicas/formulario2.html', context)


def enviar2(request):
    context = {
        'diametro': request.POST['diametro'],
        'altura': request.POST['altura'],
        'resultado': float(request.POST['diametro'])**2*math.pi*float(request.POST['altura'])/4
    }

    return render(request, 'matematicas/respuesta2.html', context)

from django.shortcuts import render
from .forms import CalculoABVForm
from django.views.generic import FormView

def listaString(s):
    # string vazia
    str1 = ""
    for indice in s:
        str1 += indice
    return str1

# Create your views here.
def calculoabv(request):
    abv = 0.0
    if str(request.method) == 'GET':
        form = CalculoABVForm(request.GET or None)
        if form.is_valid():
            og = form.cleaned_data['og']
            fg = form.cleaned_data['fg']
            if form.data['og'].count('.') == 0: #se nao houver ponto no OG
                #COLOCANDO . APOS O PRIMEIRO NUMERO CASO NAO TENHA.
                listaOG=[]
                listaOG[:0] = str(og)
                #lista[]
                print(listaOG[-2])
                listaOG.pop(-2)
                listaOG.insert(1,'.')
                del listaOG[-1]
                og = float((listaString(listaOG)))
            if form.data['fg'].count('.') == 0:
                # ------------------------------------- FG ------- #
                listaFG = []
                listaFG[:0] = str(fg)
                # lista[]
                print(listaFG[-2])
                listaFG.pop(-2)
                listaFG.insert(1, '.')
                del listaFG[-1]
                fg = float((listaString(listaFG)))
            # CALCULO ABV 20graus
            abv = 131.25 * (og - fg)
            abv = round(abv, 2)
    else:
        form = CalculoABVForm()

    context = {
        'form': form,
        'abv': abv
    }

    return render(request, 'calculoabv.html', context)
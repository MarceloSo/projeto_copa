from django.shortcuts import render
from sistema.models import Selecao

def index(request):
	selecoes = Selecao.objects.all()
	return render(request, 'index.html', {'selecoes':selecoes})

def selecaoAdicionar(request):
	return render(request,'form.html')

def selecaoSalvar(request):
	if request.method == 'POST':
		codigo = request.POST.get('codigo', '0')

		selecao = Selecao()
		selecao.time1 = request.POST.get('time1','')
		selecao.gols1 = request.POST.get('gols1','')

		selecao.time2 = request.POST.get('time2','')
		selecao.gols2 = request.POST.get('gols2','')

		selecao.save()

	#return HttpResponseRedirect('/')
	#return render(request,'form.html')
	return render(request, 'index.html')
# Create your views here.

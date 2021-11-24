from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Post, Form
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST

#pagina inicial
def index(request):
	return render(request, "bioc/index.html")

#pagina de susgestões
def sugestao(request):
	return render(request, "bioc/sugestao/sugest.html")

@require_POST
def submited_form(request):
	sugestao = request.POST['sugestao']
	recado = request.POST['recado']
	categoria = request.POST['categoria']
	foto = request.POST['foto']

	nova_resposta = Form.objects.create(sugestao=sugestao, recado=recado, categoria=categoria, foto=foto)
	nova_resposta.save()
	return HttpResponseRedirect('/')

def sucu_posts(request):
	posts = Post.objects.filter(tipo = 'SC')
	return render(request, 'bioc/post_list.html', {'posts' : posts})

def fito_posts(request):
	posts = Post.objects.filter(tipo = 'FT')
	return render(request, 'bioc/post_listo.html', {'posts' : posts})

class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post


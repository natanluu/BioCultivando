from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView, DetailView

#pagina inicial
def index(request):
	return render(request, "bioc/index.html")

#pagina de susgestões
def sugestao(request):
	return render(request, "bioc/sugestao/sugest.html")

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


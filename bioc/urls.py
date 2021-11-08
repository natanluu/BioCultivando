from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import PostListView, PostDetailView

urlpatterns = [

	#geral
	path('', views.index, name='index'),

	#sugestao
	path('sugestao/sugest.html/', views.sugestao, name='sugestao'),

	#filtros
	path('orna-posts/', views.sucu_posts, name='postso'),
	path('fito-posts/', views.fito_posts, name='posts'),

	#posts
	path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]
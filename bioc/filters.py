import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
	tipo_planta = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Post
		fields = ('Suculentas')
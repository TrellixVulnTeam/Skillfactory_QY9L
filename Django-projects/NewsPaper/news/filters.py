from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'header':['icontains'], 'create_date':['gte'], 'author__name':['exact']}
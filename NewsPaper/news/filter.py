from django.forms import DateInput
from django_filters import FilterSet, CharFilter, DateFromToRangeFilter, DateFilter
from .models import Post, Author



'''class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'postCategory',
            'dateCreation'
        )
'

class data_filter(FilterSet):
    date = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['dateCreation']


class author_filter(FilterSet):
    username = CharFilter(method='my_filter')

    class Meta:
        model = Author
        fields = ['authorUser']

    def my_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,

        })
'''

class PostFilter(FilterSet):
    date = DateFilter(field_name='dateCreation',
                      widget=DateInput(attrs={'type': 'date'}),
                      lookup_expr='lt',
                      label='C даты:')
    title = CharFilter(field_name='title',
                       label='Название',
                       lookup_expr=['icontains'])
    class Meta:
        model = Post
        fields = (
            #'title',
            'author',
            #'postCategory',
            #'dateCreation'
        )
#
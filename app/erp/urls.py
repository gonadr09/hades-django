from django.urls import path
from erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/def/', category_list, name='category_list_def'),
    path('category/list/class/', CategoryListView.as_view(), name='category_list_class')
]

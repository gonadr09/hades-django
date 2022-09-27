from django.shortcuts import render
from django.views.generic import ListView
from erp.models import Category, Product

# Create your views here.

def category_list(request):
    data = {
        'title': 'Listado de categorías',
        'categories': Category.objects.all() 
    }
    return render(request, "category/categories_def.html", data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/categories_class.html'

    def get_queryset(self):
        return Product.objects.all()  # Reemplaza el método de consulta

    def get_context_data(self, **kwargs):  # Agrega claves al contexto
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        return context

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.urls import reverse_lazy
from erp.models import Category, Product
from erp.forms import CategoryForm

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

    #def get_queryset(self):
       # pass
        #return Product.objects.all()  # Reemplaza el método de consulta

    @method_decorator(csrf_exempt)  # Omite el csrf
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):  # Metodo Post
        data = {}
        data = Category.objects.get(id=request.POST['id']).toJSON()
        return JsonResponse(data)

    def get_context_data(self, **kwargs):  # Agrega claves al contexto
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list_class')
        context['entity'] = 'Categorias'
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    #success_url: reverse_lazy('erp:category_list_def') # no funciona usar def get_absolute_url en el modelo

    def get_context_data(self, **kwargs):  # Agrega claves al contexto
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de categoría'
        context['list_url'] = reverse_lazy('erp:category_list_class')
        context['entity'] = 'Categorías'
        return context
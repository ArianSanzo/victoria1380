from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from .models import Product, Image, PrimaryCategory, SecondaryCategory
from .forms import ProductForm, ImageFormSet
from .context_processors import primary_to_secondary_context

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    ordering = ['date']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(primary_category__name__icontains=query) |
                Q(secondary_categories__name__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(primary_to_secondary_context(request=self.request))
        return context

class ProductBaseView(View):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['image_formset'] = ImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['image_formset'] = ImageFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']
        if image_formset.is_valid():
            self.object = form.save()
            image_formset.instance = self.object
            image_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

@method_decorator(login_required(login_url='/users/login/'), name='dispatch')
class ProductCreateView(ProductBaseView, CreateView):
    pass

@method_decorator(login_required(login_url='/users/login/'), name='dispatch')
class ProductUpdateView(ProductBaseView, UpdateView):
    pass
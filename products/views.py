from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Product, Image
from .forms import ProductForm, ImageFormSet

# Create your views here.
def products_list(request):
    products = Product.objects.all().order_by('date')
    return render(request, 'products/products_list.html', {'products': products})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update_page.html'
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
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)
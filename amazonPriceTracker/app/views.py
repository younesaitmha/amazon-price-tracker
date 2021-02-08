from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import AddProductForm

# Create your views here.

def home_view(request):
    no_discounted = 0
    error = None

    form = AddProductForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Ups! Couldn't get the name or price of the product"
        except:
            error = "Ups! something went wrong"

    form = AddProductForm()

    queryset = Product.objects.all()
    number_of_items = queryset.count()
    if number_of_items > 0:
        discount_list =list()
        for item in queryset:
            if item.old_price > item.current_price:
                discount_list.append(item)
        no_discounted = len(discount_list)

    context = {
        'queryset': queryset,
        'number_of_items': number_of_items,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
    }
    return render(request, 'products/index.html', context)

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'products/confirm_delete.html'
    success_url = reverse_lazy('home-view')

def update_product(request):
    queryset = Product.objects.all()
    for product in queryset:
        product.save()
    return redirect('home-view')

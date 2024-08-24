from django.shortcuts import render, redirect
from .models import Subscriber

from django.views.generic import ListView, DetailView
from .models import Product


def opt(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        company_name = request.POST.get('company_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        # Сохранение данных в базе
        Subscriber.objects.create(
            full_name=full_name,
            company_name=company_name,
            phone_number=phone_number,
            email=email
        )
        return redirect('success')

    return render(request, 'email_app/opt.html')


def success(request):
    return render(request, 'email_app/success.html')


def main(request):
    return render(request, 'email_app/main.html')

def catalog(request):
    return render(request, 'email_app/catalog.html')

def privacy_policy(request):
    return render(request, 'email_app/privacy_policy.html')

def user_agreement(request):
    return render(request, 'email_app/user_agreement.html')

def personal_data(request):
    return render(request, 'email_app/personal_data.html')

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.filter(category__in=['teens', 'women', 'children', 'new_arrivals'])
        return queryset


from django.shortcuts import render, get_object_or_404
from .models import Product


def product(request, id):
    # Извлечение товара по id
    product = get_object_or_404(Product, pk=id)
    # Извлечение изображений и похожих продуктов (пример)
    images = product.images.all()
    similar_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]

    context = {
        'product': product,
        'images': images,
        'similar_products': similar_products
    }

    return render(request, 'email_app/product.html', context)



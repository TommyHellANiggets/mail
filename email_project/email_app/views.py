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

from .models import Product

def main(request):
    # Fetch up to 6 products for each category
    kids_products = Product.objects.filter(category='children')[:6]
    teens_products = Product.objects.filter(category='teens')[:6]
    women_products = Product.objects.filter(category='women')[:6]

    context = {
        'kids_products': kids_products,
        'teens_products': teens_products,
        'women_products': women_products,
    }
    return render(request, 'email_app/main.html', context)

def catalog(request):
    return render(request, 'email_app/catalog.html')

def about_brand(request):
    return render(request, 'email_app/about_brand.html')

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



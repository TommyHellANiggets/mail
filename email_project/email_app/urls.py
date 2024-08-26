from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('opt/', views.opt, name='opt'),
    path('catalog/', views.catalog, name='catalog'),
    path('about_brand/', views.about_brand, name='about_brand'),
    path('success/', views.success, name='success'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('user_agreement/', views.user_agreement, name='user_agreement'),
    path('personal_data/', views.personal_data, name='personal_data'),
    path('teenagers/', views.list_teenagers, name='list-teenagers'),
    path('kids/', views.list_kids, name='list-kids'),
    path('adult/', views.list_adult, name='list-adult'),
    path('product/<int:id>/', views.product, name='product-detail'),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

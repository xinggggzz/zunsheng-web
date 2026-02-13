from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/equipment/', views.technical_equipment, name='equipment'),
    path('about/environment/', views.company_environment, name='environment'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('service/philosophy/', views.service_philosophy, name='service_philosophy'),
    path('contact/', views.contact, name='contact'),
]

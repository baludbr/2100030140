from django.urls import path
from . import views

urlpatterns = [
    path('companies/<str:cn>/categories/<str:can>/products', views.top_products, name='Top products'),
]

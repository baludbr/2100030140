from django.urls import path
from .views import NumbersView

urlpatterns = [
    path('numbers/<str:number_type>/', Calc.as_view(), name='numbers')
]
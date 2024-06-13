from django.urls import path
from .views import NumbersView

urlpatterns = [
    path('numbers/<str:numberid>/', Calc.as_view(), name='numbers')
]
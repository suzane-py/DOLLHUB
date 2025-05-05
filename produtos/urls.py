from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('registrar_venda/<int:produto_id>/', views.registrar_venda, name='registrar_venda'),
]
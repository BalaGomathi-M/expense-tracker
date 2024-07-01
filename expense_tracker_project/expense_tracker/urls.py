from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('expense_create/', views.expense_create, name='expense_create'),
    path('expense_list/', views.expense_list, name='expense_list')
]

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.add_project_account, name='Project_account'),
    path('projectExpense/', views.ShowProjectExpense, name='Project_Expense'),

]
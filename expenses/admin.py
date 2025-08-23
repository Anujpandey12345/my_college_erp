from django.contrib import admin
from .models import ComputerExpense, DailyExpense

admin.site.register(ComputerExpense)
admin.site.register(DailyExpense)

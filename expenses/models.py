from django.db import models

class ComputerExpense(models.Model):
    CATEGORY_CHOICES = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Maintenance', 'Maintenance'),
        ('Other', 'Other'),
    ]

    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name

from django.db import models
from django.contrib.auth.models import User

class DailyExpense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Stationery', 'Stationery'),
        ('Mobile Recharge', 'Mobile Recharge'),
        ('Entertainment', 'Entertainment'),
        ('Hostel', 'Hostel'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # To support multiple students
    title = models.CharField(max_length=100, help_text="What did you spend on?")
    amount = models.DecimalField(max_digits=8, decimal_places=2, help_text="How much did you spend?")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True, help_text="Optional note")

    def __str__(self):
        return f"{self.title} - ₹{self.amount} on {self.date}"

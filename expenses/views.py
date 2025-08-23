from django.shortcuts import render, redirect, get_object_or_404
from .models import ComputerExpense, DailyExpense
from .forms import ComputerExpenseForm, DailyExpenseForm
from django.contrib.auth.decorators import login_required

def expense_list(request):
    expenses = ComputerExpense.objects.all().order_by('-date')
    total_cost = sum(exp.cost for exp in expenses)
    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_cost': total_cost,
    })

def add_expense(request):
    if request.method == 'POST':
        form = ComputerExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ComputerExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

def edit_expense(request, pk):
    expense = get_object_or_404(ComputerExpense, pk=pk)
    if request.method == 'POST':
        form = ComputerExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ComputerExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(ComputerExpense, pk=pk)
    expense.delete()
    return redirect('expense_list')




from django.shortcuts import render, redirect
from .forms import DailyExpenseForm
from .models import DailyExpense

def dailyExpenses(request):
    if request.method == "POST":
        form = DailyExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            # expense.user = request.user  ← REMOVE THIS LINE
            expense.save()
            return redirect('daily_expenses')
    else:
        form = DailyExpenseForm()

    expenses = DailyExpense.objects.all().order_by('-date')  # show all
    return render(request, 'expenses/daily_expense.html', {
        'form': form,
        'expenses': expenses
    })

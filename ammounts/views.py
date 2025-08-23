from django.shortcuts import render
from django.shortcuts import render
from ammounts.models import ProjectAccounts
from project.forms import createForm
# Create your views here.


from django.shortcuts import render, redirect
from .forms import CreateForm

def add_project_account(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ammounts/')  # redirect after successful save
        else:
            print(form.errors)  # debug errors
    else:
        form = CreateForm()
    return render(request, 'ammounts/ProjectAccounts.html', {'form': form})


def ShowProjectExpense(request):
    data = ProjectAccounts.objects.all() # ojects.all() means all the objects which is inside the class(project model)
    print("Data: ", data)
    context = {'data': data}
    return render(request, 'ammounts/showProjectExpense.html', context)




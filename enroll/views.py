from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
# Create your views here.
def home(request):
    Employees = Employee.objects.all()
    return render(request,'home.html', {'Enmployees':Employees})

def create_view(request):
    return render(request, 'create.html')
    
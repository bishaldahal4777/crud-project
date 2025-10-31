from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
# Create your views here.
def home(request):
    Employees = Employee.objects.all()
    return render(request,'home.html', {'Enmployees':Employees})

def create_view(request):
    return render(request, 'create.html')

def create_emp(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        emp_dept = request.POST.get('emp_dept')

        if emp_id and emp_name and emp_dept:
            Employee.objects.create(emp_id=emp_id, emp_name=emp_name,emp_dept=emp_dept)
            return redirect("/")
    return render(request, 'create.html')

def update_view(request, id):
    Employee = get_object_or_404(request, id=id)
    return render(request, 'update.html',{'Employee':Employee})

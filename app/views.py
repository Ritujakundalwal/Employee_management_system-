from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Employee



from django.db.models import Avg

@login_required(login_url='login')
def home(request):
    total_employees = Employee.objects.count()
    it_count = Employee.objects.filter(department="IT").count()
    hr_count = Employee.objects.filter(department="HR").count()
    avg_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg']

    return render(request, 'employee/home.html', {
        'total_employees': total_employees,
        'it_count': it_count,
        'hr_count': hr_count,
        'avg_salary': avg_salary
    })


def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'employee/register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'employee/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')



from django.db.models import Q

@login_required(login_url='login')
def employee_list(request):
    query = request.GET.get('q')

    if query:
        employees = Employee.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )
    else:
        employees = Employee.objects.all()

    return render(request, 'employee/employee_list.html', {
        'employees': employees,
        'query': query
    })



@login_required(login_url='login')
def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            salary=request.POST.get('salary'),
            department=request.POST.get('department'),
            date_of_joining=request.POST.get('date_of_joining')
        )
        messages.success(request, "Employee added successfully")
        return redirect('employee_list')

    return render(request, 'employee/add_employee.html')

@login_required(login_url='login')
def update_employee(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.salary = request.POST.get('salary')
        emp.department = request.POST.get('department')
        emp.date_of_joining = request.POST.get('date_of_joining')
        emp.save()

        messages.success(request, "Employee updated successfully")
        return redirect('employee_list')

    return render(request, 'employee/update_employee.html', {
        'emp': emp
    })

@login_required(login_url='login')
def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    messages.success(request, "Employee deleted successfully")
    return redirect('employee_list')

from django.db.models import Count, Avg
from .models import Employee

def home(request):
    total_employees = Employee.objects.count()
    it_count = Employee.objects.filter(department="IT").count()
    hr_count = Employee.objects.filter(department="HR").count()
    avg_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg']

    # 🔹 Department-wise chart data
    dept_data = (
        Employee.objects
        .values('department')
        .annotate(count=Count('id'))
    )

    labels = [d['department'] for d in dept_data]
    data = [d['count'] for d in dept_data]

    return render(request, 'employee/home.html', {
        'total_employees': total_employees,
        'it_count': it_count,
        'hr_count': hr_count,
        'avg_salary': avg_salary,
        'labels': labels,
        'data': data,
    })

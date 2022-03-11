import json
from django.http import HttpResponse
from django.core.serializers import serialize
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.db.models import Sum
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *

# Create your views here.

@unauthenticated_user
def loginPage(request):
    
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user  = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.error(request,'Invalid credentials')

    
    return render(request, 'drivingschool/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def RegisterPage(request):

    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'drivingschool/register.html', context)








# admin views

@login_required(login_url='login')
@admin_only
def DashboardPage(request):
    instructors = instructor.objects.all()
    students = student.objects.all()
    payments = payment.objects.all()

    total_instructors = instructors.count()
    total_students = students.count()

    #calculating the total income, here use aggregation and sum from django.db.models import
    income = payments.aggregate(Sum('price_paid'))['price_paid__sum']

    mydict = {'instructors': total_instructors, 'students': total_students, 'total_income':income}
    return render(request, 'drivingschool/admin-dashboard/dashboard.html', mydict)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def manageStudent(request):

    students = student.objects.all()

    return render(request, 'drivingschool/admin-dashboard/manage-student.html', {'students':students})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def addStudent(request):

    form = studentForm()

    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage-student')

    mydict = {'form': form}
    return render(request, 'drivingschool/admin-dashboard/add-student.html', mydict)

@login_required(login_url='login')
def manageInstructorPage(request):

    instructors = instructor.objects.all()

    mydict = {'instructors':instructors}
    return render(request, 'drivingschool/admin-dashboard/manage-instructor.html', mydict)

@login_required(login_url='login')
@admin_only
def addInstructorPage(request):
   
    form = instructorForm()

    if request.method == 'POST':
        print('Printed post:', request.POST) #debugging purposes
        form = instructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-instructor')

    mydict = {'form':form}
    return render(request, 'drivingschool/admin-dashboard/add-instructor.html', mydict)

@login_required(login_url='login')
@admin_only
def addSchedulePage(request):

    form = scheduleForm()

    if request.method == 'POST':
        print("Schedules:", request.POST)
        form = scheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-schedule')

    mydict = {'form': form}
    return render (request, 'drivingschool/admin-dashboard/add-schedule.html', mydict)
      
@login_required(login_url='login')
@admin_only
def manageSchedulePage(request):

    schedules = schedule.objects.all()
    return render(request, 'drivingschool/admin-dashboard/manage-schedule.html', {'schedules': schedules})

@login_required(login_url='login')
@admin_only
def addEnrollPage(request):

    form = enrollmentForm()

    if request.method == 'POST':
        form = enrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-enroll')

    mydict = {'form': form}
    return render(request, 'drivingschool/admin-dashboard/add-enroll.html',mydict)


@login_required(login_url='login')
@admin_only
def manageEnrollPage(request):

    enrolls = enrollment.objects.all()
    return render(request, 'drivingschool/admin-dashboard/manage-enroll.html', {'enrollments':enrolls})

@login_required(login_url='login')
@admin_only
def addPaymentPage(request):


    form = paymentForm()
    # payments = payment.objects.all()

    if request.method == 'POST':
        form = paymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-payment')

    mydict = {'form': form}
    return render(request, 'drivingschool/admin-dashboard/add-payment.html',mydict)

@login_required(login_url='login')
@admin_only
def managePaymentPage(request):

    payments = payment.objects.all()
    return render(request, 'drivingschool/admin-dashboard/manage-payment.html', {'payments':payments})

# ========dynamic delete views=======
@admin_only
def deleteStudent(request, pk):

    students = student.objects.get(id=pk)
    students.delete()
    return redirect('manage-student')

@admin_only
def deleteInstructor(request, pk):

    instructors = instructor.objects.get(id=pk)
    instructors.delete()
    return redirect('manage-instructor')

@admin_only
def deleteSchedule(request, pk):

    schedules = schedule.objects.get(id=pk)
    schedules.delete()
    return redirect('manage-schedule')

@admin_only
def deleteEnrollment(request, pk):

    enroll = enrollment.objects.get(id=pk)
    enroll.delete()
    return redirect('manage-enroll')

@admin_only
def deletePayment(request, pk):

    payments = payment.objects.get(id=pk)
    payments.delete()
    return redirect('manage-payment')


# ========dynamic update views=======
@admin_only
def updateInstructor(request, pk):

    update = instructor.objects.get(id=pk)
    form = instructorForm(instance=update)
    
    if request.method == 'POST':
        print('Update:', request.POST) #debugging purposes
        form = instructorForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('manage-instructor')
    

    
    mydict = {'form': form}

    return render(request, 'drivingschool/admin-dashboard/add-instructor.html', mydict)

@admin_only
def updateStudent(request, pk):
    update = student.objects.get(id=pk)
    form = studentForm(instance=update)

    if request.method == 'POST':
        form  = studentForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('manage-student')

    mydict = {'form': form}
    return render(request, 'drivingschool/admin-dashboard/add-student.html', mydict)


@admin_only
def updateSchedule(request, pk):

    update = schedule.objects.get(id=pk)
    form = scheduleForm(instance=update)

    if request.method == 'POST':
        form = scheduleForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('manage-schedule')

    mydict = {'form': form}
    return render(request, 'drivingschool/admin-dashboard/add-schedule.html',mydict)

@admin_only
def updateEnroll(request, pk):
    
    update = enrollment.objects.get(id=pk)
    form = enrollmentForm(instance=update)

    if request.method == 'POST':
        form = enrollmentForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('manage-enroll')

    mydict = {'form': form}
    return render(request, 'drivingschool/admin-dashboard/add-enroll.html',mydict)

@admin_only
def updatePayment(request, pk):
    
    update = payment.objects.get(id=pk)
    form = paymentForm(instance=update)

    if request.method == 'POST':
        form = paymentForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('manage-payment')

    mydict = {'form': form}
    return render(request, 'drivingschool/admin-dashboard/add-payment.html',mydict)





# student views
@login_required(login_url='login')
# @student_only
def StudentDashboard(request):
    return render(request, 'drivingschool/student-dashboard/index.html')

@login_required(login_url='login')
@student_only
def StudentProfile(request):
    return render(request, 'drivingschool/student-dashboard/profile.html')

@login_required(login_url='login')
@student_only
def StudentSchedule(request):
    return render(request, 'drivingschool/student-dashboard/schedule.html')

@login_required(login_url='login')
@student_only
def StudentPayment(request):
    return render(request, 'drivingschool/student-dashboard/payment.html')

@login_required(login_url='login')
@student_only
def StudentReport(request):
    return render(request, 'drivingschool/student-dashboard/report.html')


# instructor views

@login_required(login_url='login')
@instructor_only
def instructorDashboard(request):
    return render(request, 'drivingschool/instructor-dashboard/index.html')


@login_required(login_url='login')
@instructor_only
def MasterLIst(request):
    return render(request, 'drivingschool/instructor-dashboard/master-list.html')

@login_required(login_url='login')
@instructor_only
def addReport(request):
    return render(request, 'drivingschool/instructor-dashboard/add-report.html')

@instructor_only
def manageReport(request):
    return render(request, 'drivingschool/instructor-dashboard/manage-report.html')


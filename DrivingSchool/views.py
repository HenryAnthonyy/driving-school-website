from django.shortcuts import render
from .models import *
from django.db.models import Sum

# Create your views here.

# admin views
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

def StudentPage(request):

    students = student.objects.all()

    return render(request, 'drivingschool/admin-dashboard/student.html', {'students':students})

def manageInstructorPage(request):

    instructors = instructor.objects.all()
    return render(request, 'drivingschool/admin-dashboard/manage-instructor.html', {'instructors':instructors})

def addInstructorPage(request):
    return render(request, 'drivingschool/admin-dashboard/add-instructor.html')

def addSchedulePage(request):
    return render(request, 'drivingschool/admin-dashboard/add-schedule.html')

def manageSchedulePage(request):

    schedules = schedule.objects.all()
    return render(request, 'drivingschool/admin-dashboard/manage-schedule.html', {'schedules': schedules})

def addEnrollPage(request):
    return render(request, 'drivingschool/admin-dashboard/add-enroll.html')

def manageEnrollPage(request):

    enrolls = enrollment.objects.all()
    return render(request, 'drivingschool/admin-dashboard/manage-enroll.html', {'enrollments':enrolls})

def addPaymentPage(request):
    return render(request, 'drivingschool/admin-dashboard/add-payment.html')

def managePaymentPage(request):

    payments = payment.objects.all()
    return render(request, 'drivingschool/admin-dashboard/manage-payment.html', {'payments':payments})


# student views

def StudentDashboard(request):
    return render(request, 'drivingschool/student-dashboard/index.html')

def StudentProfile(request):
    return render(request, 'drivingschool/student-dashboard/profile.html')

def StudentSchedule(request):
    return render(request, 'drivingschool/student-dashboard/schedule.html')

def StudentPayment(request):
    return render(request, 'drivingschool/student-dashboard/payment.html')

def StudentReport(request):
    return render(request, 'drivingschool/student-dashboard/report.html')


# instructor views

def instructorDashboard(request):
    return render(request, 'drivingschool/instructor-dashboard/index.html')


def MasterLIst(request):
    return render(request, 'drivingschool/instructor-dashboard/master-list.html')

def addReport(request):
    return render(request, 'drivingschool/instructor-dashboard/add-report.html')

def manageReport(request):
    return render(request, 'drivingschool/instructor-dashboard/manage-report.html')
from django.shortcuts import render

# Create your views here.

# admin views
def DashboardPage(request):
    return render(request, 'drivingschool/admin-dashboard/dashboard.html')

def StudentPage(request):
    return render(request, 'drivingschool/admin-dashboard/student.html')

def manageInstructorPage(request):
    return render(request, 'drivingschool/admin-dashboard/manage-instructor.html')

def addInstructorPage(request):
    return render(request, 'drivingschool/admin-dashboard/add-instructor.html')

def addSchedulePage(request):
    return render(request, 'drivingschool/admin-dashboard/add-schedule.html')

def manageSchedulePage(request):
    return render(request, 'drivingschool/admin-dashboard/manage-schedule.html')

def addEnrollPage(request):
    return render(request, 'drivingschool/admin-dashboard/add-enroll.html')

def manageEnrollPage(request):
    return render(request, 'drivingschool/admin-dashboard/manage-enroll.html')

def addPaymentPage(request):
    return render(request, 'drivingschool/admin-dashboard/add-payment.html')

def managePaymentPage(request):
    return render(request, 'drivingschool/admin-dashboard/manage-payment.html')


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
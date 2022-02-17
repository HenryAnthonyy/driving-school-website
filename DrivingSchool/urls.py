from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    
    # admin------------
    path('', views.DashboardPage, name = 'dashboard'),
    path('student-list',views.StudentPage, name = 'student-list'),
    path('manage-instructor',views.manageInstructorPage, name = 'manage-instructor'),
    path('add-instructor',views.addInstructorPage, name = 'add-instructor'),
    path('add-schedule',views.addSchedulePage, name = 'add-schedule'),
    path('manage-schedule',views.manageSchedulePage, name = 'manage-schedule'),
    path('add-enroll',views.addEnrollPage, name = 'add-enroll'),
    path('manage-enroll',views.manageEnrollPage, name = 'manage-enroll'),
    path('add-payment',views.addPaymentPage, name = 'add-payment'),
    path('manage-payment',views.managePaymentPage, name = 'manage-payment'),

#    ----------- student------------
    
    path('student-dashboard', views.StudentDashboard, name = 'student-dashboard'),
    path('student-profile', views.StudentProfile, name = 'student-profile'),
    path('student-schedule', views.StudentSchedule, name = 'student-schedule'),
    path('student-payment', views.StudentPayment, name = 'student-payment'),
    path('student-report', views.StudentReport, name = 'student-report'),


    #----------- instructor------------------------

    path('instructor-dashboard', views.instructorDashboard, name = 'instructor-dashboard'),
    path('instructor-master-list', views.MasterLIst, name = 'master-list'),
    path('instructor-add-report', views.addReport, name = 'instructor-add-report'),
    path('instructor-manage-report', views.manageReport, name = 'instructor-manage-report'),
    

]
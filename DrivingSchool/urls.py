from unicodedata import name
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('login', views.loginPage, name='login'),
    path('register', views.RegisterPage, name='register'),
    path('logout', views.logoutUser, name='logout'),


    #------------- admin------------
    
    path('', views.DashboardPage, name = 'dashboard'),
    path('add-student',views.addStudent, name = 'add-student'),
    path('manage-student',views.manageStudent, name = 'manage-student'),
    path('manage-instructor',views.manageInstructorPage, name = 'manage-instructor'),
    path('add-instructor',views.addInstructorPage, name = 'add-instructor'),
    path('add-schedule',views.addSchedulePage, name = 'add-schedule'),
    path('manage-schedule',views.manageSchedulePage, name = 'manage-schedule'),
    path('add-enroll',views.addEnrollPage, name = 'add-enroll'),
    path('manage-enroll',views.manageEnrollPage, name = 'manage-enroll'),
    path('add-payment',views.addPaymentPage, name = 'add-payment'),
    path('manage-payment',views.managePaymentPage, name = 'manage-payment'),

    path('settings/<str:pk>',views.adminProfile, name = 'settings'),

    
    path('update-student/<str:pk>', views.updateStudent, name ='update-student'),
    path('update-instructor/<str:pk>', views.updateInstructor, name ='update-instructor'),
    path('update-schedule/<str:pk>', views.updateSchedule, name ='update-schedule'),
    path('update-enroll/<str:pk>', views.updateEnroll, name ='update-enroll'),
    path('update-payment/<str:pk>', views.updatePayment, name ='update-payment'),

    # ==========delete urls=================
    path('delete-student/<str:pk>', views.deleteStudent, name ='delete-student'),
    path('delete-instructor/<str:pk>', views.deleteInstructor, name ='delete-instructor'),
    path('delete-enroll/<str:pk>', views.deleteEnrollment, name ='delete-enroll'),
    path('delete-schedule/<str:pk>', views.deleteSchedule, name ='delete-schedule'),
    path('delete-payment/<str:pk>', views.deletePayment, name ='delete-payment'),



#    ----------- student------------
    
    path('student', views.StudentDashboard, name = 'student'),
    path('student-profile', views.StudentProfile, name = 'student-profile'),
    path('student-schedule', views.StudentSchedule, name = 'student-schedule'),
    path('student-payment', views.StudentPayment, name = 'student-payment'),
    path('student-report', views.StudentReport, name = 'student-report'),


    #----------- instructor------------------------

    path('instructor', views.instructorDashboard, name = 'instructor'),
    path('instructor-master-list', views.MasterLIst, name = 'master-list'),
    path('instructor-add-report', views.addReport, name = 'instructor-add-report'),
    path('instructor-manage-report', views.manageReport, name = 'instructor-manage-report'),


    # ---------------password reset urls----------
    # path('settings/update-password', views.passwordChange, name = 'password-change'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

]
from os import name
from django.urls import path
from .import views

urlpatterns = [
    # ----instructors----
    path('instructors', views.getInstructors),
    path('add/instructors', views.addInstructor, name='add-instructor'),
    path('update/instructor/<str:pk>', views.updateInstructor, name='update-instructor'),
    path('delete/instructor/<str:pk>', views.deleteInstructor, name='delete-instructor'),
    

    # -----student-----
    path('students', views.getStudents),
    path('add/student', views.addStudent),
    path('update/student/<str:pk>', views.updateStudent, name='update-student'),
    path('delete/student/<str:pk>', views.deleteStudent, name='delete-student'),

    # -----schedule-----

    path('schedules', views.getSchedule),
    path('add/schedule', views.addSchedule, name='add-schedule'),
    path('update/schedule/<str:pk>', views.updateSchedule, name='update-schedule'),
    path('delete/schedule/<str:pk>', views.deleteSchedule, name='delete-schedule'),


    # -----enrollments-----

    path('enrollments', views.getEnrollment),
    path('add/enrollments', views.addEnrollment, name='add-enrollment'),
    path('update/enrollment/<str:pk>', views.updateEnrollment, name='update-enrollment'),
    path('delete/enrollment/<str:pk>', views.deleteEnrollment, name='delete-enrollment'),

    # -----payments-----

    path('payments', views.getPayment),
    path('add/payment', views.addPayment, name='add-payment'),
    path('update/payment/<str:pk>', views.updatePayment, name='update-payment'),
    path('delete/payment/<str:pk>', views.deletePayment, name='delete-payment'),
]
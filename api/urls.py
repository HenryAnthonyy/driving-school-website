from os import name
from django.urls import path
from .import views

urlpatterns = [
    # ----instructors----
    path('instructors', views.getInstructors),
    path('add/instructors', views.addInstructor, name='api-add-instructor'),
    path('update/instructor/<str:pk>', views.updateInstructor, name='api-update-instructor'),
    path('delete/instructor/<str:pk>', views.deleteInstructor, name='api-delete-instructor'),
    

    # -----student-----
    path('students', views.getStudents),
    path('add/student', views.addStudent),
    path('update/student/<str:pk>', views.updateStudent, name='api-update-student'),
    path('delete/student/<str:pk>', views.deleteStudent, name='api-delete-student'),

    # -----schedule-----

    path('schedules', views.getSchedule),
    path('add/schedule', views.addSchedule, name='add-schedule'),
    path('update/schedule/<str:pk>', views.updateSchedule, name='api-update-schedule'),
    path('delete/schedule/<str:pk>', views.deleteSchedule, name='api-delete-schedule'),


    # -----enrollments-----

    path('enrollments', views.getEnrollment),
    path('add/enrollments', views.addEnrollment, name='api-add-enrollment'),
    path('update/enrollment/<str:pk>', views.updateEnrollment, name='api-update-enrollment'),
    path('delete/enrollment/<str:pk>', views.deleteEnrollment, name='api-delete-enrollment'),

    # -----payments-----

    path('payments', views.getPayment),
    path('add/payment', views.addPayment, name='add-payment'),
    path('update/payment/<str:pk>', views.updatePayment, name='api-update-payment'),
    path('delete/payment/<str:pk>', views.deletePayment, name='api-delete-payment'),
]
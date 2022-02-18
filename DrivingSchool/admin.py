from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(instructor)
admin.site.register(student)
admin.site.register(schedule)
admin.site.register(enrollment)
admin.site.register(payment)
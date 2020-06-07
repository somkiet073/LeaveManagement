from django.contrib import admin

from employee.models import Profile, Department, AppoveGroup
# Register your models here.


admin.site.register(Profile)
admin.site.register(Department)
admin.site.register(AppoveGroup)

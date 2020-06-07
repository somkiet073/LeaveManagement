from django.contrib import admin
from leave.models import LeaveType, Leave
# Register your models here.
admin.site.register(LeaveType)
admin.site.register(Leave)
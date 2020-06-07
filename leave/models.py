from django.db import models
from django.contrib.auth.models import User
from employee.models import AppoveGroup

# Create your models here.


class LeaveType(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('1', 'ลาป่วย'),
        ('2', 'ลากิจ'),
        ('3', 'ลาพักผ่อน'),
        ('4', 'อื่นๆ'),
    ]
    LEAVE_TYPE_STATUS_CHOICES = [
        ('1', 'ใช้งาน'),
        ('2', 'ยกเลิก'),
    ]
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=LEAVE_TYPE_STATUS_CHOICES)
    quota = models.IntegerField()

    def __str__(self):
        return self.name

        def get_Typename():     
            names = LeaveType.objects.only('name')
            names = [(str(item), item) for item in names]
            return names


class Leave(models.Model):
    choices = [
        ('F', 'เต็มวัน'),
        ('HA', 'ครึ่งวันเช้า'),
        ('HP', 'ครึ่งวันบ่าย'),
    ]

    status_choices = [
        ('D', ''),
        ('Y', 'Approved'),
        ('N', 'Rejected'),
    ]

    STATUS = [
        (1, 'Pending'),
        (2, 'send')
    ]

    leavetype = models.ForeignKey(
        LeaveType, on_delete=models.CASCADE, related_name="LeaveType")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    generated_time = models.DateField(auto_now_add=True)
    start_time = models.DateField()
    end_time = models.DateField()
    period = models.CharField(choices=choices, max_length=3, default='F')
    leave_sum = models.FloatField()
    letter_status = models.IntegerField(choices=STATUS, default=1)
    approved_by = models.ForeignKey(
        AppoveGroup, on_delete=models.CASCADE, blank=True, null=True, related_name='appoveGroup')
    approved_time = models.DateField(null=True, blank=True)
    approved_status = models.CharField(
        choices=status_choices, max_length=2, default='D')
    checked_by = models.ForeignKey(
        AppoveGroup, on_delete=models.CASCADE, blank=True, null=True, related_name='checked_by')
    checked_time = models.DateField(null=True, blank=True)
    checked_status = models.CharField(
        choices=status_choices, max_length=2, default='D')
    reply_note = models.CharField(max_length=2000)

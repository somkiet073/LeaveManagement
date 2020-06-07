from django.db import models
from django.contrib.auth.models import User

class AppoveGroup(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True, related_name='Appoved')
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0}".format(self.user)

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "{0}".format(self.name)

class Prename(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class Positions(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True) 

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'ชาย'),
        ('W', 'หญิง'),
    ]

    STATUS_CHOICES = [
        ('1', 'ปกติ'),
        ('2', 'พ้น'),
    ]
    prename = models.ForeignKey(Prename, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    img_profile = models.ImageField(upload_to='img_profile/', blank=True, null=True)

    def __str__(self):
        return "{0} {1} ".format(self.user.first_name, self.user.last_name)

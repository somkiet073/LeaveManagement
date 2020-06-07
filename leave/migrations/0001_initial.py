# Generated by Django 2.2.12 on 2020-06-04 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('1', 'ใช้งาน'), ('2', 'ยกเลิก')], max_length=2)),
                ('quota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_time', models.DateField(auto_now_add=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('period', models.CharField(choices=[('F', 'เต็มวัน'), ('HA', 'ครึ่งวันเช้า'), ('HP', 'ครึ่งวันบ่าย')], default='F', max_length=3)),
                ('leave_sum', models.FloatField()),
                ('letter_status', models.IntegerField(choices=[(1, 'Pending'), (2, 'send')], default=1)),
                ('approved_time', models.DateField(blank=True, null=True)),
                ('approved_status', models.CharField(choices=[('D', ''), ('Y', 'Approved'), ('N', 'Rejected')], default='D', max_length=2)),
                ('checked_time', models.DateField(blank=True, null=True)),
                ('checked_status', models.CharField(choices=[('D', ''), ('Y', 'Approved'), ('N', 'Rejected')], default='D', max_length=2)),
                ('reply_note', models.CharField(max_length=2000)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appoveGroup', to='employee.AppoveGroup')),
                ('checked_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_by', to='employee.AppoveGroup')),
                ('leavetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LeaveType', to='leave.LeaveType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

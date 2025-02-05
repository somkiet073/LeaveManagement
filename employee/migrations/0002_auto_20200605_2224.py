# Generated by Django 2.2.12 on 2020-06-05 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appovegroup',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Appoved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Positions'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prename',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Prename'),
        ),
    ]

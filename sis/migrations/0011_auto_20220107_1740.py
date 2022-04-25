# Generated by Django 3.2.9 on 2022-01-07 22:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sis', '0010_auto_20220105_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='code',
            field=models.CharField(default='EE483703', editable=False, max_length=5, unique=True),
        ),
        migrations.RemoveField(
            model_name='class',
            name='student',
        ),
        migrations.AddField(
            model_name='class',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='school',
            name='student_code',
            field=models.CharField(default='ABFF7EA1', editable=False, max_length=5, unique=True),
        ),
    ]
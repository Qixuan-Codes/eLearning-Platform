# Generated by Django 4.2.9 on 2024-02-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eLearningApp', '0006_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='materials',
            field=models.FileField(blank=True, null=True, upload_to='course_materials/'),
        ),
    ]
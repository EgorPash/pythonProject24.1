# Generated by Django 5.1 on 2024-10-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='course_previews'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_previews'),
        ),
    ]

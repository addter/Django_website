# Generated by Django 3.2.6 on 2021-08-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_create_signup_create1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='create1',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=122)),
                ('password', models.CharField(max_length=80)),
                ('confirm_password', models.CharField(max_length=80)),
                ('create', models.BooleanField(verbose_name=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='queries',
            field=models.CharField(choices=[('Personal Question', 'Personal Question'), ('Site Bugs', 'Site Bugs'), ('About Books', 'About Books'), ('About Our Services', 'About Our Services'), ('Other', 'Other')], max_length=100),
        ),
    ]

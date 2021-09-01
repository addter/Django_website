from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    queries_choose = (
        ('Personal Question', 'Personal Question'),
        ('Site Bugs', 'Site Bugs'),
        ('About Books', 'About Books'),
        ('About Our Services', 'About Our Services'),
        ('Other', 'Other'),
    )
    queries = models.CharField(max_length=100, choices=queries_choose)
    tell_us = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

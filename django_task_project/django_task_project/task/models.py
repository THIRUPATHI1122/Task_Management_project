from django.db import models

#Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField()
    remark = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


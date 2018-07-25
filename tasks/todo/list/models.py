from django.db import models
from list import constants
# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    completion_date=models.DateTimeField()
    priority=models.CharField(max_length=100,choices=constants.tasks_priority)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title
from django.db import models
import datetime
import pyrebase

# Create your models here.
class Goal(models.Model):
    goal_name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=100)
    date_createG = models.DateTimeField(default=datetime.date.today)
    dueDateG = models.DateTimeField(null=False,default=datetime.date.today)
    doneDateG = models.DateTimeField(null=True)

    def __str__(self):
        return 'goal {}'.format(self.goal_name)

    def get_Status(self):
        status = 0
        total = 0
        substasks = Subtask.objects.all()
        for task in substasks:
            if task.goal_name.goal_name == self.goal_name:
                total += 1
                if task.doneDateS is not None:
                    status += 1
        return (status/total) * 100

class Subtask(models.Model):
    goal_name = models.ForeignKey(Goal, null=True, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    doneDateS = models.DateTimeField(null=True)

    date_createS = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return 'Subtasks: {} , of {}'.format(self.task_name,self.goal_name)


from django.db import models


class Task(models.Model):
    title = models.TextField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class category(models.Model):
    category = models.ForeignKey(Task, on_delete=models.PROTECT())




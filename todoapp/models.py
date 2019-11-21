from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    content = models.TextField(verbose_name='Content', null=True)
    completed = models.BooleanField(verbose_name='Status')
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    due_date = models.DateTimeField(verbose_name='Due date', null=True)

    def __str__(self):
        return self.title

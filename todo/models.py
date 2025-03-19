from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    discription = models.TextField()
    completed = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    # about = Title + Discription

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    @property
    def about(self):
        return self.title + " - " + self.discription

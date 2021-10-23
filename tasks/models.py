from django.db import models
from django.contrib.auth.models import User

COLOR_CHOICES = (
    ('green', 'green'),
    ('red', 'red'),
    ('yellow', 'yellow'),
    ('blue', 'blue'),
    ('orange', 'orange')
)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    color = models.CharField(choices=COLOR_CHOICES, max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

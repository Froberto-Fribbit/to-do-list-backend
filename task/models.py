from django.db import models

class Task(models.Model):
    content_text = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.pk}: {self.content_text}"
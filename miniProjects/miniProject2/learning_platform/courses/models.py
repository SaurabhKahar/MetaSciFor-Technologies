from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, default="Untitled Course")
    description = models.TextField()

    def __str__(self):
        return self.name

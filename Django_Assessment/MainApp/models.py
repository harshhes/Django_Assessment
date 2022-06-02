from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    email = models.EmailField(blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        
from django.db import models

# Create your models here.

class article(models.Model):
    question = models.TextField()
    summary = models.TextField()
    content = models.TextField()
    published = models.DateField(blank = True)
    title = models.CharField(unique = True, max_length = 70)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.question
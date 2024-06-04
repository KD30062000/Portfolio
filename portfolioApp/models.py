from django.db import models

# Create your models here.
class Emails(models.Model):
    email1=models.EmailField()
    email2=models.CharField(max_length=100)

    def __str__(self):
        return self.email2

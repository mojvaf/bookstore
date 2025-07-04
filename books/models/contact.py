from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=2500, blank=True, null=True)

    def __str__(self):
        return f'Contact : {self.name}'
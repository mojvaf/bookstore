from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    review = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        return f"Books store: {self.name}"

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})



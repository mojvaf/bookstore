from django.db import models
from django.urls import reverse


class Publisher(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"publisher's name :   {self.name}"
    


class Author(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    review = models.TextField(max_length=1500, blank=True, null=True)


    def __str__(self):
        return f"Books store: {self.name}"

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})



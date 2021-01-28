from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, default='')
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name

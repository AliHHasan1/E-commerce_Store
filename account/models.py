from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    #تم جعل الemail حقل unique
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=500)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
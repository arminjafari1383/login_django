from django.db import models


#this class for signup
class Personsignup(models.Model):
    entered_username = models.CharField(max_length=200)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.firstname
from django.contrib.admin import ModelAdmin, register
from .models import Personsignup

#register sign up class
@register(Personsignup)
class signupAdmin(ModelAdmin):
    pass


from ..models import *
from rest_framework.serializers import ModelSerializer,CharField


class PersonsignupSerializer(ModelSerializer):
    class Meta:
        model = Personsignup
        fields = '__all__'
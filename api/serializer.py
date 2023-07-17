from rest_framework import serializers
from .models import Programmer

class ProgrammerSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Programmer
      #  fields = ('fullname', ' nickname')
        fields = '__all__'
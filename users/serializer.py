from rest_framework import serializers
from .models import *

class ReacSerializer(serializer.ModelSerializer):
    class Meta:
        model = React
        fields = ['',...]

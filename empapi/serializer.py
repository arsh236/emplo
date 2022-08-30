from empapi.models import Emp
from rest_framework import serializers

class EmpSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Emp
        fields="__all__"


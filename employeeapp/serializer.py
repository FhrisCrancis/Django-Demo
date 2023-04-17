from .models import Employee
from rest_framework import serializers

#used to convert querysets from ORM to json that python can interpret
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
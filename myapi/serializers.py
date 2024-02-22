from rest_framework import serializers
from company.models import Employee, Team

class EmployeeSerializerTeam(serializers.ModelSerializer):
    
    class Meta:
        model=Employee
        fields="__all__"


class TeamSerializer(serializers.ModelSerializer):
    manager=EmployeeSerializerTeam() 
    class Meta:
        model=Team
        fields="__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    
    team=TeamSerializer() 
    class Meta:
        model=Employee
        fields="__all__"



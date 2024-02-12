from .models import Task,Employee
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_name','task_desc','completed','image']

class Empserializers(serializers.ModelSerializer):
    class Meta:
        model = Employee       
        fields =  '__all__'
        
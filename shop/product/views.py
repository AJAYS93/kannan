from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import TaskSerializers,Empserializers
from .models import Task,Employee
# Create your views here.

class Taskviewsets(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers

class Dueviewsets(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializers

class Completedviewsets(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializers    

class Employeedetails(APIView):
    def get(self,request):
        obj = Employee.objects.all()
        serialzer = Empserializers(obj,many=True)
        return Response(serialzer.data,status= status.HTTP_200_OK)

    def post(self,request):  
        serializer = Empserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class Employeeinfo(APIView):
    def get(self,request,id):
        try:
            obj= Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = Empserializers(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {'msg':'not found error'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND) 
        serializer = Empserializers(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)           
    




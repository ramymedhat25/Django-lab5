from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from company.models import Employee, Team
from myapi.serializers import EmployeeSerializer, TeamSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["GET", "POST"]) 
def EmployeesFunBaseView(request):
    
    if request.method == 'GET':
        employees=Employee.objects.all() 
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data) 
    
    if request.method == 'POST':
        data=request.data 
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED)  
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
class EmployeesFunBaseView2(APIView):
    
    def get(self,request):
        employees=Employee.objects.all()   
        serializer=EmployeeSerializer(employees,many=True) 
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  
            employees=Employee.objects.all()
            all_data=EmployeeSerializer(serializer.data) 
            return Response({"employees":all_data.data},status=status.HTTP_201_CREATED) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        

class EmployeesFunBaseView3(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]  
    permission_classes = [IsAuthenticated]          
    serializer_class = EmployeeSerializer           
    queryset = Employee.objects.all()





@api_view(["GET", "POST"]) 
def TeamFunBaseView(request):
    
    if request.method == 'GET':
        team=Team.objects.all() 
        serializer=TeamSerializer(team,many=True) 
        return Response(serializer.data) 
    
    if request.method == 'POST':
        data=request.data 
        serializer=TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class TeamFunBaseView2(APIView):
    
    def get(self,request):
        team=Team.objects.all()   
        serializer=TeamSerializer(team,many=True) 
        return Response(serializer.data) 
    
    def post(self,request):
        data=request.data
        serializer=TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  
            team=Team.objects.all()
            all_data=TeamSerializer(serializer.data) 
            return Response({"employees":all_data.data},status=status.HTTP_201_CREATED) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        




class TeamFunBaseView3(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication] 
    permission_classes = [IsAuthenticated]         
    serializer_class = TeamSerializer              
    queryset = Team.objects.all()


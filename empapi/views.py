from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from empapi.serializer import EmpSerializer
from empapi.models import Emp

# Create your views here
class EmpView(ViewSet):

    def list(self,request,*args,**kwargs):
        qs=Emp.objects.all()
        serializer=EmpSerializer(qs,many=True)
        return Response(data=serializer.data)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Emp.objects.get(id=id)
        serializer=EmpSerializer(qs)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Emp.objects.get(id=id)
        qs.delete()
        return Response({'msg':'deleted..'})
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Emp.objects.get(id=id)
        serializer=EmpSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
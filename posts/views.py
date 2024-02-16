from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from serializer import *
from rest_framework.response import Response


# Create your views here.
class ReactView(APIView):
    def get(self, request):
        output= [{}]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=requests.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




from django.shortcuts import render
from cylinder.models import Parameter
from cylinder.serializers import ParameterSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.decorators import api_view
# from rest_framework.response import Response

# Create your views here.
class ParameterListCreate(generics.ListCreateAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer

def results(request, thickness):
    response = "the thickness is %s"
    print(response % thickness)
    return HttpResponse(response % thickness)

# @api_view(['GET', 'POST'])
def data(request):
    print('inside data')
    if request.method == 'POST':
        print(request.body)
        return HttpResponse('I am posting')
        # return HttpResponse({"message": "Got some data!", "data": request.body})
    # return HttpResponse({"message": "Hello, world!"})
    return HttpResponse("i am getting")

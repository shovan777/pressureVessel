from django.shortcuts import render
from cylinder.models import Parameter
from cylinder.serializers import ParameterSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.decorators import api_view
from cgi import parse_qs, escape
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from cylinder.utils import thickness_calc
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
@require_http_methods(['POST', 'GET'])
@csrf_exempt
def data(request):
    print('inside data')
    print(request.method)
    # print(request.body)
    param = request.body
    if request.method == 'POST':
        # print(request.body)
        print("I am calculating thickness")
        # thickness_calc.cylinder_t
        print(thickness_calc.cylinder_t(D=5.8, S=60, P=30.8))
        return HttpResponse('I am posting')
        # return HttpResponse({"message": "Got some data!", "data": request.body})
    # return HttpResponse({"message": "Hello, world!"})
    return HttpResponse("i am getting")

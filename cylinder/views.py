from django.shortcuts import render
from cylinder.models import Parameter
from cylinder.serializers import ParameterSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.decorators import api_view
from cgi import parse_qs, escape
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from cylinder.utils.thickness_calc import cylinder_t
from cylinder.models import Parameter
import json
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
    print(request)
    print(request.body)
    param_unicode = request.body.decode('utf-8')
    param = json.loads(param_unicode)
    print(param['material'])

    if request.method == 'POST':
        # get all attr for db query
        spec_num, type_grade = param['material'].split(' ')
        temp = param['temp1']
        row_dict = Parameter.objects.filter(
            spec_num = spec_num
        ).filter(
            type_grade = type_grade
        ).values()[0]

        # get max_tensile_strength
        max_stress = row_dict['max_stress_' + str(temp)]

        print("I am calculating thickness")
        P = int(param['ip'])
        S = max_stress
        D = int(param['sd'])
        C_A = int(param['ic'])
        thickness = cylinder_t(P, S, D, C_A)

        return HttpResponse(thickness)

    return HttpResponse("give me a POST")

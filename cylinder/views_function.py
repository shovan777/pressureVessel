# python imports
import json

# django imports
from django.http import HttpResponse, JsonResponse

# userdefined modules
from cylinder.models import Parameter
from cylinder.utils.thickness_calc import cylinder_t

# pip imports
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
# format keywork lets the view handle multiple content type responses
# def data(request, fromat=None)
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
            spec_num=spec_num
        ).filter(
            type_grade=type_grade
        ).values()[0]

        # get max_tensile_strength
        max_stress = row_dict['max_stress_' + str(temp)]

        print("I am calculating thickness")
        P = int(param['ip'])
        S = max_stress
        D = int(param['sd'])
        C_A = int(param['ic'])
        thickness = cylinder_t(P, S, D, C_A)
        print(thickness)

        return JsonResponse({'thickness': thickness})

    return JsonResponse({'error': 'Request is not POST'})

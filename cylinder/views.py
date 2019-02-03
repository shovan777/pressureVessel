# cylinder modules
from cylinder.models import Parameter
from cylinder.serializers import ParameterSerializer
from cylinder.utils.thickness_calc import cylinder_t


# django modules
from django.http import Http404, JsonResponse

# django-rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class ThicknessData(APIView):
    """
    Determine thickness for provided cylinder params
    """
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        data = request.data.get('cylinderParam', {})
        if data:
            try:
                row_dict = Parameter.objects.filter(
                    spec_num=data['spec_num']
                ).filter(
                    type_grade=data['type_grade']
                ).values()[0]
            except:
                raise Http404
            temp = data['temp1']
            max_stress = row_dict['max_stress_' + str(temp)]
            P = int(data['ip'])
            S = max_stress
            D = int(data['sd'])
            C_A = int(data['ic'])
            thickness = cylinder_t(P, S, D, C_A)

            return JsonResponse({'thickness': thickness})
            # use something like
            # return Response(data = {'thickness': thickness}, content_type='x-json')
        return Response(status=status.HTTP_400_BAD_REQUEST)
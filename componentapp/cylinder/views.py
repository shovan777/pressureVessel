# cylinder modules
from .models import Parameter
from .serializers import ParameterSerializer
from .utils.thickness_calc import cylinder_t


# django modules
from django.http import Http404, JsonResponse

# django-rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ThicknessData(APIView):
    """
    Determine thickness for provided cylinder params
    """
    # permission_classes = (IsAuthenticated,)
    serializer_classes = ParameterSerializer
    def post(self, request, format=None):

        data = request.data.get('cylinderParam', {})
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        a = Parameter.objects.get_thickness(data=serializer.data)
        
        print(a)
        # if data:
        #     try:
        #         row_dict = Parameter.objects.filter(
        #             spec_num=data['spec_num']
        #         ).filter(
        #             type_grade=data['type_grade']
        #         ).values()[0]
        #     except:
        #         raise Http404

        #     try:
        #         temp = data['temp1']
        #         max_stress = row_dict['max_stress_' + str(temp)]
        #         P = int(data['ip'])
        #         S = max_stress
        #         D = int(data['sd'])
        #         C_A = int(data['ic'])
        #     except:
        #         data_format = {
        #                             "cylinderParam": {
        #                                 "spec_num": "SA-516",
        #                                 "type_grade": "70",
        #                                 "temp1": "150",
        #                                 "ip": "40",
        #                                 "sd": "50"
        #                             }
        #                         }
        #         return Response(data = data_format, status=status.HTTP_400_BAD_REQUEST)
        #     thickness = cylinder_t(P, S, D, C_A)
        if (a):
            return JsonResponse({'thickness': a})
            # use something like
            # return Response(data = {'thickness': thickness}, content_type='x-json')
        return Response(status=status.HTTP_400_BAD_REQUEST)
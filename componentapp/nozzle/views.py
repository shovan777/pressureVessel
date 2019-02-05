# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.http import require_http_methods
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# @require_http_methods(['POST', 'GET'])
# @csrf_exempt
# def data(request):
#     """Calculate nozzle detail and weild sizing.

#     Parameters
#     ----------
#     request : type
#         Description of parameter `request`.

#     Returns
#     -------
#     t_c: float
#         minimum fillet weild throat dimension
#     r_1: float
#         minimum inside corner radius

#     """
#     if request.method == 'POST':
#         # GET THE VALUES FROM swain
#         cylinder_t = 0.625
#         nozzle_d = 10
#         nozzle_t = 0.5
#         C_A = 0.125

#         t_c = calculate_t_c(cylinder_t, nozzle_t, C_A)


from asme.models import PipingSchedule
from .serializers import NozzleSerializer
from .renderers import NozzleJSONRenderer
from .utils.calc import calculate_t_c

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException

from exceptionapp.exceptions import newError


class NozzleData(APIView):

    # permission_classes = (IsAuthenticated,)
    renderer_classes = (NozzleJSONRenderer,)
    serializer_classes = NozzleSerializer
    
    def post(self, request):
        data = request.data.get('nozzleParam',{})
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        data1 = serializer.data

        try:
            row_dict = PipingSchedule.objects.filter(schedules=data1.get('schedules')).values()[0]
        except:
            raise newError({
                "database":["Data cannot be found incorrect data"]
            })

        cylinder_t = 0.125
        nozzle_t = 0.125
        C_A = int(data1.get('ic'))

        thickness = calculate_t_c(cylinder_t,nozzle_t,C_A)
        print(thickness)
        newdict = {'thickness':thickness}
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)

from asme.models import NozzleData,PipingSchedule
from .serializers import NozzleSerializer
from .renderers import NozzleJSONRenderer
from .utils.calc import calculate_t_c

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException

from exceptionapp.exceptions import newError


class NozzleAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    renderer_classes = (NozzleJSONRenderer,)
    serializer_classes = NozzleSerializer
    
    def post(self, request):
        data = request.data.get('nozzleParam',{})
        data['projectID'] = request.data.get('projectID',None)
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        data1 = serializer.data

        try:
            row_dict_nozzle = NozzleData.objects.filter(class_value=data1.get('class_value')).filter(type_name=data1.get('type_name')).filter(nominal_pipe_size=data1.get('nominal_pipe_size')).values()[0]
            row_dict_pipe = PipingSchedule.objects.filter(schedules=data1.get('schedules')).filter(nominal_pipe_size=data1.get('nominal_pipe_size')).values()[0]
        except:
            raise newError({
                "database":["Data cannot be found incorrect data"]
            })

        # cylinder_t = 0.125
        # nozzle_t = 0.125
        # C_A = 0.13

        # thickness = calculate_t_c(cylinder_t,nozzle_t,C_A)
        # print(thickness)
        newdict = {}
        newdict.update(serializer.data)
        newdict.update(row_dict_nozzle)
        newdict.update(row_dict_pipe)
        return Response(newdict,status=status.HTTP_200_OK)

# cylinder modules
from asme.models import MaximumAllowableStress
from .serializers import HeadSerializer
from .renderers import HeadJSONRenderer
from .utils.thickness_calc import head_t

# django-rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from exceptionapp.exceptions import newError

class ThicknessData(APIView):
    """
    Determine thickness for provided cylinder params
    """
    # permission_classes = (IsAuthenticated,)
    serializer_classes = HeadSerializer
    renderer_classes = (HeadJSONRenderer,)
    def post(self, request, format=None):

        data = request.data.get('headParam', {})
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        
        data1 = serializer.data
        try:
            row_dict = MaximumAllowableStress.objects.filter(spec_num=data1.get('spec_num')).filter(type_grade=data1.get('type_grade')).values()[0]
        except:
            raise newError({
                "database":["Data cannot be found incorrect data"]
                })
        temp = data1.get('temp1')
        max_stress = row_dict['max_stress_' + str(temp)]
        P = int(data1.get('ip'))
        S = max_stress
        D = int(data1.get('sd'))
        C_A = int(data1.get('ic'))
        thickness = head_t(P, S, D, C_A)

        newdict = {'thickness':thickness}
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)

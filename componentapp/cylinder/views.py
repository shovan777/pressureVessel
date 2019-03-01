# cylinder modules
from asme.models import MaximumAllowableStress
from .serializers import ParameterSerializer
from .renderers import ParameterJSONRenderer
from .utils.thickness_calc import cylinder_t

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
    permission_classes = (IsAuthenticated,)
    serializer_classes = ParameterSerializer
    renderer_classes = (ParameterJSONRenderer,)
    def post(self, request, format=None):
        print(request.data)
        data = request.data.get('cylinderParam', {})
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
        max_stress = row_dict['max_stress_' + str(int(temp))]
        P = data1.get('ip')
        S = max_stress
        D = data1.get('sd')
        C_A = data1.get('ic')
        projectID = request.data['projectID']
        thickness = cylinder_t(P, S, D, C_A, projectID)

        newdict = {'thickness':thickness}
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)

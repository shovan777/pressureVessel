from asme.models import MaximumAllowableStress
from .serializers import ParameterSerializer
from .renderers import ParameterJSONRenderer
from .utils.skirtCalc import skirtCalculation,center_of_gravity

# django-rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from exceptionapp.exceptions import newError
from asme.utils.calculators import max_stress_calculator


class SkirtThicknessData(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_classes = ParameterSerializer
    renderer_classes = (ParameterJSONRenderer,)
    def post(self, request, format=None):
        data = request.data.get('skirtParam', {})
        data['projectID'] = request.data.get('projectID',None)
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        data1 = serializer.data
        try:
            row_dict = MaximumAllowableStress.objects.filter(spec_num=data1.get('spec_num')).filter(type_grade=data1.get('type_grade')).values()[0]
        except:
            raise newError({
                "database":["Data cannot be found incorrect data"]
            })

        max_stress = max_stress_calculator(row_dict, data1.get('temp1'))
        yield_strength = row_dict['min_yield_strength']
        # modulus of elasticity at design temp
        
        S = max_stress
        D = data1.get('sd')
        C_A = data1.get('ic')
        thickness = data1.get('thickness')
        length = data1.get('length')
        density = row_dict['density']
        projectID = data1.get('projectID')
        component_react_id = data1.get('componentID')

        thicknessResponse = skirtCalculation(D, thickness, C_A, S*1000, projectID, component_react_id)
        weightResponse = center_of_gravity(D,length+4,density,thickness-C_A)
        
        newdict = {
            'thicknessResponse':thicknessResponse,
            'weight':weightResponse
        }
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)

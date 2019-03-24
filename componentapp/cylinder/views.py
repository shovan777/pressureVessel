# cylinder modules
from asme.models import MaximumAllowableStress
from .serializers import ParameterSerializer,ParameterSerializerConical
from .renderers import ParameterJSONRenderer
from .utils.thickness_calc import cylinder_t,conical_t,center_of_gravity

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
        data = request.data.get('cylinderParam', {})
        data['projectID'] = request.data.get('projectID',None)
        # data['componentID'] = request.data.get('componentID',None)
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
        P = data1.get('ip')
        S = max_stress
        D = data1.get('sd')
        C_A = data1.get('ic')
        density = row_dict['density']
        projectID = data1.get('projectID')
        component_react_id = data1.get('componentID')
        thickness = cylinder_t(P, S, D, C_A, projectID, component_react_id)
        weightOfCylinder = center_of_gravity(D,48,density,60,thickness-C_A)
        newdict = {
            'thickness':thickness,
            'weight':weightOfCylinder[1],
            'weightTimesCG':weightOfCylinder[0]
        }
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)

class ThicknessDataConical(APIView):
    """
    Determine thickness for provided cylinder params
    """
    permission_classes = (IsAuthenticated,)
    serializer_classes = ParameterSerializerConical
    renderer_classes = (ParameterJSONRenderer,)
    def post(self, request, format=None):
        data = request.data.get('conicalParam', {})
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
        temp = data1.get('temp1')
        max_stress = row_dict['max_stress_' + str(temp)]
        P = data1.get('ip')
        S = max_stress
        D_l = data1.get('sd_l')
        D_s = data1.get('sd_s')
        L_c = data1.get('length')
        C_A = data1.get('ic')
        projectID = data1.get('projectID')
        thickness = conical_t(P,S,D_l,D_s,L_c,C_A,projectID)

        newdict = {'thickness':thickness}
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)

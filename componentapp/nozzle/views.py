from asme.models import NozzleData,PipingSchedule,MaximumAllowableStress
from .serializers import NozzleSerializer
from .renderers import NozzleJSONRenderer
from .utils.calc import calculate_t_c
from .utils.nozzlecalc import calculation_thick

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
            row_dict_stress = MaximumAllowableStress.objects.filter(spec_num=data1.get('spec_num')).filter(type_grade=data1.get('type_grade')).values()[0]
            # row_dict_pipe = PipingSchedule.objects.filter(schedules=data1.get('schedules')).filter(nominal_pipe_size=data1.get('nominal_pipe_size')).values()[0]
        except:
            raise newError({
                "database":["Data cannot be found incorrect data"]
            })


        designPressure = data1.get('designPressure')
        corrosionAllowance = data1.get('corrosionAllowance')

        temp = data1.get('temp1')
        shellAllowableStress = row_dict_stress['max_stress_' + str(temp)]
        
        yieldStrength = row_dict_stress['min_yield_strength']
        cylinderInsideDiameter = data1.get('cylinderDiameter')
        cylinderThickness = data1.get('cylinderThickness')
        # nozzleOutsideDiameter = data1.get('nozzleDiameter')
        nozzleThickness = row_dict_nozzle['neck_thickness']
        externalNozzleProjection = data1.get('externalNozzleProjection')
        internalNozzleProjection = data1.get('internalNozzleProjection')
        # print(yieldStrength,nozzleThickness,shellAllowableStress)
        nozzleOutsideDiameter = row_dict_nozzle['flange_outer_diameter']
        # nozzleThickness = 4.75
        nozzleAllowableStress = shellAllowableStress*1000
        reinforcingElementAllowableStress = shellAllowableStress*1000
        projectID = data1.get('projectID')
        component_react_id = data1.get('componentID')
        value = calculation_thick(designPressure,corrosionAllowance,shellAllowableStress*1000,yieldStrength*1000,cylinderInsideDiameter,cylinderThickness,nozzleOutsideDiameter,nozzleThickness,externalNozzleProjection,internalNozzleProjection,nozzleAllowableStress,reinforcingElementAllowableStress, projectID, component_react_id)

        newdict = {
            "areaAvailable": value[0],
            "areaRequired" : value[1],
            "areaResponse" : value[2]
        }
        newdict.update(serializer.data)
        newdict.update(row_dict_nozzle)
        # newdict.update(row_dict_pipe)
        return Response(newdict,status=status.HTTP_200_OK)

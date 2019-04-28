from asme.models import MaximumAllowableStress
from .serializers import ParameterSerializer
from .renderers import ParameterJSONRenderer
from .utils.saddleCalc import saddleCalc

# django-rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from exceptionapp.exceptions import newError
from asme.utils.calculators import max_stress_calculator

class SaddleResponse(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_classes = ParameterSerializer
    renderer_classes = (ParameterJSONRenderer,)
    def post(self, request, format=None):
        data = request.data.get('saddleParam',{})
        data['projectID'] = request.data.get('projectID',None)
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        data1 = serializer.data

        try:
            row_dict = MaximumAllowableStress.objects.filter(spec_num=data1.get('vessel_spec_num')).filter(type_grade=data1.get('vessel_type_grade')).values()[0]
        except:
            raise newError({
                "database":["Data cannot be found incorrect data"]
            })
        
        max_stress = max_stress_calculator(row_dict, data1.get('vessel_design_temperature'))
        vessel_yield_stress = row_dict['min_yield_strength']

        vessel_diameter = data1.get('vessel_diameter')
        vessel_thickness = data1.get('vessel_thickness')
        vessel_corrosion_allowance = data1.get('vessel_corrosion_allowance')
        vessel_head_height = data1.get('vessel_head_height')
        vessel_design_pressure = data1.get('vessel_design_pressure')
        weld_joint_effiency = data1.get('weld_joint_effiency') # need to be take from user
        length_of_vessel = data1.get('length_of_vessel')
        saddle_center_line_to_head = data1.get('saddle_center_line_to_head')
        saddle_contact_angle = data1.get('saddle_contact_angle')
        saddle_width = data1.get('saddle_width')
        total_vessel_weight = data1.get('total_vessel_weight')

        projectID = data1.get('projectID')
        component_react_id = data1.get('componentID')
        responses = saddleCalc(
            vessel_diameter=vessel_diameter,
            vessel_thickness=vessel_thickness,
            vessel_corrosion_allowance=vessel_corrosion_allowance,
            vessel_head_height=vessel_head_height,
            vessel_design_pressure=vessel_design_pressure,
            vessel_allowable_pressure=max_stress*1000,
            vessel_yield_stress=vessel_yield_stress*1000,
            weld_joint_effiency=weld_joint_effiency,
            length_of_vessel=length_of_vessel,
            saddle_center_line_to_head=saddle_center_line_to_head,
            saddle_contact_angle=saddle_contact_angle,
            saddle_width=saddle_width,
            total_vessel_weight=total_vessel_weight,
            report_id=projectID,
            component_react_id=component_react_id
        )

        newdict = {"responses":responses}
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)

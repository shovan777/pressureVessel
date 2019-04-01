from asme.models import MaximumAllowableStress
from .serializers import LiftingLugSerializer
from .renderers import LiftingLugJSONRenderer
from .utils.lug_calc import lug_calc

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException

from exceptionapp.exceptions import newError


class LiftingLugAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    renderer_classes = (LiftingLugJSONRenderer, )
    serializer_classes = LiftingLugSerializer

    def post(self, request):
        data = request.data.get('lugParam', {})
        # print(request.data)
        data['projectID'] = request.data.get('projectID', None)
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        data1 = serializer.data

        try:
            row_dict_stress = MaximumAllowableStress.objects.filter(spec_num=data1.get(
                'spec_num')).filter(type_grade=data1.get('type_grade')).values()[0]
        except:
            raise newError({
                "database": ["Data cannot be found incorrect data"]
            })

        # get from db ok
        tensile_stress = row_dict_stress['min_tensile_stress']
        # get other stress from db also
        # for now we put default values as in per compress report 18-001 pdf
        shear_stress = 13320 # in psi
        bearing_stress = 29970 # in psi
        bending_stress = 22201 # in psi
        weld_shear_stress = 13320 # in psi


        length = data1.get('length')
        height = data1.get('height')
        hole_diameter = data1.get('holeDiameter')
        thickness = data1.get('thickness')
        pin_diameter = data1.get('pinDiameter')
        load_eccentricity = data1.get('loadEccentricity')
        distance_load_to_shell = data1.get('distanceLoadToShell')
        normal_load_angle = data1.get('normalLoadAngle')
        vertical_load_angle = data1.get('verticalLoadAngle')
        weld_size = data1.get('weldSize')
        lug1_cg_distance = data1.get('lug1CgDistance')
        lug2_cg_distance = data1.get('lug2CgDistance')
        weight = data1.get('weight')
        projectID = data1.get('projectID')
        componentID = data1.get('componentID')
        calc_dict = lug_calc(
            L = length,
            H = height,
            t = thickness,
            d = hole_diameter,
            D_p = pin_diameter,
            a_1 = load_eccentricity,
            a_2 = distance_load_to_shell,
            beta = normal_load_angle,
            phi = vertical_load_angle,
            t_w = weld_size,
            x_1 = lug1_cg_distance,
            x_2 = lug2_cg_distance,
            sigma_t = tensile_stress,
            sigma_s = shear_stress,
            sigma_p = bearing_stress,
            sigma_b = bending_stress,
            tau_allowable = weld_shear_stress,
            W = weight
        )
        # add some code here

        #
        newdict = calc_dict
        newdict.update(serializer.data)
        return Response(newdict, status=status.HTTP_200_OK)

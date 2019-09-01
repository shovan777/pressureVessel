# rest framework modules
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# state modules
from .models import CylinderState, NozzleState, Report
from .serializers import CylinderStateSerializer, NozzleStateSerializer, ProjectIdSerializer

from reporter.models import Report

import json

from django.http import HttpResponse, JsonResponse

from pressureVessel import file_utils

class CylinderStateViewSet(viewsets.ModelViewSet):
    queryset = CylinderState.objects.all()
    serializer_class = CylinderStateSerializer


class NozzleStateViewSet(viewsets.ModelViewSet):
    queryset = NozzleState.objects.all()
    serializer_class = NozzleStateSerializer

# TODO handle error in data,projectID,componentID, database query is available or not
@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def schemaWrite(request):
    data = request.data['schema']

    serialization = ProjectIdSerializer(data=request.data)
    serialization.is_valid(raise_exception=True)
    projectID = serialization.data.get('projectID')

    report = Report.objects.get(id=projectID)
    state_path = report.location_state
    # read the file and add the component
    # with open(state_path, 'r') as file:
    #     json_data = json.load(file)
    #     json_data['components'].append(data)
    file_content = file_utils.read_file(state_path)
    file_content = file_content if file_content else json.dumps({
        'components': []
    })
    json_dict = json.loads(file_content)
    json_dict['components'].append(data)

    # write to file
    # with open(state_path, 'w') as file:
    #     json.dump(json_data, file)
    file_content = json.dumps(json_dict)
    file_utils.write_file(state_path, file_content)
    return HttpResponse('ok iam writing')


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def schemaUpdate(request):
    data = request.data['schema']
    array_id = data['componentID']

    serialization = ProjectIdSerializer(data=request.data)
    serialization.is_valid(raise_exception=True)
    projectID = serialization.data.get('projectID')

    report = Report.objects.get(id=projectID)
    state_path = report.location_state
    # read the file and update the component
    # with open(state_path, 'r') as file:
    #     json_data = json.load(file)
    #     json_data['components'][array_id] = data
    file_content = file_utils.read_file(state_path)
    json_dict = json.loads(file_content)
    json_dict['components'][array_id] = data


    # write to file
    # with open(state_path, 'w') as file:
    #     json.dump(json_data, file)
    file_content = json.dumps(json_dict)
    file_utils.write_file(state_path, file_content)
    return HttpResponse('ok iam writing')


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def schemaDelete(request):
    # print('**************')
    # print(request.data['schema']['componentID'])
    data = request.data['schema']
    array_id = data['componentID']

    serialization = ProjectIdSerializer(data=request.data)
    serialization.is_valid(raise_exception=True)
    projectID = serialization.data.get('projectID')

    report = Report.objects.get(id=projectID)

    # delete the component with ComponentID
    _ = report.component_set.all().filter(react_component_id=array_id).delete()
    state_path = report.location_state
    # read the file and update the component
    # with open(state_path, 'r') as file:
    #     json_data = json.load(file)
    #     array = json_data['components']
    #     for i in range(len(array)):
    #         if array[i] != {}:
    #             # print(array[i])
    #             if int(array[i]['componentID']) == int(array_id):
    #                 json_data['components'][i]={}
    #                 break
    file_content = file_utils.read_file(state_path)
    json_data = json.loads(file_content)
    array = json_data['components']
    for i in range(len(array)):
        if array[i] != {}:
            # print(array[i])
            if int(array[i]['componentID']) == int(array_id):
                json_data['components'][i]={}
                break

    # write to file
    # with open(state_path, 'w') as file:
    #     json.dump(json_data, file)
    file_content = json.dumps(json_data)
    file_utils.write_file(state_path, file_content)
    return HttpResponse('deleted')


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated, ))
def schemaOpen(request):
    # print('**********')
    # print(request.data)
    # print(request.GET.get('projectID'))
    # print(request.params)
    # print('************')

    serialization = ProjectIdSerializer(data=request.GET)
    serialization.is_valid(raise_exception=True)
    projectID = serialization.data.get('projectID')

    # projectID = request.GET.get('projectID')
    report = Report.objects.get(id=projectID)
    state_path = report.location_state
    # data = request.data['schema']
    # read the file and send the json response
    # with open(state_path, 'r') as file:
    #     json_data = json.load(file)
    file_content = file_utils.read_file(state_path)
    json_dict = json.loads(file_content)

    return JsonResponse(json_dict)

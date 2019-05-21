# rest framework modules
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, serializer_class
from rest_framework import permissions

# state modules
from .models import CylinderState, NozzleState, Report
from .serializers import CylinderStateSerializer, NozzleStateSerializer, ProjectIdSerializer

from reporter.models import Report

import json

from django.http import HttpResponse, JsonResponse


class CylinderStateViewSet(viewsets.ModelViewSet):
    queryset = CylinderState.objects.all()
    serializer_class = CylinderStateSerializer


class NozzleStateViewSet(viewsets.ModelViewSet):
    queryset = NozzleState.objects.all()
    serializer_class = NozzleStateSerializer

# TODO handle error in data,projectID,componentID, database query is available or not
@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
# @serializer_class(ProjectIdSerializer)
def schemaWrite(request):
    # print(request.data)
    data = request.data['schema']
    projectID = request.data['projectID']
    # serializer_class()
    report = Report.objects.get(id=projectID)
    state_path = report.location_state
    # read the file and add the component
    with open(state_path, 'r') as file:
        json_data = json.load(file)
        json_data['components'].append(data)

    # write to file
    with open(state_path, 'w') as file:
        json.dump(json_data, file)
    return HttpResponse('ok iam writing')


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def schemaUpdate(request):
    data = request.data['schema']
    array_id = data['componentID']
    projectID = request.data['projectID']
    report = Report.objects.get(id=projectID)
    state_path = report.location_state
    # read the file and update the component
    with open(state_path, 'r') as file:
        json_data = json.load(file)
        json_data['components'][array_id] = data

    # write to file
    with open(state_path, 'w') as file:
        json.dump(json_data, file)
    return HttpResponse('ok iam writing')


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def schemaDelete(request):
    # print('**************')
    # print(request.data['schema']['componentID'])
    data = request.data['schema']
    array_id = data['componentID']
    projectID = request.data['projectID']
    report = Report.objects.get(id=projectID)

    # delete the component with ComponentID
    _ = report.component_set.all().filter(react_component_id=array_id).delete()
    state_path = report.location_state
    # read the file and update the component
    with open(state_path, 'r') as file:
        json_data = json.load(file)
        array = json_data['components']
        for i in range(len(array)):
            if array[i] != {}:
                # print(array[i])
                if int(array[i]['componentID']) == int(array_id):
                    json_data['components'][i]={}
                    break

    # write to file
    with open(state_path, 'w') as file:
        json.dump(json_data, file)
    return HttpResponse('deleted')


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated, ))
def schemaOpen(request):
    print('**********')
    # print(request.data)
    print(request.GET.get('projectID'))
    # print(request.params)
    print('************')
    projectID = request.GET.get('projectID')
    report = Report.objects.get(id=projectID)
    state_path = report.location_state
    # data = request.data['schema']
    # read the file and send the json response
    with open(state_path, 'r') as file:
        json_data = json.load(file)

    return JsonResponse(json_data)

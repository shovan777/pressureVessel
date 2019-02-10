# django modules
from django.http import HttpResponse, Http404
from django.template import loader

# rest framework modules
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

# component modules
from componentapp.cylinder.models import Parameter

# weasyprint = pdf gen library modules
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

# reporter modules
from .models import CylinderState, NozzleState, Report
from reporter.serializers import CylinderStateSerializer, NozzleStateSerializer, ReportSerializer


# def index(request):
#     # return HttpResponse("Hello, world. You're at the reporter index.")
#     material_list = Parameter.objects.all()
#     output = 'Calcgen REport\n'+ ', '.join([p.spec_num for p in material_list])
#     return HttpResponse(output)
html_out = None
# templating index page
def index(request):
    material_list = Parameter.objects.all()
    template = loader.get_template('reporter/index.html')
    list_array = [p.spec_num for p in material_list]
    context = {
        'title': 'Calcgen Reports',
        'material_spec_num': list_array[0],
    }
    html_out = template.render(context, request)
    css = CSS(filename='static/reporter/typography.css')
    # print(request.build_absolute_uri())
    html = HTML(string=html_out,base_url=request.build_absolute_uri())
    html.write_pdf('gen_reports/report1.pdf', stylesheets=[css])
    html.write_pdf()

    return HttpResponse(html_out)

# class ReportViewSet(viewsets.ModelViewSet):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer

# class CylinderStateViewSet(viewsets.ModelViewSet):
#     queryset = CylinderState.objects.all()
#     serializer_class = CylinderStateSerializer

# class NozzleStateViewSet(viewsets.ModelViewSet):
#     queryset = NozzleState.objects.all()
#     serializer_class = NozzleStateSerializer
class ReportList(APIView):
    """
    List all report, or create a new report.
    """
    def get(self, request, format=None):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportDetail(APIView):
    """
    Retrieve, update or delete a report.
    """
    def get_report(self, pk):
        try:
            print(pk)
            return Report.objects.get(pk=pk)
        except Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        report = self.get_report(pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        report = self.get_report(pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        report = self.get_report(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
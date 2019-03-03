# django modules
from django.http import HttpResponse, Http404, FileResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage, Storage
from django.core.files import File
from pressureVessel import settings


# rest framework modules
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse

# component modules
from asme.models import MaximumAllowableStress

# weasyprint = pdf gen library modules
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

# pandas - data manipulator
import pandas as pd
import io

# reporter modules
from .models import CylinderState, NozzleState, Report
from reporter.serializers import CylinderStateSerializer, NozzleStateSerializer, ReportSerializer

# def index(request):
#     # return HttpResponse("Hello, world. You're at the reporter index.")
#     material_list = Parameter.objects.all()
#     output = 'Calcgen REport\n'+ ', '.join([p.spec_num for p in material_list])
#     return HttpResponse(output)
# templating index page
# @permission_classes(permissions.IsAuthenticatedOrReadOnly,)
def csv_loader(filename):
    try:
        df = pd.read_csv(filename, skiprows=1)
        # print(df)
        return df.to_html()
    except Exception as e:
        print(str(e))


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def index(request):
    # print(request.data)
    material_list = MaximumAllowableStress.objects.all()
    template = loader.get_template('reporter/vessel2.html')
    # header_tempalate = loader.get_template('')
    list_array = [p.spec_num for p in material_list]
    info_table_path = 'static/reporter/csv/'
    info_tables = {
        'area': csv_loader(info_table_path + 'area.csv'),
        'temp': csv_loader(info_table_path + 'temp.csv'),
        'angle': csv_loader(info_table_path + 'angle.csv'),
        'distance': csv_loader(info_table_path + 'distance.csv'),
        'frequency': csv_loader(info_table_path + 'frequency.csv'),
        'max': csv_loader(info_table_path + 'max.csv'),
        'pipe': csv_loader(info_table_path + 'pipe.csv'),
        'pressure': csv_loader(info_table_path + 'pressure.csv'),
        'weight': csv_loader(info_table_path + 'weight.csv'),
        'speed': csv_loader(info_table_path + 'speed.csv'),
        'volume': csv_loader(info_table_path + 'volume.csv')
    }
    # get this variable from request ok
    # projectID = '87'
    projectID = request.data['projectID']
    print(projectID)
    cylinder_params = CylinderState.objects.filter(report__id=projectID).values()
    # print(infoTables['area'])
    context = {
        'title': 'Calcgen Reports',
        'material_spec_num': list_array[0],
        'author': request.user.username if request.user.username else 'Shovan Raj Shrestha',
        # 'projectID': request.data['projectID'],
        'projectID': projectID,
        # bring out createdat from report table
        'createdAt': '2019-02-21',
        'infoTables': info_tables,
        'cylinderParams': cylinder_params
    }
    # print(Report.objects.get(id=87))
    html_out = template.render(context, request)
    google_css = CSS(filename='static/reporter/google2.css')
    typo_css = CSS(filename='static/reporter/typography.css')
    # print(css)
    # print(request.build_absolute_uri())
    html = HTML(string=html_out,base_url=request.build_absolute_uri())
    html.write_pdf(settings.MEDIA_ROOT+'report3.pdf', stylesheets=[google_css, typo_css])
    # pdf = html.write_pdf(stylesheets=[google_css, typo_css])
    # fs = FileSystemStorage(location=str(Report.objects.get(id=87))[:-10])
    # fs.save(content='hello', name='report.pdf')
    # with open(str(Report.objects.get(id=87)), 'w') as f:
    #     # pdf_file = File(f)
    #     # pdf_file.write(pdf)
    #     html.write_pdf(f, stylesheets=[google_css, typo_css])    # f.closed
    # with open('gen_reports/report3.pdf', 'rb') as f:
    #     # html.write_pdf(stylesheets=[google_css, typo_css])
    #     # File
    #     pdf_file = File(f)
    #     # return pdf_file.url
    #     response = HttpResponse(pdf_file, content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment;filename=report.pdf'
    #     # print(dict(response))
    #     return response
    # file = Storage()
    # file = file.open('gen_reports/report3.pdf')
    # print(file.url())
    # buffer = io.BytesIO()
    # pdf = html.write_pdf(buffer, stylesheets=[google_css, typo_css])
    # return FileResponse(buffer, as_attachment=True, filename='report.pdf')

    # html.write_pdf()
    # response = HttpResponse(pdf, content_type='application/blob')
    # response['Content-Disposition'] = 'attachment;filename=report.pdf'
    # return response
    print(settings.MEDIA_URL)
    report_url = settings.MEDIA_URL+'report3.pdf'
    return HttpResponse(report_url)

class ReportViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username if self.request.user.username else 'Shovan Shrestha')
        # serializer.save(author='calcgen')
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #  use @action to handle custom endpoints of GET requests
    #  use @method to handle custom endpoints of POST requests
class CylinderStateViewSet(viewsets.ModelViewSet):
    queryset = CylinderState.objects.all()
    serializer_class = CylinderStateSerializer

class NozzleStateViewSet(viewsets.ModelViewSet):
    queryset = NozzleState.objects.all()
    serializer_class = NozzleStateSerializer

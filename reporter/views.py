# django modules
from django.http import HttpResponse, Http404
from django.template import loader

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
# @permission_classes(permissions.IsAuthenticatedOrReadOnly,)
def index(request):
    material_list = MaximumAllowableStress.objects.all()
    template = loader.get_template('reporter/index.html')
    list_array = [p.spec_num for p in material_list]
    context = {
        'title': 'Calcgen Reports',
        'material_spec_num': list_array[0],
        'author': request.user.username
    }
    html_out = template.render(context, request)
    css = CSS(filename='static/reporter/typography.css')
    # print(request.build_absolute_uri())
    html = HTML(string=html_out,base_url=request.build_absolute_uri())
    html.write_pdf('gen_reports/report1.pdf', stylesheets=[css])
    html.write_pdf()

    return HttpResponse(html_out)

class ReportViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    # def perform_create(self, serializer):
    #     # serializer.save(author=self.request.user)
    #     serializer.save(author='calcgen')

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #  use @action to handle custom endpoints of GET requests
    #  use @method to handle custom endpoints of POST requests
class CylinderStateViewSet(viewsets.ModelViewSet):
    queryset = CylinderState.objects.all()
    serializer_class = CylinderStateSerializer

class NozzleStateViewSet(viewsets.ModelViewSet):
    queryset = NozzleState.objects.all()
    serializer_class = NozzleStateSerializer

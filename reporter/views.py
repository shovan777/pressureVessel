from django.http import HttpResponse
from django.template import loader
from componentapp.cylinder.models import Parameter
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
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
# default modules
import io
import json
import os

# django modules
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage, Storage
from django.core.files import File
from django.shortcuts import render


# rest framework modules
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions, renderers
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.reverse import reverse

# component modules
from asme.models import MaximumAllowableStress

# weasyprint = pdf gen library modules
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

# pandas - data manipulator
import pandas as pd


from pressureVessel import settings, file_utils

# reporter modules
from .models import Report
from reporter.serializers import ReportSerializer, ReportInputSerializer

# userapp modules
from userapp.models import User

from exceptionapp.exceptions import newError

# state modules
from state.models import CylinderState, NozzleState, HeadState, SkirtState, LiftingLugState

# drawing modules
# from drawing.drawing import PyGame
from drawing.drawingcopy import DrawingClass

# matplotlib modules
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import datetime
from django.core.files.storage import default_storage

# def index(request):
#     # return HttpResponse("Hello, world. You're at the reporter index.")
#     material_list = Parameter.objects.all()
#     output = 'Calcgen REport\n'+ ', '.join([p.spec_num for p in material_list])
#     return HttpResponse(output)
# templating index page
# @permission_classes(permissions.IsAuthenticatedOrReadOnly,)


def csv_loader(filename):
    try:
        file_bytes = file_utils.read_file(filename)
        file_buf = BytesIO(file_bytes)
        df = pd.read_csv(file_buf, skiprows=1)
        file_buf.close()
        # print(df)
        return df.to_html()
    except Exception as e:
        print(str(e))


def get_page_body(boxes):
    for box in boxes:
        if box.element_tag == 'body':
            return box

        return get_page_body(box.all_children())


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def index(request):
    # print(request.data)
    font_config = FontConfiguration()
    material_list = MaximumAllowableStress.objects.all()
    template = loader.get_template('reporter/vessel2.html')
    # header_tempalate = loader.get_template('')
    list_array = [p.spec_num for p in material_list]
    info_table_path = os.path.join(settings.STATIC_ROOT, 'reporter/csv/')
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
    # projectID = 1344
    # projectID = 1442
    projectID = request.data['projectID']

    # all queries from db here
    cylinder_qset = CylinderState.objects.filter(
        report__id=projectID)
    nozzle_qset = NozzleState.objects.filter(
        report__id=projectID)
    head_qset = HeadState.objects.filter(
        report__id=projectID)
    skirt_qset = SkirtState.objects.filter(
        report__id=projectID)
    lug_qset = LiftingLugState.objects.filter(
        report__id=projectID)

    # print(projectID)
    cylinder_params = cylinder_qset.values()
    nozzle_params = nozzle_qset.values()
    head_params = head_qset.values()
    skirt_params = skirt_qset.values()
    lug_params = lug_qset.values()

    # get names and id of the components
    cylinder_id_name = [{'id': n.component.react_component_id,
                         'name': n.component.name} for n in cylinder_qset]
    nozzle_id_name = [{'id': n.component.react_component_id,
                       'name': n.component.name} for n in nozzle_qset]
    head_id_name = [{'id': n.component.react_component_id,
                     'name': n.component.name} for n in head_qset]
    skirt_id_name = [{'id': n.component.react_component_id,
                      'name': n.component.name} for n in skirt_qset]
    lug_id_name = [{'id': n.component.react_component_id,
                    'name': n.component.name} for n in lug_qset]

    ########################### FOR DRAWING PURPOSE ONLY ########
    # read the file
    # string json content
    # convert json to python object
    report = Report.objects.get(id=projectID)
    project_name = report.projectName
    state_path = report.location_state
    report_path = report.location
    state_data = file_utils.read_file(state_path)
    main_data = json.loads(state_data)
    # file_obj = default_storage.open('abc.png', 'wb')
    # file_name_svg = settings.MEDIA_ROOT + 'images/'+main_data.get('projectName') + "_" +str(main_data.get("projectID"))

    # make the folder to store 2D image
    if settings.PRODUCTION:
        file_utils.create_file(report_path, 'jpt')
    else:
        print('*************')
        print("I am in local")
        print(report_path)
        file_utils.create_file(report_path, 'abc')

    with default_storage.open(os.path.join(os.path.dirname(report_path),'abc.png'), 'wb') as file:
        dra = DrawingClass(fileName=file, drawing_scale_factor=1,
                        type=main_data.get('orientation'))

        if main_data.get('orientation') == 'horizontal':
            print("i am here")
            starting_y = 600
            main_array, length_of_left_head, length_of_right_head, total_length = dra.arrange_data(
                main_data)
            dra.draw_main_horizontal(data=main_array,
                                    starting_x=length_of_left_head+10,
                                    starting_y=starting_y,
                                    total_length=total_length,
                                    length_of_left_head=length_of_left_head,
                                    length_of_right_head=length_of_right_head
                                    )

        elif main_data.get('orientation') == 'vertical':
            print("i am not avaliable")
            starting_x = 600
            main_array, length_of_bottom_head, length_of_top_head, total_length = dra.arrange_data(
                main_data)
            dra.draw_main_vertical(data=main_array,
                                starting_x=starting_x,
                                starting_y=length_of_top_head + 10,
                                total_length=total_length,
                                length_of_top_head=length_of_top_head,
                                length_of_bottom_head=length_of_bottom_head
                                )
    # closing the file object

    # ############################ DRAWING PURPOSE END ##############

    # # cylinder_img_path = pygame.do_task(settings.MEDIA_ROOT + 'images/')
    # cylinder_img_path = settings.MEDIA_ROOT + 'images/' + \
    #     main_data.get('projectName') + "_" + \
    #     str(main_data.get("projectID"))+".png"
    # print(cylinder_img_path)
    cylinder_img_path = os.path.join(os.path.dirname(report_path), 'abc.png')
    # fig = plt.figure()
    img_in_memory = io.BytesIO()
    img_bytes = io.BytesIO(file_utils.read_file(cylinder_img_path))
    # print(img_bytes.read())
    # img = plt.imread(cylinder_img_path)
    # plt.imshow(img, interpolation='bicubic')
    # plt.xticks([]), plt.yticks([])

    def display_image_in_actual_size(img_bytes, img_in_memory):
        dpi = 1000
        # im_buff = plt.read
        im_data = plt.imread(img_bytes)
        height, width, depth = im_data.shape

        # What size does the figure need to be in inches to fit the image?
        figsize = width / float(dpi), height / float(dpi)

        # Create a figure of the right size with one axes that takes up the
    #   full figure
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1])

        # Hide spines, ticks, etc.
        ax.axis('off')

        # Display the image.
        ax.imshow(im_data, cmap='gray')

        plt.savefig(img_in_memory, format='png')
    display_image_in_actual_size(img_bytes, img_in_memory)
    plt.savefig(img_in_memory, format='png')
    print('****************')
    # print(img_in_memory.getvalue())
    image = base64.b64encode(img_in_memory.getvalue())
    # image = base64.b64encode(img)
    image = image.decode('utf-8')
    # image=str(image)
    # print(image)
    today = datetime.datetime.today()
    context = {
        'projectName': project_name,
        'title': 'Pressure Vessel Analysis Report',
        'material_spec_num': list_array[0],
        'author': request.user.username if request.user.username else 'Shovan Raj Shrestha',
        # 'projectID': request.data['projectID'],
        'projectID': projectID,
        # bring out createdat from report table
        'createdAt': '{}-{}-{}'.format(today.year, today.month, today.day),
        'infoTables': info_tables,
        'image': image,
        'cylinderParams': cylinder_params,
        'nozzleParams': nozzle_params,
        'headParams': head_params,
        'skirtParams': skirt_params,
        'lugParams': lug_params,
        'nozzleZip': zip(nozzle_params, nozzle_id_name)
    }
    # print(Report.objects.get(id=87))
    html_out = template.render(context, request)
    file_bytes = file_utils.read_file(os.path.join(
        settings.STATIC_ROOT, 'reporter/vessel.css'))
    file_buf = BytesIO(file_bytes)
    vessel_css = CSS(file_buf)
    file_buf.close()
    file_bytes = file_utils.read_file(os.path.join(
        settings.STATIC_ROOT, 'reporter/bootstrap.min.css'))
    file_buf = BytesIO(file_bytes)
    bootstrap_css = CSS(file_buf)
    file_buf.close()
    # print(css)
    # print(request.build_absolute_uri())

    # this code is added new report generation
    html_template = loader.get_template('reporter/vessel2.html')
    header_template = loader.get_template('reporter/header.html')

    html_out = html_template.render(context, request)
    html_header = header_template.render(context, request)

    pdf_header = HTML(string=html_header,
                      base_url=request.build_absolute_uri())

    pdf = HTML(string=html_out, base_url=request.build_absolute_uri())

    header = pdf_header.render(stylesheets=[
                               vessel_css, bootstrap_css], presentational_hints=True, font_config=font_config)
    doc = pdf.render(stylesheets=[vessel_css, bootstrap_css],
                     presentational_hints=True, font_config=font_config)

    exists_links = False
    print(header.pages)
    header_page = header.pages[0]
    exists_links = exists_links or header_page.links
    header_body = get_page_body(header_page._page_box.all_children())
    header_body = header_body.copy_with_children(header_body.all_children())

    # Insert header and footer in main doc
    for i, page in enumerate(doc.pages):
        # if not i:
        #     continue

        page_body = get_page_body(page._page_box.all_children())

        page_body.children += header_body.all_children()

        if exists_links:
            page.links.extend(header_page.links)

    pdf_file = doc
    if settings.PRODUCTION:
        pdf = pdf_file.write_pdf()
        file_utils.create_file(report_path, pdf)
    else:
        print('*************')
        print("I am in local")
        print(report_path)
        file_utils.create_file(report_path, 'abc')
        pdf_file.write_pdf(report_path)
    # pdf_file = pdf.write_pdf(
    #     stylesheets=[vessel_css, bootstrap_css], presentational_hints=True,font_config=font_config)

    # this code is added new report generation

    # html = HTML(string=html_out, base_url=request.build_absolute_uri())
    # if settings.PRODUCTION:
    #     pdf = html.write_pdf(stylesheets=[google_css, typo_css])
    #     file_utils.create_file(report_path, pdf)
    # else:
    #     html.write_pdf(report_path,
    #                stylesheets=[google_css, typo_css])
    # pdf= ''
    # pdf = base64.decode(pdf)

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
    # print(settings.MEDIA_URL)
    '''
    page viewed to solve problem
    https://stackoverflow.com/questions/48287623/pythonconversion-of-pdf-to-blob-and-back-to-pdf-leads-to-corrupt
    '''
    if settings.PRODUCTION:
        file_content = file_utils.read_file(report_path)
        blob = base64.b64encode(file_content)
        response = HttpResponse(blob, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=report.pdf'
        return response
    else:
        with open(report_path, 'rb') as file_content:
            blob = base64.b64encode(file_content.read())
            response = HttpResponse(blob, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=report.pdf'
            return response

    # report_url = settings.MEDIA_URL+'report3.pdf'
    # return HttpResponse(report_url)
    # return HttpResponse(html_out)


class ReportViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    # renderer_classes = (renderers.JSONRenderer, )
    serializerClass = ReportInputSerializer

    # override the create action
    def create(self, *args, **kwargs):
        serializers = self.serializerClass(data=self.request.data)
        serializers.is_valid(raise_exception=True)
        data1 = serializers.data

        # write a schema file
        data = {
            'createdBy': self.request.user.username,
            'projectName': data1['projectName'],
            'components': []
        }

        # get the user
        username = self.request.user.username
        # save the default queryset
        temp_query = self.queryset
        # filter the queryset to get querys where given projectName exists
        name_exists = temp_query.filter(author=username).filter(
            projectName=data['projectName'])
        if name_exists:
            raise newError({
                'msg': 'The project name already exists.'
            })

        response = super(ReportViewSet, self).create(*args, **kwargs)

        report_id = response.data['id']
        vessel_orientation = response.data['orientation']

        data['orientation'] = vessel_orientation
        data['projectID'] = report_id

        state_path = str(response.data['location_state'])
        # folder = os.path.split(state_path)[0]
        # os.makedirs(folder)
        file_content = json.dumps(data)
        try:
            file_utils.create_file(state_path, file_content)
        except Exception as error:
            raise error

        # with open(state_path, 'w') as file:
        #     json.dump(data, file)

        return response

    # override the list action
    def list(self, *args, **kwargs):
        username = self.request.user.username
        # print('****************')
        # print(username)
        temp_query = self.queryset
        self.queryset = self.queryset.filter(author=username)
        # print(self.queryset)
        response = super(ReportViewSet, self).list(*args, **kwargs)
        self.queryset = temp_query
        return response

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def project(self, request, *args, **kwargs):
        report = self.get_object()
        # cylinder_params = report.cylinderstate_set.all()
        # cylinder_params = cylinder_params.values()
        report_params = {
            'cylinder_params': list(report.cylinderstate_set.all().values()),
            'nozzle_params': list(report.nozzlestate_set.all().values()),
            'head_params': list(report.headstate_set.all().values()),
            'skirt_params': list(report.skirtstate_set.all().values()),
            'lug_params': list(report.liftinglugstate_set.all().values())
        }
        # print(report.cylinderstate_set.all()[0].id)
        # return JsonResponse(list(cylinder_params), safe=False)
        return JsonResponse(report_params)

    def perform_create(self, serializer):
        # print('*****************')
        # print(self.request.user.username)
        serializer.save(
            author=self.request.user.username if self.request.user.username else 'Shovan Shrestha')
        # serializer.save(author='calcgen')
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #  use @action to handle custom endpoints of GET requests
    #  use @method to handle custom endpoints of POST requests

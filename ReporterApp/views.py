# django modules
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage, Storage
from django.core.files import File
from django.shortcuts import render
from django.views.generic import *


from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse
from django.conf import settings
from weasyprint.fonts import FontConfiguration


class GeneratePdf(TemplateView):
    template_name = "reporter/vessel2.html"


def get_page_body(boxes):
    for box in boxes:
        if box.element_tag == 'body':
            return box

        return get_page_body(box.all_children())

def PdfGeneration(request):
    font_config = FontConfiguration()
    html_template = get_template('reporter/vessel2.html')
    header_template = get_template('reporter/header.html')

    
    context = {
        'allblogs': [
            {
                'title': 'pramod',
                'id': '123'
            }]
    }
    vessel_css = CSS(filename='static/reporter/vessel.css')
    bootstrap_css = CSS(filename='static/reporter/bootstrap.min.css')

    html_out = html_template.render(context, request)
    html_header = header_template.render({}, request)

    pdf_header = HTML(string=html_header, base_url=request.build_absolute_uri())

    pdf = HTML(string=html_out, base_url=request.build_absolute_uri())


    header = pdf_header.render(stylesheets=[vessel_css, bootstrap_css], presentational_hints=True,font_config=font_config)
    doc = pdf.render(stylesheets=[vessel_css, bootstrap_css], presentational_hints=True,font_config=font_config)
    
    
    
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
    
    
    
    
    pdf_file = doc.write_pdf()
    # pdf_file = pdf.write_pdf(
    #     stylesheets=[vessel_css, bootstrap_css], presentational_hints=True,font_config=font_config)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename=home_page.pdf'

    # html = HTML(string=html_out)
    # html = HTML(string=html_out, base_url=request.build_absolute_uri())

    # google_css = CSS(filename='static/reporter/google2.css')
    # HTML(string=html_out, base_url=request.build_absolute_uri())
    # pdf = html.write_pdf(stylesheets=[CSS(
    #     settings.STATIC_ROOT + '/css/vessel.css')], presentational_hints=True)
    # typo_css = CSS(filename='static/reporter/vessel.css')
    # # print(css)
    # # print(request.build_absolute_uri())
    # html = HTML(string=html_out, base_url=request.build_absolute_uri())
    # html.write_pdf(settings.MEDIA_ROOT+'report3.pdf',
    #                stylesheets=[google_css, typo_css])
    # google_css = CSS(filename='static/css/google2.css')
    # typo_css = CSS(filename='static/css/typography.css')
    # html = HTML(string=html_out, base_url=request.build_absolute_uri())
    # html.write_pdf(settings.MEDIA_ROOT+'report3.pdf',
    #                stylesheets=[google_css, typo_css])
    # return response
    print('***********')
    print(doc.pages)
    return response
    # return HttpResponse(html_out)


# def url_fetcher(url):
#     if url.startswith('assets://'):
#         url = url[len('assets://'):]
#         url = "file://" + safe_join(settings.ASSETS_ROOT, url)  
#     return weasyprint.default_url_fetcher(url)
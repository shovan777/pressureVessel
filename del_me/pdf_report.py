from pdf_reports import pug_to_html, write_report
html = pug_to_html("template.pug", title="My report")
write_report(html, "example.pdf")

from pdf_reports import pug_to_html, write_report
# import matplotlib.pyplot as plt
# img = plt.imread('logo.png')
html = pug_to_html("template.pug", title="My report", img='logo.png')
write_report(html, "example_me.pdf")

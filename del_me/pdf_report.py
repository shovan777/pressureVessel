from pdf_reports import pug_to_html, write_report
import matplotlib.pyplot as plt
import pandas as pd
# img = plt.imread('logo.png')
df = pd.DataFrame.from_records({
    "Name": ["Anna", "Bob", "Claire", "Denis"],
    "Age": [12,22,33,44],
    "Height (cm)": [140, 175, 173, 185]
}, columns=["Name", "Age", "Height (cm)"])
print(df)
html = pug_to_html("template.pug", title="Vessel Report", dataframe=df, img="/home/calcgen2/pressureVessel/del_me/logo.png")
write_report(html, "example_me.pdf")

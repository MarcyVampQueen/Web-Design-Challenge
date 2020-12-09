import pandas as pd
import os

path = os.path.join(os.path.dirname(__file__), 'clean_data.csv')
data = pd.read_csv(path)

html = data.to_html()
writeOut = open("resources/tables.html","w")
writeOut.write(html)
writeOut.close()
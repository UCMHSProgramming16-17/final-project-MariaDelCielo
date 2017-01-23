#import programs needed
import csv
import pandas as pd
import numpy as np
import bokeh
#make the csv file readable
df = pd.read_csv('PokemonData.csv')

#import type of graph needed from bokeh
from bokeh.charts import Donut, output_file, save
#import colors 
from bokeh.palettes import plasma
#create parameters and graph
PokemonPG = Donut(df, label='Type 1', values='#', text_font_size='8pt', hover_text = "#", palette=plasma(18), title = "Amount of Types of Pokemon")
#print file
output_file("PokemonPG.html")
#save the file
save(PokemonPG)
#import programs needed 
import csv
import pandas as pd
import numpy as np
import bokeh
#make the csv file readable 
df = pd.read_csv('PokemonData.csv')

#import type of graph needed from bokeh
from bokeh.charts import BoxPlot, output_file, save
#Create parameters and graph
PokemonBWG = BoxPlot(df, "Type 1", values = 'Sp. Atk', title = 'Pokemon Types, grouped by Attack Speeds', xlabel = 'Type of Pokemon', ylabel='Speeds')
#print the file 
output_file("PokemonBWG.html")
#save the file 
save(PokemonBWG)
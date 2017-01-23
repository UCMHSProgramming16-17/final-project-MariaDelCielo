#import programs needed
import csv
import pandas as pd
import numpy as np
import bokeh
#make the csv file readable
df = pd.read_csv('PokemonData.csv')

#import type of graph needed from bokeh
from bokeh.charts import Bar, output_file, save
#Create parameters and chart 
PokemonBG = Bar(df, 'Type 1', values = 'Speed', title = "Speed of Types of Pokemon",xlabel="Type of Pokemon", ylabel='Speeds', color = "blue")  
#print the file
output_file('PokemonBG.html')
#save the file 
save(PokemonBG)
import csv
import pandas as pd
import numpy as np
import bokeh

df = pd.read_csv('PokemonData.csv')

from bokeh.charts import Bar, output_file, save

Pokemon = Bar(df, 'Type 1', values = 'Speed', title = "Speed of Types of Pokemon", color = "blue")  
output_file('Pokemon.html')

save(Pokemon)
#import programs needed 
import csv
import pandas as pd
import numpy as np
import bokeh
#make the csv file readable
df = pd.read_csv('PokemonData.csv')

from bokeh.charts import Scatter, output_file, save
from bokeh.palettes import plasma
PokemonScatterPlot = Scatter(df,'Type 1', y='Speed', title = 'Pokemon Types Vs. Speed', xlabel='Type of Pokemon', ylabel='Speed')
output_file("PokemonScatterPlot.html")
save(PokemonScatterPlot)
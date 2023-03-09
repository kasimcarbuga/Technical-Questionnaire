import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/kasim/Desktop/BELGELER/country_vaccination_stats.csv')

print(data.isnull().any())

countries = data['country'].unique()

for c in countries:
    
    min_vac = data[data['country']==c].daily_vaccinations.min()
    
    if np.isnan(min_vac):
        
        values = {'daily_vaccinations': 0}
        
    else:
        

        values = {'daily_vaccinations': min_vac}
        
    data[data['country'] == c] = data[data['country'] == c].fillna(value=values)

print(data.isnull().any())

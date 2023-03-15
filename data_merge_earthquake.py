#merge csv files
import pandas as pd
import os
csvs_path = 'queries/'
csvs = [csvs_path + f for f in os.listdir(csvs_path) if f.endswith('.csv')]
df = pd.concat([pd.read_csv(f) for f in csvs])
df.to_csv('merged.csv', index=False)

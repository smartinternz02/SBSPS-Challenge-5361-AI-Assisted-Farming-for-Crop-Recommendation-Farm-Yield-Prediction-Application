    

import pandas as pd
import csv
import sqlite3
from pathlib import Path
Path('crop_data.sqlite3').touch()

conn=sqlite3.connect('crop_data.sqlite3')
cursor=conn.cursor()
data=pd.read_csv("crop_production.csv")
data.to_sql('crop_production', conn, if_exists='replace', index = False)
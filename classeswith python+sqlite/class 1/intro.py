import sqlite3
import pandas as pd

database = 'classeswith python+sqlite\class 1\database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

data =  pd.read_sql("""SELECT * 
FROM sqlite_master
WHERE type='table';""", conn)

print(data)


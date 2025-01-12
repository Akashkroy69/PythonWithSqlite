# import sqlite3
# import pandas as pd

# database = 'classeswith python+sqlite\class 1\database.sqlite'

# conn = sqlite3.connect(database)
# print('Opened data successfully')

# data =  pd.read_sql("""SELECT * 
# FROM sqlite_master
# WHERE type='table';""", conn)

# print(data)

import sqlite3
import pandas as pd

databaseSource = r'C:\Users\Lenovo\OneDrive\Desktop\aaVS_CODE\PythonWithSQLite\classeswith python+sqlite\class 1\database.sqlite'

connection = sqlite3.connect(databaseSource)
print('Opened data successfully',connection)

data = pd.read_sql("""select * from sqlite_master where type='table'""",connection)
print(data)
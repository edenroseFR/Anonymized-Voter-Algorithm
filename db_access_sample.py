import pygsheets
import pandas as pd

# authorization
path = "C:/Users/John Eric Engana/Documents/Projects/CSC-TRIAL_CODE/creds.json"
gc = pygsheets.authorize(service_file=path)

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

# open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('CSC-TRIAL')

# select the first sheet
wks = sh[0]

# update the first sheet with df, starting at cell B2.
wks.set_dataframe(df, (1, 1))

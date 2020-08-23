
import pandas as pd
# Reading and displaying data
df = pd.read_csv (r'real_estate.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(df.head(5))




x = df[1,2]
print(x)
#y = data[:,-1]
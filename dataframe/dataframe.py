#as pd to alias
from lib2to3.pgen2.pgen import DFAState
import pandas as pd

my_df = pd.read_csv('people.csv')
#read the whole thing
print(my_df)
print()

#read an attribute value based on row and column index [row, column]
print("my_df.iloc[1,0]: ", my_df.iloc[1,0])
print()

#read an attribute value based on row index and column name [row, column name]
print("my_df.loc[2, 'Who']: ", my_df.loc[2, 'Who'])
print()

#add a unique ID to the dataframe so that we can write it to csv
my_df['ID'] = my_df.index
print(my_df)

#write back the changes to the file
my_df.to_csv('people.csv')
import pandas as pd 
dict={'x':[1,2,3,4],
        'v':[5,6,7,8]}

# print dict['x'][1]


df=pd.DataFrame(dict)
# print (df)

# print(df.shape)
rows,cols=df.shape
# returns a tuple
# print(rows)


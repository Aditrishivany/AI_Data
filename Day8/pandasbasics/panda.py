import pandas as pd
my_dataset={
    'bike':['KTM','Yamaha','Honda','Harley'],
    'passings':[1,2,3,4]
}

df=pd.DataFrame(my_dataset)
print(df)

#pandas series

a=[1,2,3,4,5]
ps=pd.Series(a)
print(ps)

# #labels
print(a[0])

mv=pd.Series(a,index=['a','b','c','d','e'])
print(mv)

print(mv['d'])

data = {
    "Name": ["Asha", "Ravi", "Neha", "Kiran", "Suman"],
    "Age": [21, 22, 20, 23, 21],
    "City": ["Hyderabad", "Bengaluru", "Chennai", "Pune", "Delhi"]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[0])
print(df.loc[[0,1]])
# named indexing
df = pd.DataFrame(data,index=['n1','n2','n3','n4','n5'])

print(df.loc['n2'])

print(df.loc[['n2','n3']])

# load files into panda dataframe
df=pd.read_csv('sample.csv')
print(df.head())
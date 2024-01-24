import pandas as pd

# Series
series1 = pd.Series( [10, 20, 30, 40, 50],index=['a', 'b', 'c', 'd', 'e'] )
print(series1)
print(series1['a'])

student_names = {
    "Student1" : "Zahir",
    "Student2" : "Barry",
    "Student3" : "Bruce Wayne"
}

series2 = pd.Series(student_names, index=["Student1", "Student3"])
print(series2)
print(series2["Student3"])

print()
print()



# DataFrames


#Via a dictionary
data = {
    'Name' :          ['Batman', 'Superman', 'Spiderman', 'X-men', 'Robocop'],
    'True Identity' : ['Bruce Wayne', 'Clark Kent', 'Peter Parker', 'Hugh Jackman', 'Someone']
}

df = pd.DataFrame(data)
print(df)
print()
print()

#Via a python list
data2 = [
        ['Batman', 'Bruce Wayne'],
        ['Superman', 'Clark Kent'],
        ['Spiderman', 'Peter Parker'],
        ['X-men', 'Hugh Jackman'],
        ['Robocop', 'Someone'],
        ]

df2 = pd.DataFrame(data2, columns=["Hero Name", "True Identity"])
print(df2)
print()
print()

#from a csv file
# df3 = pd.read_csv('data.csv')
# print(df3)

print()
print()



#via empty DataFrame
df4 = pd.DataFrame()
print(df4)
print()
print()



##Index

#Default
df3 = pd.read_csv('data.csv')
print(df3)


#Setting Index
data2 = {
    'Name' :          ['Batman', 'Superman', 'Spiderman', 'X-men', 'Robocop'],
    'True Identity' : ['Bruce Wayne', 'Clark Kent', 'Peter Parker', 'Hugh Jackman', 'Someone']
}

df5 = pd.DataFrame(data2)
df5.set_index('Name', inplace=True)
print(df5)
print()
print()


#Range Index
# student_grades = {
#     'Name': ['John', 'Joey', 'Sheldon'],
#     'GPA' : [3.1, 2.0, 3.5]
# }
# df6 = pd.DataFrame(student_grades, index = pd.RangeIndex(5,8, name="custom_index"))

# print(df6)

#Index renaming
student_grades = {
    'Name': ['John', 'Joey', 'Sheldon'],
    'GPA' : [3.1, 2.0, 3.5]
}
df6 = pd.DataFrame(student_grades)
df6.rename(index={0:'A', 1:'B', 2:'C'}, inplace=True)
print(df6)
print()
print()

## Pandas Data Cleaning
#Missing Values
data3 = {
    'A' : [1,    2,  3,     None,  5, 1,    2,  3,     None,  5],
    'B' : [None, 2,  3,     4,     5, None, 2,  3,     4,     5],
    'C' : [1,    2,  None,  None,  5, 1,    2,  None,  None,  5]
}
df7 = pd.DataFrame(data3)
print("Dirty DataFrame")
print(df7)
print("Clean DataFrame")
# clean_df7 = df7.dropna()
# print(clean_df7)
# df7.fillna(0, inplace=True)
df7.fillna(df7.mean(), inplace=True)
print(df7)

print()
print()

#Duplicates
data4 = {
    'A' : [1,2,2,3,3,4],
    'B' : [5,6,6,7,7,8]
}
df8 = pd.DataFrame(data4)
print(df8)
print()
# print(df8[df8.duplicated()])
df8.drop_duplicates(subset=['A'], keep='first', inplace=True)
print(df8)

print()
print()

#Aggregate
data5 = {
    'Category' : ['a','a','b','b'],
    'Value' : [10,15,20,25]
}

df9 = pd.DataFrame(data5)
print(f"Total sum {df9['Value'].aggregate('sum')}")
print(f"Mean {df9['Value'].aggregate('mean')}")
print(f"Max {df9['Value'].aggregate('max')}")
print(f"Min {df9['Value'].aggregate('min')}")

result = df9.groupby('Category')['Value'].agg(['sum', 'mean','max','min'])
print(result)
print("Hello")
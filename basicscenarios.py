import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', 'Priya'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)

import pandas as pd

df = pd.read_csv('employee.csv')

print(df)

import pandas as pd

df = pd.read_csv('students.csv')

print(df.head())

import pandas as pd

df = pd.read_csv('students.csv')

print(df.tail())

import pandas as pd

data = {'Marks': [80, 90, 70, 85, 95]}

df = pd.DataFrame(data)

print("Average:", df['Marks'].mean())

import pandas as pd

data = {'Marks': [45, 78, 90, 65, 88]}

df = pd.DataFrame(data)

print("Maximum:", df['Marks'].max())
print("Minimum:", df['Marks'].min())

import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', 'Priya', 'John'],
    'Marks': [35, 80, 90, 25]
}

df = pd.DataFrame(data)

passed = df[df['Marks'] >= 40]

print(passed)

import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', 'Priya'],
    'Marks': [85, 65, 95]
}

df = pd.DataFrame(data)

df['Grade'] = ['A', 'B', 'A']

print(df)

import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', 'Priya'],
    'Marks': [85, 65, 95]
}

df = pd.DataFrame(data)

df['Grade'] = ['A', 'B', 'A']

print(df)

import pandas as pd

data = {
    'Name': ['Amit', 'Ravi'],
    'Age': [25, 30],
    'Salary': [20000, 30000]
}

df = pd.DataFrame(data)

df = df.drop('Age', axis=1)

print(df)

import pandas as pd

data = {
    'Name': ['Amit', 'Ravi', 'Priya'],
    'Marks': [80, None, 90]
}

df = pd.DataFrame(data)

df = df.fillna(0)

print(df)
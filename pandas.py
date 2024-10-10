# https://www.geeksforgeeks.org/pandas-tutorial/
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
# https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp

import pandas as pd

data = pd.read_csv("employee_data.csv")
df = pd.DataFrame(data)

df.head()

it_employees=df[(df['Department'] == "IT")]
it_employees

seasoned_employees=df[(df['Years of Experience'] > 5)]
seasoned_employees

number_four=df[(df['City'] == 'New York') & (df['Salary'] > 60000)]
number_four

num_five=df[(df['Salary'] > 65000)]
num_five.to_csv('high_salary_employees.csv')
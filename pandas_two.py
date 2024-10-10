import pandas as pd
from word2number import w2n

data = pd.read_csv("Updated_employee.csv")

df = pd.DataFrame(data)
df.info()

df

df["Name"] = df["Name"].str.capitalize()
df["Name"]

formats = ['%m-%d-%Y', '%m/%d/%Y', '%Y-%m-%d', '%Y/%m/%d']

# Define a function to convert date
def convert_to_date(date_str):
    for fmt in formats:
        try:
            date = pd.to_datetime(date_str, format=fmt, errors='coerce').strftime('%m-%d-%Y')
            return date if not pd.isna(date) else date_str  # Return formatted date if valid, else original
        except ValueError:
            continue
    return date_str


df['Joining Date'] = df['Joining Date'].apply(convert_to_date)
df['Joining Date']

df["Age"] = df["Age"].apply(lambda x: w2n.word_to_num(x) if pd.notna(x) else x)
df["Age"]

#Summary Statistics for Age
df["Age"].describe()

#Calculate the Average Salary
numeric_salary = df["Salary"].apply(lambda x: w2n.word_to_num(x) if pd.notna(x) else x)

print(numeric_salary.mean().round(2))

#Count the Number of Employees in Each Department
count_by_dept = df.groupby(["Department"])["Name"].count()
count_by_dept

#Identify the Employee with the Highest and Lowest Salary
df["Salary"]= df["Salary"].apply(lambda x: w2n.word_to_num(x) if pd.notna(x) else x)
max_salary=df["Salary"].max()
min_salary=df["Salary"].min()

employees_with_max = df[(df["Salary"] == max_salary)]["Name"]
employees_with_min = df[(df["Salary"] == min_salary)]["Name"]

employees_with_max
employees_with_min
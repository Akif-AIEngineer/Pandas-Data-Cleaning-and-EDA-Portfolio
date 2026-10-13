import pandas as pd
import numpy as np
# Step 1: Data Load Karna 
data = { 'Name': ['Akif', 'Saquib', 'Abnu', 'Akif'], 'Age': [19, 22, 6, 250], 'Salary': [10000, np.nan, 2000, np.nan] }
df = pd.DataFrame(data)
Name = "--- 🩷MD AKIF ANNU🩷 ---"
print (Name.center(50))
print ("\n--- Messy/Ganda Data Ko Dikhao Table Mein ---\n")
print (df)
# Step 2: Duplicates Hatao
df = df.drop_duplicates(subset = ['Name'])
#Step 3: Khaali Jagah Ko Check Karna
print ("\n--- Duplicate Hata Kar Aur Khaali Jagah Check Kar Ke Table Banao ---\n")
print (df.isnull().sum())
# Step 4: Khaali Jagah Ko Bharna
avg_salary = df ['Salary'].mean()
df ['Salary'] = df ['Salary'].fillna(avg_salary)
# Step 5: Serial Number Ko Correct Karna
df = df.reset_index(drop=True)
# Step 6: Final Data Clean
print ("\n--- Clean Data Ko Table Mein Dikhao ---\n")
print (df)
print ("\n--- Data Ko Describe Kar Ke Table Mein Dikhao ---\n")
print (df.describe())
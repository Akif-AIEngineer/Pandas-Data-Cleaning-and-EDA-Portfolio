import pandas as pd
import numpy as np
#Step 1: Ganda Data Hai Compnay Ka
data = {
    'Emp_Name': ['Rahul', 'Priya', 'Amit', 'Rahul', 'Sneha', 'Amit'],
    'Age': [25, 28, 250, 25, 22, 29], 
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Delhi', np.nan, 'Pune'],
    'Salary': [50000, 60000, np.nan, 50000, 45000, 70000]
}
df = pd.DataFrame(data)
print("--- Kachra Data ---\n", df)
# Step 2: Ganda Data Se DUPLICATE Hatao
df = df.drop_duplicates(subset = ['Emp_Name'])
df = df [df ['Age'] < 100]
# Step 3: Missing Data Ko Dhundna
print ("\n--- Missing Data Ka Detail Dikhao ---\n")
print (df.isnull().sum())
# Step 4: Data Ko Fill Karna
df ['City'] = df ['City'].fillna ('Unknown')
# Step 5: Serial Number Ko Thik Karna
df = df.reset_index(drop=True)
# Step 6: Final Result 
print ("\n--- Saaf Suthra Data Ko Dikhao ---\n")
print (df)
# Step 7: EDA Karna Saaf Suthra Data Par
print ("\n--- Data Kee HIDDEN Insight Bataa/Dikhana Naa ---\n")
print (df.describe())
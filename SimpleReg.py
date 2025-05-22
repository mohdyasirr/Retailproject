# salary_prediction.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load dataset

df = pd.read_csv(r"Salary_Data.csv")
print(df)

# Visualize the relationship
sns.jointplot(x = "Years of Experience", y = "Salary", data = df)
plt.show()

# Prepare input and output
x = df["Years of Experience"]
y = df["Salary"]

print(x)
print(y)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

print("Testting *************")

print(x_test)
print(y_test)

print("Training *************")

print(x_train)
print(y_train)
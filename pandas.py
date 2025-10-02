import pandas as pd

# 1. Create a small sample DataFrame
data = {
    "Name": ["Chulsoo", "Younghee", "Minsu", "Jiyoung", "Minsu"],
    "Age": [25, 30, 27, 35, 27],
    "City": ["Seoul", "Busan", None, "Seoul", None],
    "Salary": [50000, None, 48000, 62000, 48000],
    "Department": ["Sales", "HR", "IT", "Sales", "IT"]
}
df = pd.DataFrame(data)

# 2. Data inspection
print("\n=== HEAD ===")
print(df.head())            # first 5 rows
print("\n=== INFO ===")
print(df.info())            # column info
print("\n=== NULL counts ===")
print(df.isnull().sum())    # count missing values

# 3. Preprocessing (basic cleaning)
df = df.drop_duplicates()                   # remove duplicate rows
df["Salary"] = df["Salary"].fillna(0)       # fill missing salary with 0
df["City"] = df["City"].fillna("Unknown")   # fill missing city with placeholder

# 4. Filtering examples
print("\n=== People older than 28 ===")
print(df[df["Age"] > 28])

print("\n=== Only Sales department ===")
print(df[df["Department"] == "Sales"])

print("\n=== Names containing 'su' ===")
print(df[df["Name"].str.contains("su", case=False)])



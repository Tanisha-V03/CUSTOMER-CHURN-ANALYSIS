# -------------------------- IMPORT LIBRARIES ----------------------------------
import pandas as pd
import numpy as np

#---------------------------- LOAD DATASET ----------------------------------------
df = pd.read_excel(r'C:\Users\hp\Documents\DATA ANALYTICS FILE\customer churn analysis.xlsx')
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

# ---------------------------- CHECK MISSING VALUES ---------------------------------------
print(df.isnull().sum())

# ----------------------------- CHECK DUPLICATE RECORD -------------------------------
print(df.duplicated().sum())

# ----------------------------- REMOVE DUPLICATE -------------------------------------
df.drop_duplicates(inplace = True)
print(df.duplicated().sum())
print(df.shape)

# ------------------------------ REPLACE DIRTY(N/A OR NULL) VALUES -----------------------------
df.replace(('N/A', 'NULL', '', ' '), np.nan, inplace= True)
print(df.isnull().sum())

# --------------------------------- REMOVE EXTRA SPACES -------------------------------
df = df.apply(lambda x:x.str.strip() if x.dtype == "object" else x)

# ---------------------------------- PROPER CASE --------------------------
print(df['Subscription_Type'].value_counts())

df["Customer_Name"] = df["Customer_Name"].str.strip().str.title()
df["Gender"] = df["Gender"].str.strip().str.title()
df["State"] = df["State"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
df["Subscription_Type"] = df["Subscription_Type"].str.strip().str.title()
df["Contract_Type"] = df["Contract_Type"].str.strip().str.title()
df["Payment_Method"] = df["Payment_Method"].str.strip().str.title()
df["Internet_Service"] = df["Internet_Service"].str.strip().str.title()
df["Tech_Support"] = df["Tech_Support"].str.strip().str.title()
df["Senior_Citizen"] = df["Senior_Citizen"].str.strip().str.title()
df["Dependents"] = df["Dependents"].str.strip().str.title()


df["Churn"] = df["Churn"].str.strip().str.title()

print(df['Subscription_Type'].value_counts())

print(df['Subscription_Type'].unique())

# -------------------------------- STANDARDIZE CHURN COLUMN ------------------------
print(df['Churn'].value_counts())

# -------------------------------- CONVERT NUMERIC COLUMNS --------------------
cols = ['Age', 'Tenure_Months', 'Monthly_Charges', 'Total_Charges']
for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

print(df.describe())

# ---------------------------------- REMOVE INVALID AGE ----------------------------
df = df[(df["Age"]>=18) & (df["Age"]<=100)]
print(df.describe())

# ------------------------------------ REMOVE NEGATIVE CHARGES ------------------------
df = df[df['Monthly_Charges']>=0]
df = df[df['Total_Charges']>=0]

print(df.shape)

# ------------------------------------- CONVERT DATE ------------------------------
df['Last_Interaction_Date'] = pd.to_datetime(df['Last_Interaction_Date'], errors='coerce')

# ------------------------------------ FILL MISSINNG VALUES -------------------------
df['Tech_Support'] = df['Tech_Support'].fillna('No')
df['Payment_Method'] = df['Payment_Method'].fillna('Unknown')
df['Monthly_Charges'] = df['Monthly_Charges'].fillna(df["Monthly_Charges"].mean())
df['Tenure_Months'] = df['Tenure_Months'].fillna(df["Tenure_Months"].mean())
df['Age'] = df['Age'].fillna(df["Age"].mean())
df['Last_Interaction_Date'] = df['Last_Interaction_Date'].fillna(df["Last_Interaction_Date"].median())


# ------------------------------------- ADDING NEW COLUMN --------------------------------

# # 1. Customer Lifetime Value
df['Customer_Value'] = df['Monthly_Charges'] * df['Tenure_Months']

# # 2. Monthly REvenue
df['Monthly_Revenue'] = df['Monthly_Charges']

# # 3. Tenure group(0-12, 13-14, 25-48, and so on)
bins = [0,12,24,48,72]
label = labels = ['0-12 month', '13-24 month', '25-48 month', '49-72 month']

df['Tenure_Group'] = pd.cut(df['Tenure_Months'], bins = bins, labels = label)

# # 4. Senior Citizen Flag
df['Senior_Flag'] = np.where(df['Age']>=60, 'Senior', 'Adult')

# # 5. Churn Flag
df['Churn_Flag'] = (df['Churn'].map({'Yes' : 1, 'No' : 0}))

# ------------------------ ------ FIANL LOOK ---------------------------------------
print(df.info())
print(df.describe())
print(df.isnull().sum())

# --------------------------- CSV CLEAN DATASET ---------------------------
df.to_csv('Clean_Churn_Dataset.csv', index = False)

# --------------------------- EXPORT TO SQL -----------------------------
# Step 18: Export into PostgreSQL

from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Mera pswd h@localhost:5432/churndb")

df.to_sql(
    "customer_churn",
    con = engine,
    if_exists = "replace",
    index = False
)




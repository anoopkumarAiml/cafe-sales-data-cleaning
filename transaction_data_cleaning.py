import numpy as np
import pandas as pd

#  ============================================================================================
#  Load raw data
#  ============================================================================================

df = pd.read_csv("dirty_cafe_sales.csv")

#  Remove leading and trailing whitespace from all column names
df.columns = df.columns.str.strip() 


#  ===============================================================================================
#  Quantity cleaning and validation
#  ===============================================================================================
#  Business rule: Quantity must be a positive whole number for
#                billing calculations

df["Quantity"] = pd.to_numeric(df["Quantity"], errors = "coerce")
df = df.dropna(subset =["Quantity"])
df = df[df["Quantity"]>0]
df =df[df["Quantity"]%1==0]
df["Quantity"] = df["Quantity"].astype(int)

assert (df["Quantity"]> 0).all()

#  ================================================================================================
#  Price Per Unit cleaning
#  ================================================================================================
#  Business rule: Price per unit must be a positive numeric value 
#                 for billing.

df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors = "coerce")
df = df.dropna(subset=["Price Per Unit"])
df = df[df["Price Per Unit"]>0]
df["Price Per Unit"] = df["Price Per Unit"].astype(float)

assert (df["Price Per Unit"]>0).all()

#  =================================================================================================
#  Transaction Date normalization
#  =================================================================================================
#  Bussiness rule: Transaction date must be a valid date and cannot
#                  be a valid date and not be in the future

df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors = "coerce")
df = df.dropna(subset = ["Transaction Date"])
df = df[df["Transaction Date"] <= pd.Timestamp.today().normalize()]
assert df["Transaction Date"].isna().sum() == 0

#  ================================================================================================
#  Transaction ID validation
#  ================================================================================================
#  Business rule: Transaction ID must be present and unique

df["Transaction ID"] = (df["Transaction ID"].astype("string").str.strip().str.upper())
df["Transaction ID"] = df["Transaction ID"].replace([" ",  "NOT","0" "UNKNOWN", "NONE", "ERROR"], pd.NA)

assert df["Transaction ID"].isna().sum() == 0
assert df["Transaction ID"].is_unique

#  ================================================================================================
# Total Spent recomputation
#  ================================================================================================
#  Business rule: Total Spent is derived
#                from Quantity x Price Per Unit.

df["Total Spent"] = df["Quantity"] * df["Price Per Unit"]

# All inavlid total spent is not correct

#  ==============================================================================================
#  Payment Method normaliztion
#  ==============================================================================================
#  Business ruel: Payment Method is optional; missing
#                 values are retained as NA
df["Payment Method"] = df["Payment Method"].astype("string")
df["Payment Method"] = (df["Payment Method"].str.strip().str.upper().replace([" ","N/A", "UNKNOWN", "NONE", "ERROR", "N/A"], pd.NA))


payment_map = {
    "CREDIT CARD" : "CARD",
    "DEBIT CARD" : "CARD",
    "CARD PAYMENT" : "CARD",
    "CASH PAYMENT" : "CASH"
}
df["Payment Method"] = df["Payment Method"].replace(payment_map)

#  ===============================================================================================
#  Location normalization
#  ===============================================================================================
df["Location"] = df["Location"].astype("string")
df["Location"] = (df["Location"].str.strip().str.title().replace([" ", "UNKOWN","Unknown","None", "Error"], pd.NA))


#  ===============================================================================================
#  Item cleaning and enforcement
#  ===============================================================================================

df["Item"] = (df["Item"].astype("string").str.strip().str.title())
df["Item"] = df["Item"].replace([" ", "None", "Unknown", "Error", "Nan"], pd.NA)
df = df.dropna(subset = ["Item"])

#  ================================================================================================
#  Duplicate transaction removal
#  ================================================================================================
dup_col =[
    "Transaction Date",
    "Item",
    "Location",
    "Quantity",
    "Price Per Unit"
]
df["is_potential_duplicate"] = df.duplicated(subset = dup_col, keep = False)

#  ================================================================================================
#  Final dataset integrity checks
#  ================================================================================================

assert df["Item"].isna().sum() == 0


#  Save cleaned dataset
df.to_csv("cleaned_transaction.csv", index = False )


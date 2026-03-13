import pandas as pd
import glob

# Step 1: Get all CSV files
files = glob.glob("data/*.csv")

# Step 2: Read and combine them
dataframes = []

for file in files:
    df = pd.read_csv(file)
    dataframes.append(df)

data = pd.concat(dataframes)

# Step 3: Keep only Pink Morsels
data = data[data["product"] == "pink morsel"]

# Step 4: Clean price column
data["price"] = data["price"].replace('[\$,]', '', regex=True).astype(float)

# Step 5: Calculate Sales
data["sales"] = data["quantity"] * data["price"]

# Step 6: Keep required columns
final_data = data[["sales", "date", "region"]]

# Step 7: Save output
final_data.to_csv("data/formatted_salesdata.csv", index=False)

print("Data processing complete!")
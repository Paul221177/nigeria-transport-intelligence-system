import pandas as pd

# Load dataset
df = pd.read_csv("data/abuja_transport_data.csv")

# Display first rows
print("\n=== Abuja Transport Dataset ===")
print(df.head())

# Average transport fares
df["Average_Fare"] = (
    df["Morning_Fare"] +
    df["Afternoon_Fare"] +
    df["Evening_Fare"]
) / 3

print("\n=== Average Fare Per Route ===")
print(df[["Route", "Average_Fare"]])

# Highest evening fare
highest_fare = df.loc[df["Evening_Fare"].idxmax()]

print("\n=== Highest Evening Fare Route ===")
print(highest_fare)

# Traffic level counts
print("\n=== Traffic Level Distribution ===")
print(df["Traffic_Level"].value_counts())

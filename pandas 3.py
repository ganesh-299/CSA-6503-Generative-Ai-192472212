import pandas as pd

data = {
    "Department": ["CSE", "AI", "CSE", "ECE"]
}

df = pd.DataFrame(data)

print(df["Department"].unique())
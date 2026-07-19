import pandas as pd

data = {
    "Department": ["CSE", "AI", "CSE", "AI", "AI"]
}

df = pd.DataFrame(data)

print(df["Department"].value_counts())
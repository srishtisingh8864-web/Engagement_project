import pandas as pd
import numpy as np

# STEP 1: Load data
df = pd.read_csv("data.csv")

# STEP 2: Engagement Index
df['EngagementIndex'] = (
    df['JobInvolvement'] +
    df['JobSatisfaction'] +
    df['EnvironmentSatisfaction'] +
    df['RelationshipSatisfaction']
) / 4

# STEP 3: Burnout Risk
def burnout(x):
    if x['OverTime'] == 'Yes' and x['WorkLifeBalance'] <= 2:
        return "High"
    elif x['OverTime'] == 'Yes':
        return "Medium"
    else:
        return "Low"

df['BurnoutRisk'] = df.apply(burnout, axis=1)

# STEP 4: Clean data
df.fillna(0, inplace=True)

# STEP 5: Save output
df.to_csv("final_output.csv", index=False)

print("✅ Analysis Done")
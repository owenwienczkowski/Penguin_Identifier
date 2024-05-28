import pandas as pd
from scipy.stats import chi2_contingency


# Load your dataset
df = pd.read_csv('Penguin_Data.csv')

# Exclude 'species' and 'sex' from the median calculation
numerical_columns = df.select_dtypes(include=['number']).columns
medians1 = df.groupby('species')[numerical_columns].median()
medians2 = df.groupby('island')[numerical_columns].median()

# Print the median values for each numerical column for each island
print(medians1)
print(medians2)

# Create a contingency table
contingency_table = pd.crosstab(df['species'], df['island'])

# Perform the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Output the results
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print(f"Expected frequencies:\n {expected}")


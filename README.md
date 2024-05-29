# Penguin_Identifier

Machine learning engine to identify the species of a penguin based on available characteristics.

## Data Preparation:

Before the data could be used, cleaning was required. The different features stored for each entry were the penguin's species, island, culmen_length (mm), culmen_depth (mm), flipper_length (mm), body_mass (mm), and sex. For some entries, the data contained several null features. Entries with multiple (two or more) null features were removed; these features were removed using R. The R script has been included for reference. Some entries only included sex as a null feature. This was accepted as missing one feature (such as sex) is not essential for determining the penguin's species. To use KNN, sex was converted from a string value to a numerical value; 'female' became 0, 'male' became 1, and NA became 0.5 to remove influence of the missing value. The original dataset (Penguin_Data.csv) and the resulting dataset (cleaned_data.csv) are also both included for reference. The presence of the original dataset in conjunciton with the R script allow for the data to be more/less modified to retrain and retest the model.


The following script was used to determine if the penguin's island is meaningful:

----------------------
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
-
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print(f"Expected frequencies:\n {expected}")
----------------------
Due to the variance in medians and low p-value, the islands are statistically significant and should remain. In order to use this categorical data in KNN, it must be converted into a numerical metric. Due to the nature of KNN and "closeness", the islands cannot be assigned unique integers. Instead, they must become represented through one-hot encoding. 

## Next Steps:

The current model is limited by its simple dataset. To improve the model, the next steps would be to alter the data, potentially by adding noise, adding volume, adding features, or augmenting the data in other ways. Aside from that, the remaining steps are to further explore the results and to provide more visualization of the findings.

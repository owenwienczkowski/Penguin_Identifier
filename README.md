# Penguin_Identifier

Machine learning engine to identify the species of a penguin based on available characteristics.

## Data Preparation:

Before the data could be used, cleaning was required. The different values stored for each entry were the penguin's species, island, culmen_length (mm), culmen_depth (mm), flipper_length (mm), body_mass (mm), and sex. For some entries, the data contained several null attributes. Entries with multiple (two or more) null values were removed; these values were removed using R. The R script has been included for reference. Some entries only included one null attribute. This was accepted as missing one attribute (such as sex) is not essential for determining the penguin's species.



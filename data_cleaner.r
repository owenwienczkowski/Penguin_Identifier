# Load the data from the CSV file
data <- read.csv('Penguin_Data.csv', na.strings = 'NA')

# Replace 'FEMALE' with 0 and 'MALE' with 1 in the 'sex' column
data$sex <- as.character(data$sex)  # Convert factors to characters if necessary
data$sex[data$sex == 'FEMALE'] <- '0'
data$sex[data$sex == 'MALE'] <- '1'

# Replace any 'NA' character strings with '0.5'
data$sex[is.na(data$sex)] <- 0.5

# Convert the 'sex' column to numeric, suppressing warnings
suppressWarnings(data$sex <- as.numeric(data$sex))

# Define a function to count NAs in each row
count_nas <- function(row) {
  sum(is.na(row))
}

# Apply the function to each row and filter out rows with 2 or more NAs
cleaned_data <- data[apply(data, 1, count_nas) < 2, ]

# Write the modified data back to a new CSV file
write.csv(cleaned_data, 'cleaned_data.csv', row.names = FALSE)

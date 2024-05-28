# Load the data from the CSV file
data <- read.csv('Penguin_Data.csv', na.strings = 'NA')

# Define a function to count NAs in each row
count_nas <- function(row) {
  sum(is.na(row))
}

# Apply the function to each row and filter out rows with 2 or more NAs
cleaned_data <- data[apply(data, 1, count_nas) < 2, ]

# Write the cleaned data back to a new CSV file
write.csv(cleaned_data, 'cleaned_data.csv', row.names = FALSE)

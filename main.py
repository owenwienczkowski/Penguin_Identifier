import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cleaned_data.csv')

# Assume 'species' is the target variable and it's the first column
X = df.iloc[:, 1:]  # Features
y = df.iloc[:, 0]   # Target species (label)

# Preprocess the data: One-hot encode categorical variables and scale numerical features
categorical_features = ['island', 'sex']
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

X_processed = preprocessor.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.1, random_state=42)

# Initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)

# Train the KNN classifier
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Assuming 'y_test' contains the actual species labels and 'y_pred' contains the predicted labels
# For demonstration, let's convert species names to numerical labels
species_to_num = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
y_test_num = [species_to_num[species] for species in y_test]
y_pred_num = [species_to_num[species] for species in y_pred]

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(y_test_num, y_pred_num, alpha=0.5)
plt.title('Model Predictions vs Actual Values')
plt.xlabel('Actual Species Labels')
plt.ylabel('Predicted Species Labels')
plt.xticks(ticks=[0, 1, 2], labels=['Adelie', 'Chinstrap', 'Gentoo'])
plt.yticks(ticks=[0, 1, 2], labels=['Adelie', 'Chinstrap', 'Gentoo'])
plt.plot([-1, 3], [-1, 3], 'r--')  # Diagonal line for reference
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.grid(True)
plt.show()

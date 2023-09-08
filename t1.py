from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
dataFrame = pd.read_csv("/home/luvranjan/Desktop/PRODIGY_ML_01-main/ranjan.csv")

# Display summary statistics of the 'SalePrice' column
print(dataFrame['SalePrice'].describe())

# Define features (A) and target (B)
A = dataFrame[['GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'BedroomAbvGr', 'FullBath', 'HalfBath']]
B = dataFrame['SalePrice']

# Split the data into training and testing sets
A_train, A_test, B_train, B_test = train_test_split(A, B, random_state=1)

# Create and fit the Linear Regression model
model = LinearRegression()
model.fit(A_train, B_train)

# Make predictions on the test set
B_pred = model.predict(A_test)

# Calculate and print the Mean Squared Error and Coefficient of Determination (R-squared)
mse = mean_squared_error(B_test, B_pred)
r2 = r2_score(B_test, B_pred)

print('Mean squared error: %.2f' % mse)
print('Coefficient of determination (R-squared): %.2f' % r2)

your_name = "Hritik ranjan"
github_link = "https://github.com/hritikranjan1"
linkedin_link = "https://www.linkedin.com/in/hritikranjan"

print(f"Name: {Hritik_ranjan}")
print(f"GitHub: {https://github.com/hritikranjan1}")
print(f"LinkedIn: {https://www.linkedin.com/in/hritik-ranjan-05a835230}")

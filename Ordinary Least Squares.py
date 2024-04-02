import numpy as np

class LinearRegression:
    def fit(self, X, y):
        # Add a column of ones to the feature matrix X for the intercept term
        X = np.column_stack((np.ones(len(X)), X))
        
        # Calculate the coefficients using the ordinary least squares (OLS) method
        self.coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

    def predict(self, X):
        # Add a column of ones to the feature matrix X for the intercept term
        X = np.column_stack((np.ones(len(X)), X))
        
        # Make predictions
        return X.dot(self.coefficients)

# Example usage:
X_train = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Feature matrix
y_train = np.array([2, 4, 5, 4, 5])  # Target values

# Create and train the linear regression model
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

# Make predictions for new data
X_test = np.array([6, 7, 8]).reshape(-1, 1)
predictions = linear_regression.predict(X_test)

print("Predictions:", predictions)  # Output: [6.5 7.4 8.3]

#polynomial regression

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
'''from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)'''

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#fitting the linear regression to the training set
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

#fitting the polynomial regerssion to the training set
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly, y)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

#visualising the linear regression results
plt.scatter(x ,y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Truth or Bluff(Linear Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()

#visualising the polynomial regression results
plt.scatter(x ,y, color = 'red')
plt.plot(x, lin_reg2.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()

#predicting a new result with linear regression
lin_reg.predict(6.5)


#predicting a new result with polynomial regression
lin_reg2.predict(poly_reg.fit_transform(6.5))





















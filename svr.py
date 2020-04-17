#svr

# regression template

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
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)

#fitting the  regression to the training set
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(x, y)

#predicting a new result with polynomial regression
y_pred = regressor.predict(6.5)
y_pred = sc_y.inverse_transform(y_pred)

y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))



#visualising the polynomial regression results
plt.scatter(x ,y, color = 'red')
plt.plot(x, lin_reg2.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()


















#Multiple linear regression
#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 #importing datasets
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
x[:, 3] = labelencoder.fit_transform(x[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
x = onehotencoder.fit_transform(x).toarray()

# Avoiding the Dummy Variable Trap
x = x[:, 1:]

#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""

#fitting multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#predicting the test set results
y_pred = regressor.predict(x_test)

"""#building the optimal model using backward elimination
import statsmodels.formula.api as sm
#x = np.append(arr = x, values = np.ones((50, 1)).astype(int), axis = 1 )
x = np.append(arr = np.ones((50, 1)).astype(int), values = x, axis = 1 )
x_opt = x[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regressor_OLS.summary()"""

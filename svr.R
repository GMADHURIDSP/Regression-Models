#Support Vector Regression

#Regression Template

#Data preprocessing
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[2:3]

#splitting the dataset into training set and test set
#install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split ==TRUE)
# test_set = subset(dataset, split ==FALSE)

#feature scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])


#fitting  svr to the training set
install.packages('e1071')
library(e1071)
regressor = svm(formula = Salary ~ ., data = dataset, type = 'eps-regression')

#predicting a new result with polynomial regression
y_pred = predict(regressor, data.frame(Level = 6.5))



#visualising the svr results
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff(SVR') +
  xlab('Level') +
  ylab('Salary')





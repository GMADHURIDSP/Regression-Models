#Simple Linear Regression

#Data preprocessing
dataset = read.csv("Salary_Data.csv")

#splitting the dataset into training set and test set
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split ==TRUE)
test_set = subset(dataset, split ==FALSE)

#feature scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])

#fitting simple linear regression to the training set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

#predicting the test set results
y_pred = predict(regressor, newdata = test_set)

#visualising the training set results
install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, 
                 y = training_set$Salary,
                 color = 'red')) +
  geom_line(aes(x = training_set$YearsExperience,
                 y = predict(regressor, newdata = training_set)),
                 color = 'blue') +
  ggtitle('Salary vs Experience(Training_set') +
  xlab('Years of Experience') +
  ylab('Salary')

#visualising the test set results
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, 
                 y = test_set$Salary,
                 color = 'red')) +
  geom_line(aes(x = training_set$YearsExperience,
                 y = predict(regressor, newdata = training_set)),
             color = 'blue') +
  ggtitle('Salary vs Experience(Test_set') +
  xlab('Years of Experience') +
  ylab('Salary')
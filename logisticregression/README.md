# Logistic Regression
Logistic regression is one of the most commonly used regressions which can be used to model the overall trends of various datasets and predict results for values that have not been provided. This model is used when the results can be separated into binary classifications. For example, checking whether someone passed(1) or failed(0) an exam. As compared to linear regression, here there are only two discrete options(yes or no), while in linear regressions, the output can take up any value and is continuous in nature. 

Therefore in linear regression, whatever is the predicted output of a certain senario is converted to its catagorical value using the sigmoid function.
The sigmoid function is such that if the values of x tend towards positive infinity, the value of y will get closer and closer to 1, and if the values of x tend towards negative infinity, the corresponding values of y will reach closer to 0. Mathematically, the sigmoid function is represented as y = 1/(1+(e^-x)) where x is the input value and y is its corresponding transformed value between 1 and 0.

To provide a clearer picture of the situation, if the transformed value is between 0 and 0.5, it can be made into 0 and if it between 0.5 and 1, it can be made into 1. In this way the conditional probabilities for two labels (0 and 1) can be defined, making the logistic regression a function which predicts the probability of the occurrence of a binary outcome.


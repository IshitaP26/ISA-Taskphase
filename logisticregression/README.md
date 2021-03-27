# Logistic Regression

**Definition:**
Logistic regression is one of the most commonly used regressions which can be used to model the overall trends of various datasets and predict results for values that have not been provided. This model is used when the results can be separated into binary classifications. For example, checking whether someone passed(1) or failed(0) an exam. As compared to linear regression, here there are only two discrete options(yes or no), while in linear regressions, the output can take up any value and is continuous in nature.   
 
**Sigmoid Function:**
Therefore in logistic regression, whatever is the predicted output of a certain senario is converted to its catagorical value using the sigmoid function.  
The sigmoid function is such that if the values of x tend towards positive infinity, the value of y will get closer and closer to 1, and if the values of x tend towards negative infinity, the corresponding values of y will reach closer to 0. Mathematically, the sigmoid function is represented as y = 1/(1+(e^-z)) where z is the input value received from a linear function(y=mx+b), e is the euler's constant and y is the corresponding transformed value between 1 and 0.

**Gradient Descent and Cost function:**
Depending on the data present, the function of z will take up the form z = b0 + b1x1 + b2x2 + b3x3... + bnxn for n number of data inputs. To model the data set accurately and attain precise values of the coefficients(b0,b1,b2...) the stochastic gradient descent can be used. In general, the process of minimizing a function based on a certain cost function is called gradient descent. Stochastic gradient descent, in specifics, is the process of evaluating and updating the coefficients for every iteration, so as to minimize the error in the model that is finally created. The equation used to update the coefficients, based on the quadratic cost function, is:
                         b = b + alpha * (y-prediction) * prediction * (1-prediction) * x.

Here, b is the coefficient that is being optimized, alpha is the learning rate, y is corresponding y value of that data point, prediction is the value attained by 1/(1+(e^-z)) and x is the corresponding input value.

**Final outcome:**
So after performing numerous iterations upon the coefficients, a highly accurate value of the coefficients is attained which can then be used in the sigmoid function to receive the probability for any of the x inputs. 

To provide a clearer picture of the situation, if the transformed value is between 0 and 0.5, it can be made into 0 and if it between 0.5 and 1, it can be made into 1. In this way the conditional probabilities for two labels (0 and 1) can be defined, making the logistic regression a function which predicts the probability of the occurrence of a binary outcome.


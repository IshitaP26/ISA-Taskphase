# Linear Regression

**Definition:**
Linear regression shows the linear relationship between two continuous variables where upon changing one, the other also changes in a constant manner. It is based on the simple equation f(x) = mx + c, where f(x) predicts future values of data following this model and m and c are regression coefficients, representing the slope and y-intercept of the line, respectively.

**Its Use**
Usually, data collected in the real world does not exactly follow a linear form of growth or decay but can be approximated by a linear regression to understand the overall trend of the data and determine unknown values. It can therefore be used to study the relationship and dependency of the dependent variable on an independent variable, showing the effect of one variable on another. It  can  also be  used  to  make  predictions for input values which are previously unknown by using the pattern and trends in the data  at  hand  as  a  basis. 

**Methodology**
If given a scatterplot or table containing data, the Least Square method and Gradient Descent method can be used to find the most appropriate linear regression pertaining to that set of data. 
In the Least Square method the sum of the squared residuals, which is the distance between the data points and the values on the line, are minimized so as to lessen any deviation. 
Then in the Gradient Descent method, random values of the regression coefficient are taken and the sum of the squares of the residuals are calculated. The coefficients are then changed accordingly to decrease this error, based on a certain parameter which governs how much to change the values by in each trial. In the process of determining the linear regression, the error between the actual values of the data and the values predicted by the linear regression must be determined. 
The m and c values are initially made equal to 0 and alpha is taken as a small value (for example 0.0001), according to which the value of m will change. So with every iteration, the values of m and c are changed until the difference between the actual data values and the values predicted by the lines is 0. 
The values of m and c are updated according to the following formulas: mnew=mold−α1/SΣ[Ypredi−Yactuali]X  and cnew=cold−α1/SΣ(Ypredi−Yactuali)

Here, 
- mold is the slope value calculated up to the previous iteration 
- cold is the intercept value calculated up to the previous iteration
- α is the learning rate
- S is the total data points
- Ypred is the predicted value of Y for the data points using the m and c values obtained from the previous iteration
- Yactual is the actual known Y values from the data
- X is the known X values from the data


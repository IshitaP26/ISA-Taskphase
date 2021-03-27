import matplotlib.pyplot as plt  

# input data from user
size = int(input("\nEnter number of points to be evaluated: "))

# getting the Y co-ordinates for dataset
print("Enter y co-ordinates: ")
Y = list(map(float, input().split()))

# getting the X co-ordinates for dataset
print("\nEnter the x co-ordinates: ")
X = list(map(float, input().split()))

# getting the number of iterations 
num_iter = int(input("Enter the number of iterations: "))

# getting the initial slope and y intercept value from the user
print("\nEnter starting value of slope(m) and y intercept(c): ")
m, c = map(float, input().split())

#alpha has been taken as 0.01
def func(current, ynew, Y, x = [1.0 for k in range(len(Y))]):
    change = 0.0
    for j in range(len(Y)):
        change += (ynew[j] - Y[j]) * x[j]  
    return current - (0.01/len(Y)) * change  

# iternation for new m and c values and predicting the value of y based on the linear regression
for i in range(num_iter):
    ynew = [m * x_val + c for x_val in X]  
    m = func(m, ynew, Y, X)
    c = func(c, ynew, Y) 

# final slope and y-intercept
print("m = {} and c = {}".format(m,c))  

# checking the working of the line made to predict y values for corresponding x values
xnew = float(input("\nEnter the x co-ordinate to predict: "))
print("The value given by regression line is",m * xnew + c)

#final graph
ynew = [m * x_val + c for x_val in X]
plt.scatter(X,Y)  
ans_x = [xnew]  
ans_y = [m * xnew + c]  
plt.scatter(ans_x,ans_y, color = 'blue')   
plt.plot(X,ynew, color = 'red') 
plt.title("Regression Line")
plt.show()

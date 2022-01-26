import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

len(a[a < 0])
# There are four negative numbers.

#How many positive numbers are there?

len(a[a > 0])
#There are five positive numbers.

#How many even positive numbers are there?

a_evens = (a[a % 2 == 0])
len(a_evens[a_evens > 0])
#There are three even positive numbers.

#If you were to add 3 to each data point, how many positive numbers would there be?

a_plus_three = a + 3
len(a_plus_three[a_plus_three > 0])
#There are ten positive numbers in (a + 3).

#If you squared each number, what would the new mean and standard deviation be?

a_sq = a ** 2
a_sq.mean()
#When a is squared, the mean is 74.0.

a_sq.std()
#The standard deviation of a squared is 144.0243035046516.


#A common statistical operation on a dataset is centering. This means to 
# adjust the data such that the mean of the data is 0. This is done by 
# subtracting the mean from each data point. Center the data set. See this 
# link for more on centering.

centered_a = a - (a.mean())
centered_a.mean()

#Calculate the z-score for each data point

z_score_a = (a - a.mean()) / a.std()
print(z_score_a)

centered_a / a.std() == z_score_a

## Setup 1
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_b to hold the sum of all the 
# numbers in above list

sum_of_b = sum(i for i in b)
print(sum_of_b)

#The sum of b is 55.

# Exercise 2 - Make a variable named min_of_b to hold the minimum of all the 
# numbers in the above list

min_of_b = min(i for i in b)
print(min_of_b)

#The min value of b is 1.

# Exercise 3 - Make a variable named max_of_b to hold the max number of all 
# the numbers in the above list

max_of_b = max(i for i in b)
print(max_of_b)

#The max value of b is 10.

# Exercise 4 - Make a variable named mean_of_b to hold the average of all the 
# numbers in the above list

mean_of_b = sum_of_b / len(b)
print(mean_of_b)

#The mean of b is 5.5.

# Exercise 5 - Make a variable named product_of_b to hold the product of 
# multiplying all the numbers in the above list together

product_of_b = 1
for i in b:
    product_of_b *= i

print(product_of_b)




# Exercise 6 - Make a variable named squares_of_b. It should hold each number 
# in a squared like [1, 4, 9, 16, 25...]

squares_of_b = [i ** 2 for i in b]
print(squares_of_b)

# Exercise 7 - Make a variable named odds_in_b. It should hold only the odd 
# numbers

odds_in_b = []
for i in b:
    if i % 2 == 1:
        odds_in_b.append(i)
print(odds_in_b)

# Exercise 8 - Make a variable named evens_in_b. It should hold only the evens.

evens_in_b = []
for i in b:
    if i % 2 == 0:
        evens_in_b.append(i)
print(evens_in_b)

## What about life in two dimensions? A list of lists is matrix, a table, a 
# spreadsheet, a chessboard...

## Setup 2: Consider what it would take to find the sum, min, max, average, 
# sum, product, and list of squares for this list of two lists.
c = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_c as the 
# variable. **Hint, you'll first need to make sure that the "c" variable is a 
# numpy array**
sum_of_c = 0
for row in c:
    sum_of_c += sum(row)

print(sum_of_c)

num_c = np.array([[3, 4, 5], [6, 7, 8]])
num_c.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_c = min(c[0]) if min(c[0]) <= min(c[1]) else min(c[1])  

# Exercise 3 - refactor the following maximum calculation to find the answer 
# with numpy.
max_of_c = max(c[0]) if max(c[0]) >= max(c[1]) else max(c[1])

num_c.min()


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_c = (sum(c[0]) + sum(c[1])) / (len(c[0]) + len(c[1]))
num_c.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product 
# of all numbers multiplied together.
product_of_c = 1
for row in c:
    for number in row:
        product_of_c *= number

num_c.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_c = []
for row in c:
    for number in row:
        squares_of_c.append(number**2)

num_c ** 2


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_c = []
for row in c:
    for number in row:
        if(number % 2 != 0):
            odds_in_c.append(number)

num_c % 2 == 1
num_c[num_c % 2 == 1]


# Exercise 8 - refactor the following to use numpy to filter only the even 
# numbers
evens_in_c = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_c.append(number)

# Exercise 9 - print out the shape of the array c.
num_c.shape

# Exercise 10 - transpose the array c.
num_c.T

# Exercise 11 - reshape the array c to be a single list of 6 numbers. (1 x 6)

num_c.reshape(1,6)

# Exercise 12 - reshape the array c to be a list of 6 lists, each containing 
# only 1 number (6 x 1)

num_c.reshape(6,1)

## Setup 3
d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# HINT, you'll first need to make sure that the "d" variable is a numpy array 
# prior to using numpy array methods.

# Exercise 1 - Find the min, max, sum, and product of d.

num_d.min()
num_d.max()
num_d.sum()
num_d.prod()

# Exercise 2 - Determine the standard deviation of d.
num_d.std()

## Setup 4
f = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

num_f = np.array([[90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]])
    
# Exercise 1 - Find the sine of all the numbers in f

# Exercise 2 - Find the cosine of all the numbers in f

# Exercise 3 - Find the tangent of all the numbers in f

# Exercise 4 - Find all the negative numbers in f

# Exercise 5 - Find all the positive numbers in f

# Exercise 6 - Return an array of only the unique numbers in f.

# Exercise 7 - Determine how many unique numbers there are in f.

# Exercise 8 - Print out the shape of f.

# Exercise 9 - Transpose and then print out the shape of f.

# Exercise 10 - Reshape d into an array of 9 x 2
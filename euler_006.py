import numpy as np

numbers = np.arange(1,101)
sumSquare = np.sum(numbers*numbers)
squareSum = np.power(sum(numbers),2)

result = squareSum - sumSquare
print(result)

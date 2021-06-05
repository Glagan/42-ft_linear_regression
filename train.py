import sys
import csv
import math
import matplotlib.pyplot as plt

# Dataset path

dataset = 'data.csv'
if len(sys.argv) == 2:
    dataset = sys.argv[1]

# Read data

X = []
Y = []
with open(dataset) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    header = False
    for row in csvReader:
        if header == False:
            header = True
            continue
        X.append(float(row[0]))
        Y.append(float(row[1]))

# Normalize


def minMaxNormalize(val, min, max):
    return (val - min) / (max - min)


m = len(X)
X = [minMaxNormalize(i, min(X), max(X)) for i in X]
Y = [minMaxNormalize(i, min(Y), max(Y)) for i in Y]
errors = []


class GradientDescent:
    def __init__(self, learningRate, iterations):
        self.learningRate = learningRate
        self.iterations = iterations
        self.theta0 = 0.
        self.theta1 = 0.
        self.errors = []

    def cost(self):
        errorSum = 0.
        for l in range(m):
            errorSum += (((self.theta0 + (self.theta1 * X[l])) - Y[l]) ** 2)
        return errorSum / float(m)

    def run(self):
        for i in range(self.iterations):
            sum0 = 0.
            sum1 = 0.

            for l in range(m):
                sum0 += ((self.theta0 + (self.theta1 * X[l])) - Y[l])
                sum1 += (((self.theta0 + (self.theta1 * X[l])) - Y[l]) * X[l])

            self.theta0 = self.theta0 - (self.learningRate * (sum0 / float(m)))
            self.theta1 = self.theta1 - (self.learningRate * (sum1 / float(m)))

            currentCost = self.cost()
            self.errors.append(currentCost)


descent = GradientDescent(0.1, 1000)
descent.run()
print('Found theta0 [{}] theta1 [{}]'.format(descent.theta0, descent.theta1))

# Save theta
try:
    f = open("theta.res", "w")
    f.write("{}\n{}".format(descent.theta0, descent.theta1))
    f.close()
    print('Saved found thetas.')
except IOError:
    print('Failed to save thetas ?')

# Mileage and price plot
plt.subplot(211)
plt.xlabel('Normalized Price')
plt.ylabel('Normalized Mileage')
plt.scatter(X, Y, color='blue')
plt.plot([min(X), max(X)], [descent.theta0 + (descent.theta1 * min(X)),
                            descent.theta0 + (descent.theta1 * max(X))])

# Cost over iterations
plt.subplot(212)
plt.xlabel('Iterations')
plt.ylabel('Mean square error')
plt.plot(descent.errors)

plt.show()

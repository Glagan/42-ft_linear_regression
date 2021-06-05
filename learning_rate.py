"""
Calculate the mean square error with different learning rates with a few iterations to see the best one.
"""

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
        print('alpha {}\n> theta0 {}\n> theta1 {}'.format(self.learningRate,
              self.theta0, self.theta1))


reports = []
steps = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]
for step in steps:
    descent = GradientDescent(step, 1000)
    descent.run()
    reports.append([descent.theta0, descent.theta1, descent.learningRate])
    errors.append(descent.errors)

# Mileage and price plot
plt.subplot(211)
plt.xlabel('Normalized Price')
plt.ylabel('Normalized Mileage')
plt.scatter(X, Y, color='blue')
for report in reports:
    plt.plot([min(X), max(X)], [report[0] + (report[1] * min(X)),
                                report[0] + (report[1] * max(X))], label="α = {}".format(report[2]))
plt.legend()

# Cost over iterations
plt.subplot(212)
plt.xlabel('Iterations')
plt.ylabel('Mean square error')
for i in range(len(errors)):
    plt.plot(list(range(1000)), errors[i],
             label="α = {}".format(reports[i][2]))
plt.legend()

plt.show()

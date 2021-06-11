import sys
import matplotlib.pyplot as plt
import src.GradientDescent as gd
import src.Normalizer as nm
import src.DatasetReader as dr

# Dataset
oX, oY, X, Y = dr.read()

# Run Gradient Descent for different learning rates
reports = []
errors = []
steps = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]
for step in steps:
    descent = gd.GradientDescent(X, Y, step, 1000)
    theta0norm, theta1norm, currentErrors = descent.run()
    theta0, theta1 = nm.minMaxDenormalize(X, Y, oX, oY, theta0norm, theta1norm)
    reports.append([theta0, theta1, step])
    errors.append(currentErrors)

# Mileage and price plot
plt.subplot(211)
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.scatter(oX, oY, color='blue')
xMin, xMax = min(oX), max(oX)
for report in reports:
    plt.plot([xMin, xMax], [report[0] + (report[1] * xMin),
                            report[0] + (report[1] * xMax)], label="α = {}".format(report[2]))
plt.legend(loc='upper right')

# Cost over iterations
plt.subplot(212)
plt.xlabel('Iterations')
plt.ylabel('Sum square error')
for i in range(len(errors)):
    plt.plot(list(range(1000)), errors[i],
             label="α = {}".format(reports[i][2]))
plt.legend()

plt.show()

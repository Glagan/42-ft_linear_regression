import sys
import matplotlib.pyplot as plt
import src.GradientDescent as gd
import src.Normalizer as nm
import src.DatasetReader as dr

# Dataset
oX, oY, X, Y = dr.read()

# Run
descent = gd.GradientDescent(X, Y, 0.1, 1000)
theta0norm, theta1norm, errors = descent.run()
print('Found\ttheta0norm [{}] theta1norm [{}]'.format(theta0norm, theta1norm))
theta0, theta1 = nm.minMaxDenormalize(X, Y, oX, oY, theta0norm, theta1norm)
print('\ttheta0 [{}] theta1 [{}]'.format(theta0, theta1))

# Save theta
# Denormalized to use h(x) directly without the min and max parameters
try:
    f = open("theta.res", "w")
    f.write("{}\n{}".format(theta0, theta1))
    f.close()
    print('Saved found thetas.')
except IOError:
    print('Failed to save thetas ?')

# Mileage and price plot
plt.subplot(211)
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.scatter(oX, oY, color='blue')
xMin, xMax = min(oX), max(oX)
plt.plot([xMin, xMax], [theta0 + (theta1 * xMin),
                        theta0 + (theta1 * xMax)])

# Cost over iterations
plt.subplot(212)
plt.xlabel('Iterations')
plt.ylabel('Sum square error')
plt.plot(errors)

plt.show()

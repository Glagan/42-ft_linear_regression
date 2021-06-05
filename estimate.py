import sys

# Find mileage, as a parameter or taken as an input
if len(sys.argv) != 2:
    mileageStr = input('Mileage: ')
    mileage = float(mileageStr)
else:
    mileage = float(sys.argv[1])

# Find theta
theta0 = 0.
theta1 = 0.
try:
    with open('theta.res') as file:
        lines = file.readlines()
        theta0 = float(lines[0])
        theta1 = float(lines[1])
except IOError:
    print('No theta saved, use train.py first !')

# Estimate
prediction = theta0 + (theta1 * mileage)
print('Price for mileage {} -> {}'.format(mileage, prediction))

import sys

if len(sys.argv) != 2:
    print('Missing mileage to predict !')
    exit()

# normalize: (mileage - min(x)) / (max(x) - min(x))
mileage = float(sys.argv[1])
theta0 = 0.
theta1 = 0.

# Find theta
try:
    with open('theta.res') as file:
        lines = file.readlines()
        theta0 = float(lines[0])
        theta1 = float(lines[1])
except IOError:
    print('No theta saved, use train.py first !')

# Estimate
# Returns a normalized prediction which needs to be denormalized
# ((theta0 + (theta1 * mileage)) * (max(y) - min(y))) + min(y)
normalizedMileage = (mileage - 22899) / (240000 - 22899)
prediction = ((theta0 + (theta1 * normalizedMileage)) * (8290 - 3650)) + 3650
print('Price for mileage {} -> {}'.format(mileage, prediction))

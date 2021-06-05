
def minMaxNormalize(val, min, max):
    return (val - min) / (max - min)


def minMaxNormalizeList(list, min, max):
    return [minMaxNormalize(i, min, max) for i in list.copy()]


def minMaxDenormalize(X, Y, oX, oY, theta0, theta1):
    x0, x1 = oX[0], oX[1]
    x0n, x1n = X[0], X[1]
    y0n = theta1 * x0n + theta0
    y1n = theta1 * x1n + theta0
    yMin, yMax = min(oY), max(oY)
    priceRange = yMax - yMin
    theta0 = (x1 / (x1 - x0)) * (y0n * priceRange +
                                 yMin - (x0 / x1 * (y1n * priceRange + yMin)))
    y0 = oY[0]
    theta1 = (y0 - theta0) / x0
    return theta0, theta1

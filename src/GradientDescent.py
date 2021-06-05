class GradientDescent:
    def __init__(self, X, Y, learningRate, iterations):
        self.learningRate = learningRate
        self.iterations = iterations
        self.theta0 = 0.
        self.theta1 = 0.
        self.errors = []
        self.X = X
        self.Y = Y
        self.m = len(self.X)

    def cost(self):
        errorSum = 0.
        for l in range(self.m):
            errorSum += (((self.theta0 + (self.theta1 *
                         self.X[l])) - self.Y[l]) ** 2)
        return errorSum / float(self.m)

    def run(self):
        for i in range(self.iterations):
            sum0 = 0.
            sum1 = 0.

            for l in range(self.m):
                sum0 += ((self.theta0 + (self.theta1 * self.X[l])) - self.Y[l])
                sum1 += (((self.theta0 + (self.theta1 *
                         self.X[l])) - self.Y[l]) * self.X[l])

            self.theta0 = self.theta0 - \
                (self.learningRate * (sum0 / float(self.m)))
            self.theta1 = self.theta1 - \
                (self.learningRate * (sum1 / float(self.m)))

            currentCost = self.cost()
            self.errors.append(currentCost)
        return self.theta0, self.theta1, self.errors

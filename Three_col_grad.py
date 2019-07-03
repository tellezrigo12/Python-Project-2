from Gradient import Gradient
class Three_col_grad(Gradient):
    def __init__(self, col1, col2, col3, steps):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.steps = steps
    def make3ColGrad(self):
        firstHalf = self.linearInterpolate(self.col1, self.col2, self.steps)
        secondHalf = self.linearInterpolate(self.col2, self.col3, self.steps)
        return firstHalf + secondHalf

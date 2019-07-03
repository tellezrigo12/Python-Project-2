from Gradient import Gradient
class TwoColGrad(Gradient):
    def __init__(self, col1, col2, steps):
        self.col1 = col1
        self.col2 = col2
        self.steps = steps
    def makeGrad(self):
        return self.linearInterpolate(self.col1, self.col2, self.steps)


from Gradient import Gradient
class MultiColorGrad(Gradient):
    def __init__(self, colors, steps):
        self.colors = colors
        self.steps = steps
    def makeInterestingGradient(self):
        parts = []
        for i in range(len(self.colors)):
            parts = parts + self.linearInterpolate(self.colors[i], [0,0,0], self.steps)
        return parts
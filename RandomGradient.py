from Gradient import Gradient
import random
class RandomGradient(Gradient):
    def __init__(self,numColors , steps):
        self.steps = steps
        self.max = numColors
    def makeRandomGradient(self):
        colorList = []
        for i in range(self.max):
            subList = []
            for j in range(3):
                randomPart = random.randint(0,255)
                subList.append(randomPart)
            colorList.append(subList)
            subList =[]
        parts = []
        for i in range(self.max - 1):
            parts = parts + self.linearInterpolate(colorList[i], colorList[i+1], self.steps)
        return parts
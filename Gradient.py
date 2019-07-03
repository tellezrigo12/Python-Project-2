
class Color():
    #making a color based on the values given
    def __init__(self, r, g, b):
        self.setRed(r)
        self.setGreen(g)
        self.setBlue(b)

    def setRed(self, r):
        """Setter for Red color channel which ensures value is in-range"""
        if r < 0:
            self.r = 0
        elif r > 255:
            self.r = 255
        else:
            self.r = int(r)


    def setGreen(self, g):
        if g < 0:
            self.g = 0
        elif g > 255:
            self.g = 255
        else:
            self.g = int(g)


    def setBlue(self, b):
        if b < 0:
            self.b = 0
        elif b > 255:
            self.b = 255
        else:
            self.b = int(b)


    def __str__(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def __repr__(self):
        return self.__str__()



class Gradient:
    #start with by makeing an objects with the tools to make a
    #gradient
    def __init__(self):
        raise NotImplementedError("Gradients cannot be instantiated.")
    def linearInterpolate(self,start, end, steps):
        deltaRed = (end[0] - start[0]) / (steps- 1)
        deltaGreen = (end[1] - start[1]) / (steps-1)
        deltaBlue = (end[2] - start[2]) / (steps-1)
        return list(map(lambda n: Color((n*deltaRed) + start[0],
                                             (n*deltaGreen) + start[1],
                                             (n*deltaBlue) + start[2]), range(steps)))








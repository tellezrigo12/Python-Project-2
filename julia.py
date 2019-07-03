#!/usr/bin/python3

## Julia Set Visualizer

import ImagePainter
import GradientFactory
import sys
from Fractal import Fractal

class Julia(Fractal):
    def __init__(self, imageFractal, name):
        self.__dict = imageFractal
        self.name = name[:-5]
        self.c = complex(self.__dict['creal'], self.__dict['cimag'])
        self.makePicture()

    def makePicture(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas. Asks the user
            for what type of image they want to create(more information given in the manual).
            This function displays a really handy status bar so you can see how far along
            in the process the program is."""
        factoryObj = GradientFactory.GradientFactory()
        grad = factoryObj.makeDifferentGradient((self.__dict['iterations']), sys.argv)
        Painter = ImagePainter.ImagePainter(self.__dict['pixels'])


        minimum = ((self.__dict['centerx'] - (self.__dict['axislength'] / 2.0)),
                   (self.__dict['centery'] - (self.__dict['axislength'] / 2.0)))

        maximum = ((self.__dict['centerx'] + (self.__dict['axislength'] / 2.0)),
                   (self.__dict['centery'] + (self.__dict['axislength'] / 2.0)))
        size = abs(maximum[0] - minimum[0]) / self.__dict['pixels']
        fraction = int(self.__dict['pixels'] / 64)
        photoType = '.png'
        self.name = self.name + photoType
        for c in range(self.__dict['pixels']):
            if c % fraction == 0:
                # Update the status bar each time we complete 1/64th of the rows
                dots = c // fraction
                percent = c / 1024
                print(f"{self.name}({self.__dict['pixels']} x {self.__dict['pixels']}) "
                      f"{'=' * dots}{'_' * (64 - dots)} {percent:.0%}", end='\r',
                      file=sys.stderr)
            for r in range(self.__dict['pixels']):
                x = minimum[0] + c * size
                y = minimum[1] + r * size
                count = self.count(complex(x, y), self.c, len(grad),2)
                color = grad[count]
                Painter.img.put(color, (c, r))
        print(f"{self.name} ({self.__dict['pixels']}x{self.__dict['pixels']}) ======================="
              f"========================================= 100%",file=sys.stderr)
        Painter.display(grad, self.name, photoType)
        print(f"Wrote image {self.name}{photoType}")








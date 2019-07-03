#!/usr/bin/python3

## Mandelbrot Set Visualizer



import GradientFactory
import ImagePainter
import sys
from Fractal import Fractal

# TODO: Sometimes I wonder whether my functions really need to be given all of
#       the data I pass to them
class Mandelbrot(Fractal):
    def __init__(self, imageFractal, imageName):
        self.__dict = imageFractal
        self.__imageName = imageName[:-5]
        self.z = complex(0, 0)
        self.makePictute()
    def makePictute(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas. Asks the user
        for what type of image they want to create(more information given in the manual).
        This function displays a really handy status bar so you can see how far along
        in the process the program is."""
        factoryObj = GradientFactory.GradientFactory()
        grad = factoryObj.makeDifferentGradient(self.__dict['iterations'], sys.argv)
        minx = self.__dict['centerx'] - (self.__dict['axislength'] / 2.0)
        maxx = self.__dict['centerx'] + (self.__dict['axislength'] / 2.0)
        miny = self.__dict['centery'] - (self.__dict['axislength'] / 2.0)
        maxy = self.__dict['centery'] + (self.__dict['axislength'] / 2.0)
        pixelsize = abs(maxx - minx) / self.__dict['pixels']
        portion = int(self.__dict['pixels']/64)
        Painter = ImagePainter.ImagePainter(self.__dict['pixels'])
        # Display the image on the screen
        imageType = '.png'
        self.__imageName = self.__imageName + imageType
        for col in range(self.__dict['pixels']):
            if col % portion == 0:
                # Update the status bar each time we complete 1/64th of the rows
                pips = col // portion
                pct = col / self.__dict['pixels']
                print(f"{self.__imageName}({self.__dict['pixels']}x{self.__dict['pixels']})"
                      f" {'=' * pips}{'_' * (64 - pips)} {pct:.0%}", end='\r', file=sys.stderr)
            for row in range(self.__dict['pixels']):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                count = self.count(self.z, complex(x,y), len(grad),2)
                color = grad[count]
                Painter.img.put(color, (col, row))
        print(f"{self.__imageName} ({self.__dict['pixels']}x{self.__dict['pixels']}) ================================================================ 100%",
              file=sys.stderr)
        Painter.display(grad, self.__imageName,imageType)
        print(f"Wrote image {self.__imageName}")





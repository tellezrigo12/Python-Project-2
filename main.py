import FractalFactory
import sys
#get the command line argument and use that to create the mandelbrot or
#julia file
makeImge = FractalFactory.FractalFactory(sys.argv[1])
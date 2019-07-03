
import mandelbrot
import julia
import Mandelbrot4

class FractalFactory():
    #get the basic information out of the file to create either a Julia or Mandelbort
    def __init__(self, file):
        self.__fileName = file.strip('data/')
        if file == '':
            print("Please enter a fractal configuration file.")
            sys.exit(0)
        self.fracfile = file
        self.makeFractal()
    def makeFractal(self):
        with open( self.fracfile, 'r') as fracFile:
            imageType = ''
            goodFiles = ['Mandelbrot', 'mandelbrot', 'Julia', 'julia', 'Mandelbrot4']
            for i in fracFile:
                if ':' in i:
                    imageType = i.split(':')[1]
                    imageType = imageType.strip('\n')
                    imageType = imageType.strip(' ')
                    if imageType in goodFiles:
                        break

        if imageType == '':
            print("Please have colon separated values")
            print("The following are examples below")
            print("type: Julia")
            print("pixels: 640")
        self.__type = imageType
        if self.__type == 'Mandelbrot' or self.__type == 'mandelbrot':
            self.__makeMandelbrot()
        elif self.__type == 'Julia' or self.__type == "julia":
            self.__makeJulia()
        elif self.__type == 'Mandelbrot4':
            self.__makeMandelbrot4()
        else:
            print('Improper frac file please look at one in the data file for an example')

    def __makeMandelbrot(self):
        #make a dictionary that has all of the values that the .frac file gave you
        #then make a mandelbrot
        with open(self.fracfile, 'r') as fracFile:
            mandelbrotDict = dict()
            infoName = ''
            info = ''
            for i in fracFile:
                if ':' in i:
                    infoName = i.split(':')[0]
                    infoName = infoName.strip('\n')
                    infoName = infoName.lower()
                    info = i.split(':')[1]
                    info = info.strip('\n')
                    info = info.strip(' ')
                    if infoName == 'pixels' or infoName == 'iterations':
                        mandelbrotDict[infoName] = int(info)
                    elif infoName != 'type':
                        mandelbrotDict[infoName] = float(info)
                    else:
                        mandelbrotDict[infoName] = info
        mandelbrot.Mandelbrot(mandelbrotDict,self.__fileName)
    def __makeJulia(self):
        # make a dictionary that has all of the values that the .frac file gave you
        # then make a julia file
        with open(self.fracfile, 'r') as fracFile:
            JuliaDict = dict()
            infoName = ''
            info = ''
            count = 0
            for i in fracFile:
                if ':' in i:
                    infoName = i.split(':')[0]
                    infoName = infoName.strip('\n')
                    infoName = infoName.lower()
                    info = i.split(':')[1]
                    info = info.strip('\n')
                    info = info.strip(' ')
                    if infoName == 'pixels' or infoName == 'iterations' or infoName == 'Iterations':
                        if infoName == 'Iterations':
                            infoName = 'iterations'
                        JuliaDict[infoName] = int(info)
                    elif infoName != 'type':
                        JuliaDict[infoName] = float(info)
                    else:
                        JuliaDict[infoName] = info
        julia.Julia(JuliaDict, self.__fileName)
    def __makeMandelbrot4(self):
        with open(self.fracfile, 'r') as fracFile:
            MandelBrot4Dict = dict()
            infoName = ''
            info = ''
            count = 0
            for i in fracFile:
                if ':' in i:
                    infoName = i.split(':')[0]
                    infoName = infoName.strip('\n')
                    infoName = infoName.lower()
                    info = i.split(':')[1]
                    info = info.strip('\n')
                    info = info.strip(' ')
                    if infoName == 'pixels' or infoName == 'iterations' or infoName == 'Iterations':
                        if infoName == 'Iterations':
                            infoName = 'iterations'
                        MandelBrot4Dict[infoName] = int(info)
                    elif infoName != 'type':
                        MandelBrot4Dict[infoName] = float(info)
                    else:
                        MandelBrot4Dict[infoName] = info
        Mandelbrot4.Mandelbrot4(MandelBrot4Dict, self.__fileName)









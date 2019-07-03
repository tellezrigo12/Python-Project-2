import Three_col_grad
import TwoColGrad
import MultiColorGrad
import RandomGradient


class GradientFactory():
    def __init__(self):
        pass
    def makeDifferentGradient(self, maxSteps, commandArg):
        gradient = []
        str = 'randomness'
        if len(commandArg) < 3:
            print('GradientFactory: No gradient specified creating default black and white color gradient')
            TwoColObj = TwoColGrad.TwoColGrad([0,0,0], [255,255,255], maxSteps)
            gradient = TwoColObj.makeGrad()
            return gradient
        elif commandArg[2] == 'wbb':
            print("GradientFactory: Creating White Blue Black gradient")
            ThreeColObj = Three_col_grad.Three_col_grad([255,255,255], [0,0,255], [0,0,0], maxSteps//2)
            gradient = ThreeColObj.make3ColGrad()
            difference = 4 * ((maxSteps) // 4) - maxSteps
            if difference != 0:
                for i in range(difference):
                    gradient.append('#ffffff')
        elif commandArg[2] == 'yrg':
            print("GradientFactory: Creating Yellow Red Green gradient")
            ThreeColObj = Three_col_grad.Three_col_grad([255,255,0], [255,0,0], [0,255,0], maxSteps//2)
            gradient = ThreeColObj.make3ColGrad()
            difference = 2 * ((maxSteps) // 2) - maxSteps
            if difference != 0:
                for i in range(difference):
                    gradient.append('#ffffff')
        elif commandArg[2] == 'aquaBlack':
            print('GradientFactory: Creating Aqua Black gradient')
            TwoColObj = TwoColGrad.TwoColGrad([0,255,255], [48,48,48], maxSteps)
            gradient = TwoColObj.makeGrad()
        elif commandArg[2]  == 'manyColors0':
            print('GradientFactory: Creating a gradient with many colors')
            colorList = [[0,255,255], [255,215,0], [34,139,34], [220,20,60], [32,100,30],
                         [0, 100, 30], [255,20,147]]
            MultiColorObj = MultiColorGrad.MultiColorGrad(colorList, (maxSteps)//4)
            gradient = MultiColorObj.makeInterestingGradient()
            difference = 4*((maxSteps) // 4) - maxSteps
            if difference != 0:
                for i in range(difference):
                    gradient.append('#ffffff')
        elif commandArg[2] == 'manyColors1':
            print('GradientFactory: Creating a gradient with many colors')
            colorList = [[255,20,147], [47,79,79], [25,25,112], [0,128,128] ,[255,255,0] ,
                         [220,20,60], [255,165,0]]
            MultiColorObj = MultiColorGrad.MultiColorGrad(colorList, (maxSteps)//7)
            gradient = MultiColorObj.makeInterestingGradient()
            difference = 7 * ((maxSteps) // 7) - maxSteps
            if difference != 0:
                for i in range(difference):
                    gradient.append('#ffffff')
        elif commandArg[2] == 'randomness':
            print('GradientFactory: Creating a random gradient')
            randomGradObj = RandomGradient.RandomGradient(7, (maxSteps)//7)
            gradient = randomGradObj.makeRandomGradient()
            difference = 7 * ((maxSteps) // 7) - maxSteps
            if difference != 0:
                for i in range(difference):
                    gradient.append('#ffffff')
        else:
            print(f'GradientFactory: Unknown gradient {sys.argv[2]}; creating default black and white color gradient')
            TwoColObj = TwoColGrad.TwoColGrad([0,0,0], [255,255,255], maxSteps)
            gradient = TwoColObj.makeGrad()
        return gradient
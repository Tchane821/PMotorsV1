from threading import Thread as T
import matplotlib.pyplot as plt
import random as pif

class AfficheurPlot(T):

    def __init__(self, tabPts):
        T.__init__(self)
        self.tabPts = tabPts

    def run(self):
        plt.ion()
        self.setLabelGraphe()
        self.centreAxes()
        self.setdraw()
        for i in range(50):
            self.update()
            self.setdraw()
            plt.draw()
            plt.pause(0.0001)
            plt.clf()

    def setdraw(self):
        x, y = self.splitterAffichageMPLxy(self.tabPts)
        plt.scatter(x, y)

    def setLabelGraphe(self):
        fig = plt.figure("Affichage")
        plt.title("Univer:")
        plt.xlabel('x')
        plt.ylabel('y')
        return fig

    def centreAxes(self):
        # centré le repere -------------------------------------------
        ax = plt.gca()
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

    def splitterAffichageMPLxy(self, tabPoints):
        x = []
        y = []
        for i in range(tabPoints.__len__()):
            x.append(tabPoints[i].posX)
            y.append(tabPoints[i].posY)
        return x, y

    def update(self):
        for p in self.tabPts:
            p.posX += pif.uniform(-1, 1)
            p.posY += pif.uniform(-1, 1)

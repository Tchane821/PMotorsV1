from threading import Thread as T
import matplotlib.pyplot as plt


class AfficheurPlot(T):

    def __init__(self, tabPts,inte):
        T.__init__(self)
        self.tabPts = tabPts
        self.integr = inte

    def run(self):
        plt.ion()
        self.setLabelGraphe()
        self.centreAxes()
        self.setdraw()
        for i in range(500):
            self.update()
            self.setdraw()
            self.centreAxes()
            plt.draw()
            plt.pause(0.00001)
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
        ax.set_xlim([-20,20])
        ax.set_ylim([-20,20])
        ax.grid(True)
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

    def splitterAffichageMPLxy(self, tabPoints):
        x = []
        y = []
        for i in range(tabPoints.__len__()):
            x.append(tabPoints[i].position.posX)
            y.append(tabPoints[i].position.posY)
        return x, y

    def update(self):
        for o in self.tabPts:
            self.integr.majObjet(o)
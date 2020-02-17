from threading import Thread as T
import matplotlib.pyplot as plt


def splitterAffichageMPLxy(tabPoints):
    x = []
    y = []
    for i in range(tabPoints.__len__()):
        x.append(tabPoints[i].posX)
        y.append(tabPoints[i].posY)
    return x, y

class AfficheurPlot(T):

    def __init__(self,tabPts):
        T.__init__(self)
        self.tabPts = tabPts


    def run(self):
        plt.figure("Affichage")
        plt.title("Univer:")
        plt.xlabel('x')
        plt.ylabel('y')
        # centré le repere -------------------------------------------
        ax = plt.gca()
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

        x, y = splitterAffichageMPLxy(self.tabPts)
        plt.scatter(x, y)
        plt.show()

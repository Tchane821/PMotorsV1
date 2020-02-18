import numpy as np
import random as pif


class Point:
    def __init__(self, x, y):
        self.posX = x
        self.posY = y

    def somme(self, p2):
        return Point(p2.posX + self.posX, p2.posY + self.posY)

    def multiplie(self, p2):
        return Point(p2.posX * self.posX, p2.posY * self.posY)

    def distance(self, p2):
        return np.sqrt((p2.posX - self.posX) ** 2 + (p2.posY - self.posY) ** 2)

    def randPoints(self, nb, min, max):
        tabPts = []
        for i in range(nb):
            tabPts.append(Point(pif.uniform(min, max), pif.uniform(min, max)))
        return tabPts

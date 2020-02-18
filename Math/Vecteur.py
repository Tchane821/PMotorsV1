import numpy as np


class Vecteur:
    def __init__(self, x, y):
        self.compX = x
        self.compY = y

    def somme(self, v2):
        return Vecteur(self.compX + v2.compX, self.compY + v2.compY)

    def norme(self):
        return np.sqrt(self.compX ** 2 + self.compY ** 2)

    def multiplieParK(self, k):
        return Vecteur(self.compX * k, self.compY * k)

    def diviserParK(self, k):
        return Vecteur(self.compX / k, self.compY / k)

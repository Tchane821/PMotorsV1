from Math.Vecteur import Vecteur


class PhysiqueGenerale:
    def __init__(self, objs):
        self.objets = objs
        self.G = 6.674 * 10 ** -11

    def attractionAB(self, a, b):
        ab = Vecteur(b.posX - a.posY, b.posY - a.posY)
        uAB = ab.diviserParK(ab.norme())
        kRatio = self.G * ((a.masse * b.masse) / a.position.distance(b) ** 2)
        res = uAB.multiplieParK(kRatio)
        return res

    def acceleration(self, obj):
        va = Vecteur(0, 0)
        for cobj in self.objets:
            if obj != cobj:
                va = va.somme(self.attractionAB(obj, cobj))
        va = va.diviserParK(obj.masse)
        return va

from Math.Vecteur import Vecteur


class PhysiqueGenerale:
    def __init__(self, objs):
        self.objets = objs
        self.G = 0.01

    def attractionAB(self, a, b):
        ab = Vecteur(b.position.posX - a.position.posX, b.position.posY - a.position.posY)
        uAB = ab.diviserParK(ab.norme())
        kRatio = self.G * ((a.masse * b.masse) / a.position.distance(b.position) ** 2)
        res = uAB.multiplieParK(kRatio)
        return res

    def acceleration(self, obj):
        va = obj.acceleration
        for cobj in self.objets:
            if obj != cobj:
                va = va.somme(self.attractionAB(obj, cobj))
        va = va.diviserParK(obj.masse)
        obj.acceleration = obj.acceleration.somme(va)

    def prochaineVitesse(self, obj, dt):
        return Vecteur(obj.vitesse.compX + obj.acceleration.multiplieParK(dt).compX,
                       obj.vitesse.compY + obj.acceleration.multiplieParK(dt).compY)

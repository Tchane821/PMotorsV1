from Integrateur.PhysiqueGenerale import PhysiqueGenerale
from Math.Point import Point
from Math.Vecteur import Vecteur


class ILeapFrog(PhysiqueGenerale):
    def __init__(self, objs, dt):
        super().__init__(objs)
        self.dt = dt
        self.first = True

    def prochaineVitesse(self, obj, dt):
        return Vecteur(obj.vitesse.compX + obj.acceleration.multiplieParK(dt).compX,
                       obj.vitesse.compY + obj.acceleration.multiplieParK(dt).compY)

    def prochainePosition(self, obj, dt):
        return Point(obj.position.posX + obj.vitesse.multiplieParK(dt).compX,
                     obj.position.posY + obj.vitesse.multiplieParK(dt).compY)

    def majObjet(self, obj):
        obj.acceleration = self.acceleration(obj)
        if self.first:
            obj.vitesse = self.prochaineVitesse(obj, 0.5 * self.dt)
            obj.position = self.prochainePosition(obj, self.dt)
            self.first = False
        else:
            obj.vitesse = self.prochaineVitesse(obj, self.dt)
            obj.position = self.prochainePosition(obj, self.dt)

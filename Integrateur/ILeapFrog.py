from Integrateur.PhysiqueGenerale import PhysiqueGenerale
from Math.Point import Point
from Math.Vecteur import Vecteur


class ILeapFrog(PhysiqueGenerale):
    def __init__(self, objs, dt):
        super(objs)
        self.deltaT = dt
        self.boolean = True

    def prochaineVitesse(self, obj, dt):
        return Vecteur(obj.vitesse.compX + obj.acceleration.multiplieparK(dt).compX,
                       obj.vitesse.compY + obj.acceleration.multiplieparK(dt).compY)

    def prochainePosition(self, obj, dt):
        return Point(obj.position.posX + obj.vitesse.multiplieparK(dt).compX,
                     obj.position.posY + obj.vitesse.multiplieparK(dt).compY)

    def majObjet(self, obj, dt):
        obj.acceleration = super.acceleration(obj, dt)
        if self.first:
            obj.vitesse = self.prochaineVitesse(obj, 0.5 * dt)
            obj.position = self.prochainePosition(obj, dt)
            self.first = False
        else:
            obj.vitesse = self.prochaineVitesse(obj, dt)
            obj.position = self.prochainePosition(obj, dt)

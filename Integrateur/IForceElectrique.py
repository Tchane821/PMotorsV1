from Integrateur.PhysiqueGenerale import PhysiqueGenerale
from Math.Vecteur import Vecteur


class IForceElectrique(PhysiqueGenerale):
    def __init__(self, objs,dt):
        super().__init__(objs)
        self.dt = dt
        self.objs = objs
        self.C = 890000

    def attractionElectriqueAB(self, a, b):
        ab = Vecteur(b.position.posX - a.position.posX, b.position.posY - a.position.posY)
        uAB = ab.diviserParK(ab.norme())
        F = a.charge * ((self.C * b.charge) / ab.norme())
        print("F= ",F)
        print("uabX =",uAB.compX,"uabY =",uAB.compY)
        return uAB.multiplieParK(F)

    def majObjetElec(self, obj):
        va = obj.acceleration
        for cobj in self.objs:
            if(cobj != obj):
                va = va.somme(self.attractionElectriqueAB(cobj, obj))
                print("elecAcce X= ",va.compX," Y= ",va.compY)
        obj.acceleration = obj.acceleration.somme(va)

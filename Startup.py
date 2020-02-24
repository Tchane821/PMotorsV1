import AffichageBasique.AfficheurPlot as afp
from Entiter.Object import Object
from Integrateur.IForceElectrique import IForceElectrique
from Integrateur.ILeapFrog import ILeapFrog
from Math.Point import Point
from Math.Vecteur import Vecteur


def main():
    #tabPoints = p.Point(0, 0).randPoints(100, -10, 10)
    terre = Object("terre",30, Point(0, 0), Vecteur(0, 0), Vecteur(0, 0),0)
    mars = Object("mars",5, Point(0,5), Vecteur(-0.25, 0), Vecteur(0, 0),0)
    positron = Object("positron",0,Point(0,0),Vecteur(0,0),Vecteur(0,0),0.00001)
    electron = Object("electron",0,Point(5,0),Vecteur(0,0),Vecteur(0,0),-0.00001)

    deltaT = 0.75
    #tabObjets = [terre,mars]
    tabObjets = [positron,electron]
    intePhysique = ILeapFrog(tabObjets,deltaT)
    inteElectrique = IForceElectrique(tabObjets,deltaT)
    th1 = afp.AfficheurPlot(tabObjets,intePhysique,inteElectrique)
    th1.start()
    th1.join()


if __name__ == '__main__':
    main()

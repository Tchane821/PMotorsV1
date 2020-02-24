import AffichageBasique.AfficheurPlot as afp
import Math.Point as p
from Entiter.Object import Object
from Integrateur.ILeapFrog import ILeapFrog
from Math.Vecteur import Vecteur


def main():
    #tabPoints = p.Point(0, 0).randPoints(100, -10, 10)
    terre = Object(30, p.Point(0, 0), Vecteur(0, 0), Vecteur(0, 0))
    mars = Object(5, p.Point(0,5), Vecteur(-0.25, 0), Vecteur(0, 0))
    tabObjets = [terre,mars]
    integrateur = ILeapFrog(tabObjets,1)
    th1 = afp.AfficheurPlot(tabObjets,integrateur)
    th1.start()
    th1.join()


if __name__ == '__main__':
    main()

import AffichageBasique.AfficheurPlot as afp
import Math.Point as p


def main():
    tabPoints = p.Point(0, 0).randPoints(100, -10, 10)

    th1 = afp.AfficheurPlot(tabPoints)
    th1.start()
    th1.join()


if __name__ == '__main__':
    main()

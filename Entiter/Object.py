class Object:
    # m un float / p un point , v et a un vecteur
    def __init__(self, n, m, p, v, a, q):
        self.nom = n
        self.masse = m
        self.position = p
        self.vitesse = v
        self.acceleration = a
        self.charge = q

    def afficher(self):
        print("Nom = ", self.nom)
        print("Masse = ", self.masse)
        print("PosX = ", self.position.posX, " posY = ", self.position.posY)
        print("vitX = ", self.vitesse.compX, " vitY = ", self.vitesse.compY)
        print("acceX = ", self.acceleration.compX, " acceY = ", self.acceleration.compY)
        print("Charge = ", self.charge)

from Methode_Cryptage import Methode_Cryptage

class Dechiffrement(Methode_Cryptage):
    res = []
    def Dechiffrement_Cesar(self):
        # Dechiffrer le message dans res
        for lettre in self.sms:
            self.x = self.nemeroL(lettre)
            self.y = self.Cesar_Dk(self.x, self.cle)
            self.Ck = self.lettre(self.y)
            self.ajouter(self.res, self.Ck)
        # MD : message déchiffré
        MD = ''.join(self.res)

        # Liberer la chaine res
        for i in range(len(self.res)):
            self.res.pop()

        return MD

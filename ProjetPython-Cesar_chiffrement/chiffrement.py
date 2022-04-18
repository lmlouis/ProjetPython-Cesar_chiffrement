from Methode_Cryptage import Methode_Cryptage

class Chiffrement(Methode_Cryptage):
    res = []
    def Chiffrement_Cesar(self):
        # Chiffrer le message dans res
        for lettre in self.sms:
            self.x = self.nemeroL(lettre)
            self.y = self.Cesar_Ck(self.x, self.cle)
            self.Ck = self.lettre(self.y)
            self.ajouter(self.res, self.Ck)

        # MC :  message chiffré
        MC = ''.join(self.res)

        # Liberer la chaine res
        for i in range(len(self.res)):
            self.res.pop()
            
        return MC

from chiffrement import Chiffrement
from dechiffrement import Dechiffrement

class Cesar(Chiffrement, Dechiffrement):
    
    def __init__(self, sms, cle):
        self.sms = sms
        self.cle = cle

    def Sairsir_sms(self):
        return str(input("----- \n Donner Message à Saisir : \n"))
        
    def Sairsir_cle(self):
        return int(input("----- \n Donner Clé, K de chiffrement comprise [0, 25] : \n"))

    def obtenir_sms(self):
        return self.sms
    
    def modifier_sms(self, value):
        self.sms = value

    def modifier_cle(self, value):
        self.cle = value
    
    def obtenir_cle(self):
        return self.cle

    def toString(self):
        return f"\n Cesar [ Message : {self.obtenir_sms()}   -   K = {self.obtenir_cle()} ]"
    
    def Chiffrer(self):
        self.sms = self.Chiffrement_Cesar()

    def Dechiffrer(self):
        self.sms = self.Dechiffrement_Cesar()
    




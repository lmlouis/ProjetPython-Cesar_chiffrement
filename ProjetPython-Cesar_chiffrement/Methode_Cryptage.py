
class Methode_Cryptage:

    def nemeroL(self, L):
        return ord(L)-65
    
    def Cesar_Ck(self, x, k):
        return (x+k)%26
        
    def Cesar_Dk(self, x, k):
        return (x-k)%26
    
    def lettre(self, x):
        return  chr(x + 65) 
    
    def ajouter(self, result, Ck): 
        result.append(Ck)
    



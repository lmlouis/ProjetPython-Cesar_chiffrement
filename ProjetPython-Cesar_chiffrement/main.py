from Cesar import Cesar
from builtins import str

print("\n")
print('------------------------------------------------------------ \n')
c = Cesar('COUCOU', 11)
print(f" D'abord : \n {c.toString()}")
print("\n")
c.Chiffrer()
print(f" Ensuite Chiffrement : \n {c.toString()}")
print("\n")
c.Dechiffrer()
print(f" Enfin Déchiffrement : \n {c.toString()}")
print("\n")
print('------------------------------------------------------------ \n')
crypter = True
while crypter:
    print("\n")
    print('Voulez-vous Envoyer un message ?  ')
    reponse = str(input("  [O/N]  "))
    print("\n")
    
    if reponse == "O" or reponse == "o" :
        print(' ----------- Création d\'une instance de message chiffé ... \n')
        c = Cesar("", 0)
        print('\n')
        c.modifier_sms(c.Sairsir_sms())
        print(' \n')
        c.modifier_cle(c.Sairsir_cle())
        print(' \n')
        print('Données implementées :) :  \n')
        print('------------------------------------------------------------ \n')
        print('Vous Envoyez un message chriffé ... \n')
        print(c.toString())                 
        print(' \n')
        print('le message est chiffrée en message suivant : \n')
        c.Chiffrer()
        print('Message codé : ',  c.toString())
        print(' \n')
        c.Dechiffrer()
        print('le message est Déchiffrée en message suivant : \n')
        print('Message codé : ',  c.toString())
        print(' \n')


    elif reponse == "N" or reponse == "n":
        print(' ok \n')
        print("\n")
        crypter = False
        
    else:
        crypter = False
        print("\n")
print('Fin ...                                Merci :)')



           # input de notes et calcul de la moyenne
i = 0
somme = 0
for i in range(4):
    
    note= int(input("entre votre note:"))
    while note < 0 or note > 20:
        print("la note est invalide, entrer une note comprise entre 0 et 20:")
        note= int(input("entre votre note:"))

    somme = somme + note
    moyenne = somme // 4
print("la moyenne est:", moyenne)         
question =input("est ce que vous voulez savoir la somme de vos notes? oui/Non  :")
if question == "oui":
        print(somme,"c'est la somme de vos notes:")
elif question == "non":
        print("comme vous voulez")
      ##detirmination se la mention##
message="un simple programme qui va donner le mention de votre moyenne:"
print(message)

port= float(input("enter your moyenne:"))
if port < 0 or port >=20 :
       print ("invalide moyenne")
else:
    if port < 10 and port > 0 :
     print("échec")
    if port == 9 :
        print("proche de la réussite")
    
    elif port >= 10 and port < 12 :
        print("passable")
        if port == 10 :
            print("tous juste admis")
        else: print("travail à améliorer")
    if port >=12 and port < 14 :
            print("assez bien") 
if port >= 14 and port < 16 :
    print("bien")
    
else:
    if port >= 16 and port < 18 :
      print ("trés bien")
    if port  >= 18 and port < 20 :
          print("excellent","felicitation exceptionnel")
print("\n fin du programme au revoir")
            
        


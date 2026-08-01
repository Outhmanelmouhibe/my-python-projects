#####
##message="un simple programme qui va donner le mention de votre note"
print(message)

port= int(input("enter your note:"))
if port < 0 or port >=20 :
       print ("invalide note")
else:
    if port < 10 and port > 0 :
     print("échec")
    if port ==9 :
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
##print("\n fin du programme")
            
        


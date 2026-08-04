personne={
    "othman": {"moyenne": 15, "mention":"bien", "age":20},
    "youssef": {"moyenne": 12, "mention":"satisfaisant", "age":22},
    "rachid": {"moyenne": 14, "mention":"bien", "age":21},
    "ahmed": {"moyenne": 16, "mention":"très bien", "age":23}
    
}
for key,valeu in personne.items():
    print(key,valeu["mention"])
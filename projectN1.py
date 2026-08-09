from tkinter import *
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

rot = Tk()

rot.geometry("1350x500")
rot.title("pharmacy[available pharmacies]")
rot.iconbitmap("iconN1.ico")
rot.configure(background="white")

def coun():
    location = ent.get().strip()
    if not location:
        return
    map.set_address(location, marker=True)
    

#===========tiltle================
title1 = Label(rot,
                text="hello your welcome to our service",
                fg="white",
                bg="grey",
                font=("italic",18),
               )
title1.pack(fill=X)
            #short explination
txd = Label(rot,
    text="Bonjour.Entrer votre nom,pour profiter d'un promotion\npour chaque médicament.",
    fg="black",
    bg="white",
    font=("italic", 16),
    justify=LEFT,
    #wraplength=300,
)
txd.place(x=330, y=50)
    
#================adding image==================
image = Image.open("projectN1.jpg")
image = image.resize((300, 200), Image.LANCZOS)  # use (width, height)
img = ImageTk.PhotoImage(image)
imgg = Label(rot, image=img, bd=2, bg="black")
imgg.image = img
imgg.place(x=5, y=40)
#==========country=====================================
coun_label = Label(rot,text="Entrer votre Nom",font=("italic",12),fg="black",bg="light grey")
coun_label.place(x=10,y=260)
 #===========entery==========================
ent=Entry(rot,font=("Tajweel",14),width=20,bd=2,bg="light grey",relief=GROOVE)    
ent.place(x=140,y=260)
#=================boutom==============================
btn=Button(text="click ici", bg="light grey",fg= "black" ,bd=2,relief="solid",width=12,cursor="hand2" ,command=coun)
btn.place(x=380,y=260) 
#==================chichid location===============
def locations():  # *******************************************same for all pharmacies' locations***********
    global map
    map.set_position(31.641637084255947, -8.000005107230102)
    map.set_zoom(20)
    marker = map.set_marker(31.641637084255947, -8.000005107230102)
    marker.set_text("Harbil / pharmacy Chichid")
#=========================local pharmacies=========================
              #firstpharmacy
but = Button(text="pharmacy Abdsamad",
            
             cursor="hand2",
             bg="white",
             fg="green",
             bd=2,
             relief="solid",
             font=("italic",13),
             width=18
             )
but.place(x=10,y=300)
        #second pharmacy#
but = Button(text="pharmacy Chichid",
             cursor="hand2",
             bg="white",
             fg="green",
             bd=2,
             relief="solid",
             font=("italic",13),
             width=18, command= locations
             )
but.place(x=200,y=300)
        #third pharmacy====
but = Button(text="pharmacy Harbil",
             cursor="hand2",
             bg="white",
             fg="green",
             bd=2,
             relief="solid",
             font=("italic",12),
             width=18
             )
but.place(x=390,y=300)
                  #forth pharmacy
but = Button(text="pharmacy Atlas",
             cursor="hand2",
             bg="white",
             fg="green",
             bd=2,
             relief="solid",
             font=("italic",13),
             width=18
             )
but.place(x=10,y=340) 
               #fifth pharmacy               
but = Button(text="pharmacy Tamnsourt",
             cursor="hand2",
             bg="white",
             fg="green",
             bd=2,
             relief="solid",
             font=("italic",13),
             width=18
             )
but.place(x=200,y=340)
          #sixth pharmacy
but = Button(text="pharmacy Ait mas3od",
             cursor="hand2",
             bg="white",
             fg="green",
             bd=2,
             relief="solid",
             font=("italic",12),
             width=18
             )
but.place(x=390,y=340)
#=====================pharmacies locations===========================

             #map adding=====#
map = TkinterMapView(rot, width=770, height=360, corner_radius=0)
map.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
map.place(x=570, y=80)
map.set_position(31.6295, -7.9811)  # default map center
map.set_zoom(20)
map.set_marker(31.6295, -7.9811, text="Harbil / Tamnsourt")
#=========================phrase under map=================

phr = Label(text="# map des pharmacies de la zone Harbil,Tamnsourt.",
          bg='white',
          fg="black",
          font=("italic",15))
phr.place(x=570,y=460)  
























rot.mainloop()
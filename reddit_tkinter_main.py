from tkinter import *
from random import *
pencere=Tk()
pencere.geometry("300x291")
pencere.title("Yapımcı --> Can Üstün")
x,y=0,0
def tikla_renk_degis(buton):
    renk=["silver","black","white","brown","red","pink","purple","blue","gold","green","gray"]
    buton["bg"] = "blue"
def buton_oluştur():
    global x,y,yeni_button
    if y<=289:
        yeni_button=Button(bg="white")
        yeni_button["command"]=lambda yeni_button=yeni_button: tikla_renk_degis(yeni_button)
        yeni_button.place(x=x,y=y,width=10,height=10)
        x+=10
        if x>=300:
            y+=9
            x=0
    pencere.after(1,buton_oluştur)
    
pencere.after(1,buton_oluştur)
pencere.mainloop()

import tkinter.font as tkFont
import tkinter as tk

#Comandos para botones
def ceroVolt():
    tk.Label(ventana,image=img_0v,relief="solid").place(x=47,y=40, width=150)

def ceroCincoVolt():
    tk.Label(ventana,image=img_0_5v,relief="solid").place(x=47,y=40, width=150)
    
def unVolt():
    tk.Label(ventana,image=img_1v,relief="solid").place(x=47,y=40, width=150)

def unoCincoVolt():
    tk.Label(ventana,image=img_1_5v,relief="solid").place(x=47,y=40, width=150)

def dosVolt():
    tk.Label(ventana,image=img_2v,relief="solid").place(x=47,y=40, width=150)
    
def borrar_visor():
    z1=tk.Label(ventana,image=img_visor_vacio,relief="solid").place(x=47,y=40, width=150)
    

#Crear ventana    
ventana=tk.Tk()

#Imagen de fondo para ventana
img=tk.PhotoImage(file="Imagenes/fondo.png")
lbl=tk.Label(ventana, image=img).pack()

#Botones para elementos
bt_h=tk.Button(ventana, text="H2|H", fg='black',command=ceroVolt).place(x=400,y=110, width=60)
bt_zn=tk.Button(ventana, text="Zn|Zn++", fg='black',command=ceroCincoVolt).place(x=400,y=140, width=60)
bt_ag=tk.Button(ventana, text="Ag|Ag+", fg='black',command=unVolt).place(x=400,y=170, width=60)
bt_fe=tk.Button(ventana, text="Fe|Fe++", fg='black',command=unoCincoVolt).place(x=400,y=200, width=60)
bt_s=tk.Button(ventana, text="S-|S", fg='black',command=dosVolt).place(x=400,y=230, width=60)

#Imagenes para los botones
img_visor_vacio=tk.PhotoImage(file="Imagenes/visor_vacio.png")
img_0v=tk.PhotoImage(file="Imagenes/0v.png")
img_0_5v=tk.PhotoImage(file="Imagenes/0_5v.png")
img_1v=tk.PhotoImage(file="Imagenes/1v.png")
img_1_5v=tk.PhotoImage(file="Imagenes/1_5v.png")
img_2v=tk.PhotoImage(file="Imagenes/2v.png")

#Boton para borrar
bt_borrar=tk.Button(ventana, text="Borrar", fg='black',command=borrar_visor).place(x=250,y=20, width=60)

#Visor inicial vacio
z1=tk.Label(ventana,image=img_visor_vacio,relief="solid").place(x=47,y=40, width=150)

#Mantener ventana abierta y sin posibilidad de maximizar
ventana.resizable(0,0)
ventana.mainloop()


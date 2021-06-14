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

def Al_positivo():
    tk.Label(ventana, image=img_Al_positivo,bd=0).place(x=295,y=261)

def Al_negativo():
    tk.Label(ventana, image=img_Al_negativo,bd=0).place(x=553,y=260)

def Cu_positivo():
    tk.Label(ventana, image=img_Cu_positivo,bd=0).place(x=295,y=261)

def Cu_negativo():
    tk.Label(ventana, image=img_Cu_negativo,bd=0).place(x=553,y=260)    

def Ag_positivo():
    tk.Label(ventana, image=img_Ag_positivo,bd=0).place(x=295,y=261)

def Ag_negativo():
    tk.Label(ventana, image=img_Ag_negativo,bd=0).place(x=553,y=260)

def Zn_positivo():
    tk.Label(ventana, image=img_Zn_positivo,bd=0).place(x=295,y=261)

def Zn_negativo():
    tk.Label(ventana, image=img_Zn_negativo,bd=0).place(x=553,y=260)

def Sn_positivo():
    tk.Label(ventana, image=img_Sn_positivo,bd=0).place(x=295,y=261)

def Sn_negativo():
    tk.Label(ventana, image=img_Sn_negativo,bd=0).place(x=553,y=260)

    
#Crear ventana    
ventana=tk.Tk()

#Imagen de fondo para ventana
img=tk.PhotoImage(file="Imagenes/fondo.png")
lbl=tk.Label(ventana, image=img).pack()

#Imagenes para voltajes
img_visor_vacio=tk.PhotoImage(file="Imagenes/visor_vacio.png")
img_0v=tk.PhotoImage(file="Imagenes/0v.png")
img_0_5v=tk.PhotoImage(file="Imagenes/0_5v.png")
img_1v=tk.PhotoImage(file="Imagenes/1v.png")
img_1_5v=tk.PhotoImage(file="Imagenes/1_5v.png")
img_2v=tk.PhotoImage(file="Imagenes/2v.png")

#Imagenes de elementos positivos
img_Al_positivo=tk.PhotoImage(file="Imagenes/Aluminio_positivo.png")
img_Cu_positivo=tk.PhotoImage(file="Imagenes/Cobre_positivo.png")
img_Ag_positivo=tk.PhotoImage(file="Imagenes/Plata_positiva.png")
img_Zn_positivo=tk.PhotoImage(file="Imagenes/Zinc_positivo.png")
img_Sn_positivo=tk.PhotoImage(file="Imagenes/Estaño_positivo.png")

#Imagenes de elementos negativos
img_Al_negativo=tk.PhotoImage(file="Imagenes/Aluminio_negativo.png")
img_Cu_negativo=tk.PhotoImage(file="Imagenes/Cobre_negativo.png")
img_Ag_negativo=tk.PhotoImage(file="Imagenes/Plata_negativa.png")
img_Zn_negativo=tk.PhotoImage(file="Imagenes/Zinc_negativo.png")
img_Sn_negativo=tk.PhotoImage(file="Imagenes/Estaño_negativo.png")

#Botones para elementos positivos
bt_h_pos=tk.Button(ventana, text="H2 | H", fg='black',command=ceroVolt).place(x=400,y=100, width=70)
bt_zn_pos=tk.Button(ventana, text="Zn | Zn++", fg='black',command=Zn_positivo).place(x=400,y=130, width=70)
bt_ag_pos=tk.Button(ventana, text="Ag | Ag+", fg='black',command=Ag_positivo).place(x=400,y=160, width=70)
bt_fe_pos=tk.Button(ventana, text="Fe | Fe++", fg='black',command=unoCincoVolt).place(x=400,y=190, width=70)
bt_s_pos=tk.Button(ventana, text="S- | S", fg='black',command=dosVolt).place(x=400,y=220, width=70)
bt_al_pos=tk.Button(ventana, text="Al | Al+++", fg='black',command=Al_positivo).place(x=475,y=100, width=70)
bt_cu_pos=tk.Button(ventana, text="Cu | Cu++", fg='black',command=Cu_positivo).place(x=475,y=130, width=70)
bt_fee_pos=tk.Button(ventana, text="Fe | Fe+++", fg='black',command=ceroVolt).place(x=475,y=160, width=70)
bt_feee_pos=tk.Button(ventana, text="Fe++,Fe+++", fg='black',command=ceroVolt).place(x=475,y=190, width=70)
bt_Sn_pos=tk.Button(ventana, text="Sn | Sn++", fg='black',command=Sn_positivo).place(x=475,y=220, width=70)

#Botones para elementos negativos
bt_h_neg=tk.Button(ventana, text="H2 | H", fg='black',command=ceroVolt).place(x=610,y=100, width=70)
bt_zn_neg=tk.Button(ventana, text="Zn | Zn++", fg='black',command=Zn_negativo).place(x=610,y=130, width=70)
bt_ag_neg=tk.Button(ventana, text="Ag | Ag+", fg='black',command=Ag_negativo).place(x=610,y=160, width=70)
bt_fe_neg=tk.Button(ventana, text="Fe | Fe++", fg='black',command=unoCincoVolt).place(x=610,y=190, width=70)
bt_s_neg=tk.Button(ventana, text="S- | S", fg='black',command=dosVolt).place(x=610,y=220, width=70)
bt_al_neg=tk.Button(ventana, text="Al | Al+++", fg='black',command=Al_negativo).place(x=685,y=100, width=70)
bt_cu_neg=tk.Button(ventana, text="Cu | Cu++", fg='black',command=Cu_negativo).place(x=685,y=130, width=70)
bt_fee_neg=tk.Button(ventana, text="Fe | Fe+++", fg='black',command=ceroVolt).place(x=685,y=160, width=70)
bt_feee_neg=tk.Button(ventana, text="Fe++,Fe+++", fg='black',command=ceroVolt).place(x=685,y=190, width=70)
bt_Sn_neg=tk.Button(ventana, text="Sn | Sn++", fg='black',command=Sn_negativo).place(x=685,y=220, width=70)

#Boton para borrar
bt_borrar=tk.Button(ventana, text="Borrar", fg='black',command=borrar_visor).place(x=250,y=20, width=60)

#Visor inicial vacio
z1=tk.Label(ventana,image=img_visor_vacio,relief="solid").place(x=47,y=40, width=150)

#Mantener ventana abierta y sin posibilidad de maximizar
ventana.resizable(0,0)
ventana.mainloop()


import tkinter as tk

#Creacion de ventana
ventana=tk.Tk()

#Imagen de fondo para ventana
img=tk.PhotoImage(file="Imagenes/fondo.png")
lbl=tk.Label(ventana, image=img).pack()
img_voltimetro=tk.PhotoImage(file="Imagenes/modoVoltimetro.png")
img_apagado=tk.PhotoImage(file="Imagenes/modoApagado.png")

#Funciones para insertar imagenes
def borrar_visor():
    tk.Label(ventana,image=img_visor_vacio,borderwidth=0,highlightthickness=0).place(x=47,y=40)

def H_positivo():
    tk.Label(ventana, image=img_H_positivo,bd=0).place(x=295,y=261)

def H_negativo():
    tk.Label(ventana, image=img_H_negativo,bd=0).place(x=553,y=260)

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

def Fee_positivo():
    tk.Label(ventana, image=img_Fee_positivo,bd=0).place(x=295,y=261)
    
def Fee_negativo():
    tk.Label(ventana, image=img_Fee_negativo,bd=0).place(x=553,y=260)

def Feee_positivo():
    tk.Label(ventana, image=img_Feee_positivo,bd=0).place(x=295,y=261)

def Feee_negativo():
    tk.Label(ventana, image=img_Feee_negativo,bd=0).place(x=553,y=260)

def FePt_positivo():
    tk.Label(ventana, image=img_FePt_positivo,bd=0).place(x=295,y=261)

def FePt_negativo():
    tk.Label(ventana, image=img_FePt_negativo,bd=0).place(x=553,y=260)

def S_positivo():
    tk.Label(ventana, image=img_S_positivo,bd=0).place(x=295,y=261)

def S_negativo():
    tk.Label(ventana, image=img_S_negativo,bd=0).place(x=553,y=260)

#Imagenes de elementos positivos
img_H_positivo=tk.PhotoImage(file="Imagenes/Hidrogeno_positivo.png")
img_Al_positivo=tk.PhotoImage(file="Imagenes/Aluminio_positivo.png")
img_Cu_positivo=tk.PhotoImage(file="Imagenes/Cobre_positivo.png")
img_Ag_positivo=tk.PhotoImage(file="Imagenes/Plata_positiva.png")
img_Zn_positivo=tk.PhotoImage(file="Imagenes/Zinc_positivo.png")
img_Sn_positivo=tk.PhotoImage(file="Imagenes/Estaño_positivo.png")
img_Fee_positivo=tk.PhotoImage(file="Imagenes/Hierro++_positivo.png")
img_Feee_positivo=tk.PhotoImage(file="Imagenes/Hierro+++_positivo.png")
img_FePt_positivo=tk.PhotoImage(file="Imagenes/HierroPt_positivo.png")
img_S_positivo=tk.PhotoImage(file="Imagenes/Azufre_positivo.png")

#Imagenes de elementos negativos
img_H_negativo=tk.PhotoImage(file="Imagenes/Hidrogeno_negativo.png")
img_Al_negativo=tk.PhotoImage(file="Imagenes/Aluminio_negativo.png")
img_Cu_negativo=tk.PhotoImage(file="Imagenes/Cobre_negativo.png")
img_Ag_negativo=tk.PhotoImage(file="Imagenes/Plata_negativa.png")
img_Zn_negativo=tk.PhotoImage(file="Imagenes/Zinc_negativo.png")
img_Sn_negativo=tk.PhotoImage(file="Imagenes/Estaño_negativo.png")
img_Fee_negativo=tk.PhotoImage(file="Imagenes/Hierro++_negativo.png")
img_Feee_negativo=tk.PhotoImage(file="Imagenes/Hierro+++_negativo.png")
img_FePt_negativo=tk.PhotoImage(file="Imagenes/HierroPt_negativo.png")
img_S_negativo=tk.PhotoImage(file="Imagenes/Azufre_negativo.png")

#Imagenes para voltajes
img_visor_vacio=tk.PhotoImage(file="Imagenes/visor_vacio.png")
img_0v=tk.PhotoImage(file="Imagenes/0v.png")
img_0_5v=tk.PhotoImage(file="Imagenes/0_5v.png")
img_1v=tk.PhotoImage(file="Imagenes/1v.png")
img_1_5v=tk.PhotoImage(file="Imagenes/1_5v.png")
img_2v=tk.PhotoImage(file="Imagenes/2v.png")
img_0=tk.PhotoImage(file="Imagenes/0.png")
img_1=tk.PhotoImage(file="Imagenes/1.png")
img_2=tk.PhotoImage(file="Imagenes/2.png")
img_3=tk.PhotoImage(file="Imagenes/3.png")
img_4=tk.PhotoImage(file="Imagenes/4.png")
img_5=tk.PhotoImage(file="Imagenes/5.png")
img_6=tk.PhotoImage(file="Imagenes/6.png")
img_7=tk.PhotoImage(file="Imagenes/7.png")
img_8=tk.PhotoImage(file="Imagenes/8.png")
img_9=tk.PhotoImage(file="Imagenes/9.png")
img_menos=tk.PhotoImage(file="Imagenes/-.png")
img_punto=tk.PhotoImage(file="Imagenes/punto.png")
img_vacio=tk.PhotoImage(file="Imagenes/vacio.png")

#Diccionario de mapeo de digitos
diccDigitos = {
    "0": img_0,
    "1": img_1,
    "2": img_2,
    "3": img_3,
    "4": img_4,
    "5": img_5,
    "6": img_6,
    "7": img_7,
    "8": img_8,
    "9": img_9,
    "-": img_menos,
    ".": img_punto,
    "": img_vacio
}

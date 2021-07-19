import tkinter as tk
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Creacion de ventana
ventana=tk.Tk()

#Titulo de la ventana
ventana.title("Equilibrio Redox")

#Imagen de fondo para ventana
img=tk.PhotoImage(file=resource_path("Imagenes\\fondo.png"))
lbl=tk.Label(ventana, image=img).pack()
img_voltimetro=tk.PhotoImage(file=resource_path("Imagenes\modoVoltimetro.png"))
img_apagado=tk.PhotoImage(file=resource_path("Imagenes\modoApagado.png"))

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
img_H_positivo=tk.PhotoImage(file=resource_path("Imagenes\Hidrogeno_positivo.png"))
img_Al_positivo=tk.PhotoImage(file=resource_path("Imagenes\Aluminio_positivo.png"))
img_Cu_positivo=tk.PhotoImage(file=resource_path("Imagenes\Cobre_positivo.png"))
img_Ag_positivo=tk.PhotoImage(file=resource_path("Imagenes\Plata_positiva.png"))
img_Zn_positivo=tk.PhotoImage(file=resource_path("Imagenes\Zinc_positivo.png"))
img_Sn_positivo=tk.PhotoImage(file=resource_path("Imagenes\Estaño_positivo.png"))
img_Fee_positivo=tk.PhotoImage(file=resource_path("Imagenes\Hierro++_positivo.png"))
img_Feee_positivo=tk.PhotoImage(file=resource_path("Imagenes\Hierro+++_positivo.png"))
img_FePt_positivo=tk.PhotoImage(file=resource_path("Imagenes\HierroPt_positivo.png"))
img_S_positivo=tk.PhotoImage(file=resource_path("Imagenes\Azufre_positivo.png"))

#Imagenes de elementos negativos
img_H_negativo=tk.PhotoImage(file=resource_path("Imagenes\Hidrogeno_negativo.png"))
img_Al_negativo=tk.PhotoImage(file=resource_path("Imagenes\Aluminio_negativo.png"))
img_Cu_negativo=tk.PhotoImage(file=resource_path("Imagenes\Cobre_negativo.png"))
img_Ag_negativo=tk.PhotoImage(file=resource_path("Imagenes\Plata_negativa.png"))
img_Zn_negativo=tk.PhotoImage(file=resource_path("Imagenes\Zinc_negativo.png"))
img_Sn_negativo=tk.PhotoImage(file=resource_path("Imagenes\Estaño_negativo.png"))
img_Fee_negativo=tk.PhotoImage(file=resource_path("Imagenes\Hierro++_negativo.png"))
img_Feee_negativo=tk.PhotoImage(file=resource_path("Imagenes\Hierro+++_negativo.png"))
img_FePt_negativo=tk.PhotoImage(file=resource_path("Imagenes\HierroPt_negativo.png"))
img_S_negativo=tk.PhotoImage(file=resource_path("Imagenes\Azufre_negativo.png"))

#Imagenes para voltajes
img_visor_vacio=tk.PhotoImage(file=resource_path("Imagenes\\visor_vacio.png"))
img_0=tk.PhotoImage(file=resource_path("Imagenes\\0.png"))
img_1=tk.PhotoImage(file=resource_path("Imagenes\\1.png"))
img_2=tk.PhotoImage(file=resource_path("Imagenes\\2.png"))
img_3=tk.PhotoImage(file=resource_path("Imagenes\\3.png"))
img_4=tk.PhotoImage(file=resource_path("Imagenes\\4.png"))
img_5=tk.PhotoImage(file=resource_path("Imagenes\\5.png"))
img_6=tk.PhotoImage(file=resource_path("Imagenes\\6.png"))
img_7=tk.PhotoImage(file=resource_path("Imagenes\\7.png"))
img_8=tk.PhotoImage(file=resource_path("Imagenes\\8.png"))
img_9=tk.PhotoImage(file=resource_path("Imagenes\\9.png"))
img_menos=tk.PhotoImage(file=resource_path("Imagenes\-.png"))
img_punto=tk.PhotoImage(file=resource_path("Imagenes\punto.png"))
img_vacio=tk.PhotoImage(file=resource_path("Imagenes\\vacio.png"))

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

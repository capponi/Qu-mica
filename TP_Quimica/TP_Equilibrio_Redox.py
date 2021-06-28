import tkinter.font as tkFont
import tkinter as tk

#Crear ventana 
ventana=tk.Tk()
estaPrendido = 0

#Valores de tension
tensionHidrogeno = 0
tensionAluminio = -1.67
tensionZinc = -0.76
tensionCobre = 0.34
tensionPlata = 0.8
tensionHierro1_3 = -0.04
tensionHierro1_2 = -0.44
tensionHierro2_3 = 0.77
tensionAzufre = -0.48
tensionEstaño = -0.14

tensionAnodo = tensionHidrogeno
tensionCatodo = tensionHidrogeno
resultadoTension = tk.StringVar(value="")

#Calculo de tensiones
def calcularTension():
    if(estaPrendido):
        resultado = "{:.2f}".format(tensionCatodo - tensionAnodo)
        resultadoTension.set(resultado)
        generarValorVisor(resultado)

def setTensionAnodo(valor):
    global tensionAnodo
    tensionAnodo = valor

def setTensionCatodo(valor):
    global tensionCatodo
    tensionCatodo = valor

#Comandos para botones
def generarValorVisor(valor):
    listaCaracteres = list(valor)
    if(not(listaCaracteres.__contains__("-"))):
        listaCaracteres = [""] + listaCaracteres
    valorX = 87
    for digito in listaCaracteres:
        tk.Label(ventana,image=diccDigitos[digito],borderwidth=0,highlightthickness=0).place(x=valorX,y=60)
        if(digito == "."):
            valorX += 6
        else:
            valorX += 21
    
def cambiarModo():
    global estaPrendido, bt_volt
    if(not(estaPrendido)):
        estaPrendido = 1
        cambioImagen = img_voltimetro
        calcularTension()
    elif(estaPrendido):
        estaPrendido = 0
        cambioImagen = img_apagado
        borrar_visor()
    bt_volt.config(image=cambioImagen)
    bt_volt.photo = cambioImagen
    
    

def borrar_visor():
    tk.Label(ventana,image=img_visor_vacio,borderwidth=0,highlightthickness=0).place(x=47,y=40)

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

#Imagen de fondo para ventana
img=tk.PhotoImage(file="Imagenes/fondo.png")
lbl=tk.Label(ventana, image=img).pack()
img_voltimetro=tk.PhotoImage(file="Imagenes/modoVoltimetro.png")
img_apagado=tk.PhotoImage(file="Imagenes/modoApagado.png")

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

#Imagenes de elementos positivos
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
img_Al_negativo=tk.PhotoImage(file="Imagenes/Aluminio_negativo.png")
img_Cu_negativo=tk.PhotoImage(file="Imagenes/Cobre_negativo.png")
img_Ag_negativo=tk.PhotoImage(file="Imagenes/Plata_negativa.png")
img_Zn_negativo=tk.PhotoImage(file="Imagenes/Zinc_negativo.png")
img_Sn_negativo=tk.PhotoImage(file="Imagenes/Estaño_negativo.png")
img_Fee_negativo=tk.PhotoImage(file="Imagenes/Hierro++_negativo.png")
img_Feee_negativo=tk.PhotoImage(file="Imagenes/Hierro+++_negativo.png")
img_FePt_negativo=tk.PhotoImage(file="Imagenes/HierroPt_negativo.png")
img_S_negativo=tk.PhotoImage(file="Imagenes/Azufre_negativo.png")

#Botones para elementos positivos
bt_h_pos=tk.Button(ventana, text="H2 | H", fg='black',command=lambda:[setTensionCatodo(tensionHidrogeno), calcularTension()]).place(x=400,y=100, width=70)
bt_zn_pos=tk.Button(ventana, text="Zn | Zn++", fg='black',command=lambda:[Zn_positivo(), setTensionCatodo(tensionZinc), calcularTension()]).place(x=400,y=130, width=70)
bt_ag_pos=tk.Button(ventana, text="Ag | Ag+", fg='black',command=lambda:[Ag_positivo(), setTensionCatodo(tensionPlata), calcularTension()]).place(x=400,y=160, width=70)
bt_fee_pos=tk.Button(ventana, text="Fe | Fe++", fg='black',command=lambda:[Fee_positivo(), setTensionCatodo(tensionHierro1_2), calcularTension()]).place(x=400,y=190, width=70)
bt_s_pos=tk.Button(ventana, text="S- | S", fg='black',command=lambda:[S_positivo(), setTensionCatodo(tensionAzufre), calcularTension()]).place(x=400,y=220, width=70)
bt_al_pos=tk.Button(ventana, text="Al | Al+++", fg='black',command=lambda:[Al_positivo(), setTensionCatodo(tensionAluminio), calcularTension()]).place(x=475,y=100, width=70)
bt_cu_pos=tk.Button(ventana, text="Cu | Cu++", fg='black',command=lambda:[Cu_positivo(), setTensionCatodo(tensionCobre), calcularTension()]).place(x=475,y=130, width=70)
bt_feee_pos=tk.Button(ventana, text="Fe | Fe+++", fg='black',command=lambda:[Feee_positivo(), setTensionCatodo(tensionHierro1_3), calcularTension()]).place(x=475,y=160, width=70)
bt_fept_pos=tk.Button(ventana, text="Fe++,Fe+++", fg='black',command=lambda:[FePt_positivo(), setTensionCatodo(tensionHierro2_3), calcularTension()]).place(x=475,y=190, width=70)
bt_Sn_pos=tk.Button(ventana, text="Sn | Sn++", fg='black',command=lambda:[Sn_positivo(), setTensionCatodo(tensionEstaño), calcularTension()]).place(x=475,y=220, width=70)

#Botones para elementos negativos
bt_h_neg=tk.Button(ventana, text="H2 | H", fg='black',command=lambda:[setTensionAnodo(tensionHidrogeno), calcularTension()]).place(x=610,y=100, width=70)
bt_zn_neg=tk.Button(ventana, text="Zn | Zn++", fg='black',command=lambda:[Zn_negativo(), setTensionAnodo(tensionZinc), calcularTension()]).place(x=610,y=130, width=70)
bt_ag_neg=tk.Button(ventana, text="Ag | Ag+", fg='black',command=lambda:[Ag_negativo(), setTensionAnodo(tensionPlata), calcularTension()]).place(x=610,y=160, width=70)
bt_fee_neg=tk.Button(ventana, text="Fe | Fe++", fg='black',command=lambda:[Fee_negativo(), setTensionAnodo(tensionHierro1_2), calcularTension()]).place(x=610,y=190, width=70)
bt_s_neg=tk.Button(ventana, text="S- | S", fg='black',command=lambda:[S_negativo(), setTensionAnodo(tensionAzufre), calcularTension()]).place(x=610,y=220, width=70)
bt_al_neg=tk.Button(ventana, text="Al | Al+++", fg='black',command=lambda:[Al_negativo(), setTensionAnodo(tensionAluminio), calcularTension()]).place(x=685,y=100, width=70)
bt_cu_neg=tk.Button(ventana, text="Cu | Cu++", fg='black',command=lambda:[Cu_negativo(), setTensionAnodo(tensionCobre), calcularTension()]).place(x=685,y=130, width=70)
bt_feee_neg=tk.Button(ventana, text="Fe | Fe+++", fg='black',command=lambda:[Feee_negativo(), setTensionAnodo(tensionHierro1_3), calcularTension()]).place(x=685,y=160, width=70)
bt_fept_neg=tk.Button(ventana, text="Fe++,Fe+++", fg='black',command=lambda:[FePt_negativo(), setTensionAnodo(tensionHierro2_3), calcularTension()]).place(x=685,y=190, width=70)
bt_Sn_neg=tk.Button(ventana, text="Sn | Sn++", fg='black',command=lambda:[Sn_negativo(), setTensionAnodo(tensionEstaño), calcularTension()]).place(x=685,y=220, width=70)

#Cambiar a voltimetro
bt_volt=tk.Label(ventana,image=img_apagado)
bt_volt.place(x=37,y=158,height=141,width=171)
bt_volt.bind('<Button-1>', lambda x: cambiarModo())

#Visor inicial vacio
z1=tk.Label(ventana,image=img_visor_vacio,bd=0,highlightthickness=0).place(x=47,y=40)

#Mantener ventana abierta y sin posibilidad de maximizar
ventana.resizable(0,0)
ventana.mainloop()


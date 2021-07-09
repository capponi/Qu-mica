import tkinter.font as tkFont
import tkinter as tk
from Imagenes import *

#Visor inicial vacio
tk.Label(ventana,image=img_visor_vacio,bd=0,highlightthickness=0).place(x=47,y=40)
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

#Generar visor a partir de la tensión calculada
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

#Encender/Apagar voltímetro
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

#Cambiar relieve de botones
def cambiarRelieve(boton,tipo):
    boton.config(relief='sunken')
    if tipo=='positivo':
        for i in range(len(botones_positivos)):
            if botones_positivos[i]!=boton:
                botones_positivos[i].config(relief='raised')
    else:
        for i in range(len(botones_negativos)):
            if botones_negativos[i]!=boton:
                botones_negativos[i].config(relief='raised')
        
#Botones para elementos positivos
botones_positivos=[]

bt_h_pos=tk.Button(ventana, text="H2 | H", fg='black',command=lambda:[H_positivo(),cambiarRelieve(bt_h_pos,'positivo'),setTensionCatodo(tensionHidrogeno), calcularTension()])
bt_h_pos.place(x=400,y=100, width=70)
botones_positivos.append(bt_h_pos)

bt_zn_pos=tk.Button(ventana, text="Zn | Zn++", fg='black',command=lambda:[Zn_positivo(),cambiarRelieve(bt_zn_pos,'positivo'), setTensionCatodo(tensionZinc), calcularTension()])
bt_zn_pos.place(x=400,y=130, width=70)
botones_positivos.append(bt_zn_pos)

bt_ag_pos=tk.Button(ventana, text="Ag | Ag+", fg='black',command=lambda:[Ag_positivo(),cambiarRelieve(bt_ag_pos,'positivo'), setTensionCatodo(tensionPlata), calcularTension()])
bt_ag_pos.place(x=400,y=160, width=70)
botones_positivos.append(bt_ag_pos)

bt_fee_pos=tk.Button(ventana, text="Fe | Fe++", fg='black',command=lambda:[Fee_positivo(),cambiarRelieve(bt_fee_pos,'positivo'), setTensionCatodo(tensionHierro1_2), calcularTension()])
bt_fee_pos.place(x=400,y=190, width=70)
botones_positivos.append(bt_fee_pos)

bt_s_pos=tk.Button(ventana, text="S- | S", fg='black',command=lambda:[S_positivo(),cambiarRelieve(bt_s_pos,'positivo'), setTensionCatodo(tensionAzufre), calcularTension()])
bt_s_pos.place(x=400,y=220, width=70)
botones_positivos.append(bt_s_pos)

bt_al_pos=tk.Button(ventana, text="Al | Al+++", fg='black',command=lambda:[Al_positivo(),cambiarRelieve(bt_al_pos,'positivo'), setTensionCatodo(tensionAluminio), calcularTension()])
bt_al_pos.place(x=475,y=100, width=70)
botones_positivos.append(bt_al_pos)

bt_cu_pos=tk.Button(ventana, text="Cu | Cu++", fg='black',command=lambda:[Cu_positivo(),cambiarRelieve(bt_cu_pos,'positivo'), setTensionCatodo(tensionCobre), calcularTension()])
bt_cu_pos.place(x=475,y=130, width=70)
botones_positivos.append(bt_cu_pos)

bt_feee_pos=tk.Button(ventana, text="Fe | Fe+++", fg='black',command=lambda:[Feee_positivo(),cambiarRelieve(bt_feee_pos,'positivo'), setTensionCatodo(tensionHierro1_3), calcularTension()])
bt_feee_pos.place(x=475,y=160, width=70)
botones_positivos.append(bt_feee_pos)

bt_fept_pos=tk.Button(ventana, text="Fe++,Fe+++", fg='black',command=lambda:[FePt_positivo(),cambiarRelieve(bt_fept_pos,'positivo'), setTensionCatodo(tensionHierro2_3), calcularTension()])
bt_fept_pos.place(x=475,y=190, width=70)
botones_positivos.append(bt_fept_pos)

bt_Sn_pos=tk.Button(ventana, text="Sn | Sn++", fg='black',command=lambda:[Sn_positivo(),cambiarRelieve(bt_Sn_pos,'positivo'), setTensionCatodo(tensionEstaño), calcularTension()])
bt_Sn_pos.place(x=475,y=220, width=70)
botones_positivos.append(bt_Sn_pos)

#Botones para elementos negativos
botones_negativos=[]

bt_h_neg=tk.Button(ventana, text="H2 | H", fg='black',command=lambda:[H_negativo(),cambiarRelieve(bt_h_neg,'negativo'),setTensionAnodo(tensionHidrogeno), calcularTension()])
bt_h_neg.place(x=610,y=100, width=70)
botones_negativos.append(bt_h_neg)

bt_zn_neg=tk.Button(ventana, text="Zn | Zn++", fg='black',command=lambda:[Zn_negativo(),cambiarRelieve(bt_zn_neg,'negativo'), setTensionAnodo(tensionZinc), calcularTension()])
bt_zn_neg.place(x=610,y=130, width=70)
botones_negativos.append(bt_zn_neg)

bt_ag_neg=tk.Button(ventana, text="Ag | Ag+", fg='black',command=lambda:[Ag_negativo(),cambiarRelieve(bt_ag_neg,'negativo'), setTensionAnodo(tensionPlata), calcularTension()])
bt_ag_neg.place(x=610,y=160, width=70)
botones_negativos.append(bt_ag_neg)

bt_fee_neg=tk.Button(ventana, text="Fe | Fe++", fg='black',command=lambda:[Fee_negativo(),cambiarRelieve(bt_fee_neg,'negativo'), setTensionAnodo(tensionHierro1_2), calcularTension()])
bt_fee_neg.place(x=610,y=190, width=70)
botones_negativos.append(bt_fee_neg)

bt_s_neg=tk.Button(ventana, text="S- | S", fg='black',command=lambda:[S_negativo(),cambiarRelieve(bt_s_neg,'negativo'), setTensionAnodo(tensionAzufre), calcularTension()])
bt_s_neg.place(x=610,y=220, width=70)
botones_negativos.append(bt_s_neg)

bt_al_neg=tk.Button(ventana, text="Al | Al+++", fg='black',command=lambda:[Al_negativo(),cambiarRelieve(bt_al_neg,'negativo'), setTensionAnodo(tensionAluminio), calcularTension()])
bt_al_neg.place(x=685,y=100, width=70)
botones_negativos.append(bt_al_neg)

bt_cu_neg=tk.Button(ventana, text="Cu | Cu++", fg='black',command=lambda:[Cu_negativo(),cambiarRelieve(bt_cu_neg,'negativo'), setTensionAnodo(tensionCobre), calcularTension()])
bt_cu_neg.place(x=685,y=130, width=70)
botones_negativos.append(bt_cu_neg)

bt_feee_neg=tk.Button(ventana, text="Fe | Fe+++", fg='black',command=lambda:[Feee_negativo(),cambiarRelieve(bt_feee_neg,'negativo'), setTensionAnodo(tensionHierro1_3), calcularTension()])
bt_feee_neg.place(x=685,y=160, width=70)
botones_negativos.append(bt_feee_neg)

bt_fept_neg=tk.Button(ventana, text="Fe++,Fe+++", fg='black',command=lambda:[FePt_negativo(),cambiarRelieve(bt_fept_neg,'negativo'), setTensionAnodo(tensionHierro2_3), calcularTension()])
bt_fept_neg.place(x=685,y=190, width=70)
botones_negativos.append(bt_fept_neg)

bt_Sn_neg=tk.Button(ventana, text="Sn | Sn++", fg='black',command=lambda:[Sn_negativo(),cambiarRelieve(bt_Sn_neg,'negativo'), setTensionAnodo(tensionEstaño), calcularTension()])
bt_Sn_neg.place(x=685,y=220, width=70)
botones_negativos.append(bt_Sn_neg)

#Crear perilla de voltímetro
bt_volt=tk.Label(ventana,image=img_apagado)
bt_volt.place(x=37,y=158,height=141,width=171)
bt_volt.bind('<Button-1>', lambda x: cambiarModo())

#Mantener ventana abierta y sin posibilidad de maximizar
ventana.resizable(0,0)
ventana.mainloop()

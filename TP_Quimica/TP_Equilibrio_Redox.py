import tkinter.font as tkFont
import tkinter as tk


def volt():
    lb.set("2.3V")

    
ventana=tk.Tk()

img=tk.PhotoImage(file="volt.png")
lbl=tk.Label(ventana, image=img).pack()

bt=tk.Button(ventana, text="Medir", fg='black',command=volt).place(x=250,y=20, width=60)

lb=tk.StringVar()
lb.set("0.5V")
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
z1=tk.Label(ventana,textvariable= lb, font=fontStyle, bg ='blue', fg="white").place(x=50,y=42, width=150, height=65)

ventana.resizable(0,0)
ventana.mainloop()


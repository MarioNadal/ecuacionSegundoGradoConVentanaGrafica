import tkinter as tk
import math


def resolver():
    a = (int)(entradaA.get())
    b = (int)(entradaB.get())
    c = (int)(entradaC.get())
    if (b*b - 4 * a * c < 0):
        labelRespuesta["text"] = "No tiene soluciones reales"
    labelRespuesta["text"] = "Las soluciones son: ", int((-b + math.sqrt(b*b - 4 * a * c)) / (2 * a)), " y ", int((-b - math.sqrt(b*b - 4 * a * c)) / (2 * a))


window = tk.Tk()
window.title("Calculadora Ecuaciones 2º Grado")

labelDescripcion = tk.Label(text="Programa para resolver ecuaciones de 2º grado de la forma ax^2 + bx + c = 0")
labelDescripcion.grid(row=0, column=0)

labelIntroduceA = tk.Label(text="Introduce a: ")
labelIntroduceA.grid(row=1, column=0)
entradaA = tk.Entry()
entradaA.grid(row=1, column=1)

labelIntroduceB = tk.Label(text="Introduce b: ")
labelIntroduceB.grid(row=2, column=0)
entradaB = tk.Entry()
entradaB.grid(row=2, column=1)

labelIntroduceC = tk.Label(text="Introduce c: ")
labelIntroduceC.grid(row=3, column=0)
entradaC = tk.Entry()
entradaC.grid(row=3, column=1)

buttonResolver = tk.Button(text="Resolver", command=resolver)
buttonResolver.grid(row=4, column=0)

labelRespuesta = tk.Label(text="")
labelRespuesta.grid(row=5, column=0)

window.mainloop()

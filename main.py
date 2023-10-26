import tkinter as tk
import math

# Función que devuelve el resultado de la ecuación
def resolver():
    a = (float)(entradaA.get())
    b = (float)(entradaB.get())
    c = (float)(entradaC.get())
    if (b*b - 4 * a * c < 0):
        labelRespuesta["text"] = "No tiene soluciones reales"
    x1 = float((-b + math.sqrt(b*b - 4 * a * c)) / (2 * a))
    x2 = float((-b - math.sqrt(b*b - 4 * a * c)) / (2 * a))
    labelRespuesta["text"] = "Las soluciones son: " + str(x1) + " y " + str(x2)

# Abrimos una ventana
window = tk.Tk()
window.title("Calculadora Ecuaciones 2º Grado")

# Creamos una descripcion
labelDescripcion = tk.Label(text="Programa para resolver ecuaciones de 2º grado de la forma ax^2 + bx + c = 0")
labelDescripcion.grid(row=0, column=0)

# Creamos la introducción de a
labelIntroduceA = tk.Label(text="Introduce a: ")
labelIntroduceA.grid(row=1, column=0)
entradaA = tk.Entry()
entradaA.grid(row=1, column=1)

# Creamos la introducción de b
labelIntroduceB = tk.Label(text="Introduce b: ")
labelIntroduceB.grid(row=2, column=0)
entradaB = tk.Entry()
entradaB.grid(row=2, column=1)

# Creamos la introducción de c
labelIntroduceC = tk.Label(text="Introduce c: ")
labelIntroduceC.grid(row=3, column=0)
entradaC = tk.Entry()
entradaC.grid(row=3, column=1)

# Creamos el botón que nos resolverá la ecuación dando la respuesta
buttonResolver = tk.Button(text="Resolver", command=resolver)
buttonResolver.grid(row=4, column=0)

# Creamos el texto que nos dará las respuestas de la ecuación
labelRespuesta = tk.Label(text="")
labelRespuesta.grid(row=5, column=0)

window.mainloop()

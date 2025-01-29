from numpy import linspace as arr
import math as m
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

def serie(x, grado, tipo):
  y = []

  # Caso función e^x
  if (tipo == 0):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        # Agregar polinomio de Taylor
        print()
      y.append(y_temp)
    return y

  # Caso e^-x
  if (tipo == 1):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        # Agregar polinomio de Taylor
        print()
      y.append(y_temp)
    return y

  # Caso sen(x)
  if (tipo == 2):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        y_temp += ((-1)**j) * ((i**(2*j+1))/(m.factorial(2*j+1)))
      y.append(y_temp)
    return y

  # Caso cos(x)
  if (tipo == 3):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        # Agregar polinomio de Taylor
        print()
      y.append(y_temp)
    return y

  # Caso senh(x)
  if (tipo == 4):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        # Agregar polinomio de Taylor
        print()
      y.append(y_temp)
    return y

  # Caso cosh(x)
  if (tipo == 5):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        # Agregar polinomio de Taylor
        print()
      y.append(y_temp)
    return y

  # Caso ln(1+x)
  if (tipo == 6):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        # Agregar polinomio de Taylor
        print()
      y.append(y_temp)
    return y

def calcReal(x, tipo):
  y = []

  # Caso función e^x
  if (tipo == 0):
    for i in x:
      y.append(m.exp(i)) 
    return y

  # Caso e^-x
  if (tipo == 1):
    for i in x:
      y.append(m.exp(-i))
    return y

  # Caso sen(x)
  if (tipo == 2):
    for i in x:
      y.append(m.sin(i))
    return y

  # Caso cos(x)
  if (tipo == 3):
    for i in x:
      y.append(m.cos(i))
    return y

  # Caso senh(x)
  if (tipo == 4):
    for i in x:
      y.append(m.sinh(i))
    return y

  # Caso cosh(x)
  if (tipo == 5):
    for i in x:
      y.append(m.cosh(i))
    return y

  # Caso ln(1+x)
  if (tipo == 6):
    for i in x:
      y.append(m.log(1+i))
    return y

def setGraph(a_ui, b_ui, n_ui, g1_ui, g2_ui, g3_ui, funcs_ui):
  a = float(0)
  b = float(0)
  n = int(0)
  g1 = int(0)
  g2 = int(0)
  g3 = int(0)

  opc = int(0)

  try:
    if funcs_ui.curselection():
      opc = funcs_ui.curselection()[0]
    else:
      tk.messagebox.showerror("Error", "No selecciono una función")
      print("Error: Función no seleccionada")
      return

    a = float(a_ui.get())
    b = float(b_ui.get())
    n = int(n_ui.get())
    g1 = int(g1_ui.get())
    g2 = int(g2_ui.get())
    g3 = int(g3_ui.get())

  except ValueError:
    tk.messagebox.showerror("Error", "Ingrese un número válido")
    print("Error: Ingrese un número válido")
    return

  if (opc < 0 or opc > 6):
    tk.messagebox.showerror("Error", "Seleccione una función")
    print("Error: Seleccione una función")
    return
  
  x = arr(a , b, n)
  y1 = serie(x, g1, opc)
  y2 = serie(x, g2, opc)
  y3 = serie(x, g3, opc)

  org = calcReal(x, opc)
  
  fig = Figure(figsize=(5, 4), dpi=100)
  ax = fig.add_subplot(111)

  ax.plot(x, org, color="orange", label="f(x)")

  ax.plot(x, y1, color="green", label=f"T{g1}(x)")
  ax.plot(x, y2, color="blue", label=f"T{g2}(x)")
  ax.plot(x, y3, color="red", label=f"T{g3}(x)")

  ax.legend(loc="upper right", fontsize="small")

  ax.set_title("Pólinomios de Taylor y McLaurin")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.set_ylim(min(org)-2 , max(org)+2)
  ax.set_xlim(min(x), max(x))
  ax.grid(True)

  canvas = FigureCanvasTkAgg(fig, master=root)
  canvas.draw()
  canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


## Ventana principal ##
root = tk.Tk()
root.wm_title("Plinomios de Taylor y McLaurin")

## Definición de Variables ##
a_ui = tk.StringVar(value="")
b_ui = tk.StringVar(value="")
n_ui = tk.StringVar(value="")

g1_ui = tk.StringVar(value="")
g2_ui = tk.StringVar(value="")
g3_ui = tk.StringVar(value="")

# Panel con las opciones
opciones = tk.Frame(root, width=300, height=450, borderwidth=2, relief="sunken")
opciones.pack(padx=20, pady=10, side=tk.RIGHT)

# Campos de texto para introducir los grados
etiqueta2 = tk.Label(opciones, text="Grados")
etiqueta2.pack(padx=10)
grad1 = tk.Entry(opciones, width=20, textvariable=g1_ui)
grad1.pack(padx=10, pady=2)
grad2 = tk.Entry(opciones, width=20, textvariable=g2_ui)
grad2.pack(padx=10, pady=2)
grad3 = tk.Entry(opciones, width=20, textvariable=g3_ui)
grad3.pack(padx=10, pady=2)

# Campos de texto para los puntos [a, b] de la evaluación
etiqueta3 = tk.Label(opciones, text="Puntos de la recta [a, b]")
etiqueta3.pack(padx=10)
punto1 = tk.Entry(opciones, width=20, textvariable=a_ui)
punto1.pack(padx=10, pady=2)
punto2 = tk.Entry(opciones, width=20, textvariable=b_ui)
punto2.pack(padx=10, pady=2)

# Cantidad de puntos a Evaluar
etiqueta5 = tk.Label(opciones, text="Cantidad de puntos")
etiqueta5.pack(padx=10)
pts = tk.Entry(opciones, width=20, textvariable=n_ui)
pts.pack(padx=10, pady=2)

# Lista de las funciones disponibles
etiqueta = tk.Label(opciones, text="Funciones")
etiqueta.pack(padx=10)
opc = tk.StringVar(value="")
funcs = tk.Listbox(opciones, selectmode=tk.SINGLE, width=20, height=5, listvariable=opc)
funcs.pack(padx=10, pady=2)

# Llenado de la lista de funciones
for item in ["Exponente", "Exponente ^-", "Seno", "Coseno", "Seno Hiperbolico", "Coseno Hiperbolico", "Logaritmo natural"]:
  funcs.insert(tk.END, item, )

# Boton que realiza el cálculo
calc = tk.Button(opciones, text="Calcular", width=15,command=lambda:setGraph(a_ui, b_ui, n_ui, g1_ui, g2_ui, g3_ui, funcs) )
calc.pack(padx=20, pady=10)

# Inicio de la ventana maximizada
root.state("zoomed")
root.mainloop()
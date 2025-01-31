from numpy import linspace as arr
import math as m
import tkinter as tk
from tkinter import messagebox as msg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# Variable global, se usa para determinar si existe un grafico en la aplicación
current_canvas = None

## Funcion para la serie de Taylor y Maclaurin ##
def serie(x, grado, tipo):
  y = []

  # Caso función e^x
  if (tipo == 0):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        y_temp += ( i**j )/m.factorial(j)
      y.append(y_temp)
    return y

  # Caso e^-x
  if (tipo == 1):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        y_temp += ((-i)**j)/ m.factorial(j)
      y.append(y_temp)
    return y

  # Caso sen(x)
  if (tipo == 2):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        y_temp += (((-1)**j) * ((i**(2*j+1))/(m.factorial(2*j+1))))
      y.append(y_temp)
    return y

  # Caso cos(x)
  if (tipo == 3):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        y_temp += ((-1)**j) * ((i**(2*j))/(m.factorial(2*j)))
      y.append(y_temp)
    return y

  # Caso senh(x)
  if (tipo == 4):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        y_temp += ( i**(2*j+1) )/m.factorial(2*j+1)
      y.append(y_temp)
    return y

  # Caso cosh(x)
  if (tipo == 5):
    for i in x:
      y_temp = 0
      for j in range(0, (grado+1)):
        y_temp += (i**(2*j))/m.factorial(2*j)
      y.append(y_temp)
    return y

  # Caso ln(1+x)
  if (tipo == 6):
    for i in x:
      y_temp = 0
      for j in range(1, (grado+1)):
        y_temp += (((-1)**(j+1))*(i**j))/j
      y.append(y_temp)
    return y
  
  ### Fin de la función ###

## Funcion para el resultado de la función original
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

  ### Fin de la función ###

## Función para dibujar la gráfica de las series de Taylor y Maclaurin
def setGraph(a_ui, b_ui, n_ui, g1_ui, g2_ui, g3_ui, funcs_ui):
  global current_canvas

  a, b, n, g1, g2, g3, opc = float(0), float(0), int(0), int(0), int(0), int(0), int(0)
  err = 0

  # Cachado de errores
  try:
    if funcs_ui.curselection():
      opc = funcs_ui.curselection()[0]
    else:
      tk.messagebox.showerror("Error", "Seleccione una función válida de la lista de las funciones disponibles")
      err += 1

    a = float(a_ui.get())
    b = float(b_ui.get())
    n = int(n_ui.get())
    g1 = int(g1_ui.get())
    g2 = int(g2_ui.get())
    g3 = int(g3_ui.get())

  except ValueError:
    tk.messagebox.showerror("Error", "Ingrese un número válido en los campos:\n• Los 3 grados de los polinomios y la cantidad de puntos son valores enteros.\n• Los puntos de inicio y final a evaluar pueden ser numero de punto flotante\n• No pueden haber campos vacios")
    err += 1

  if err != 0:
    return
  
  if opc == 6 and (a <= -1 or b <= -1):
    tk.messagebox.showerror("Error", "La función ln(1+x) no puede ser evaluada en números menores o iguales a -1")
    return
  
  # Calcular y evaluar las funciones y polinomios
  x = arr(a, b, n)
  y1, y2, y3 = serie(x, g1, opc), serie(x, g2, opc), serie(x, g3, opc)
  org = calcReal(x, opc)
  
  # Destruir el canvas anterior si existe
  if current_canvas is not None:
    current_canvas.get_tk_widget().destroy()
  
  limY = [min(org)-(max(org)*0.25), max(org)*1.25]

  # Creación de la gráfica
  fig = Figure(figsize=(5, 4), dpi=100)
  ax = fig.add_subplot(111)

  ax.plot([min(x), max(x)], [0, 0], color="black", linewidth=1)
  ax.plot([0, 0], limY, color="black", linewidth=1)

  ax.plot(x, y1, color="green", label=f"T{g1}(x)")
  ax.plot(x, y2, color="blue", label=f"T{g2}(x)")
  ax.plot(x, y3, color="red", label=f"T{g3}(x)")
  ax.plot(x, org, color="orange", label="f(x)")
  ax.legend(loc="upper right", fontsize="small")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.set_ylim(limY[0], limY[1])
  ax.set_xlim(min(x), max(x))
  ax.grid(which="major", linestyle="dashed")

  # Dibujo del canva nuevo
  current_canvas = FigureCanvasTkAgg(fig, master=root)
  current_canvas.draw()
  current_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

  ### Fin de la función ###


## Ventana principal ##
root = tk.Tk()
root.wm_title("Polinomios de Taylor y McLaurin")

titulo = tk.Label(root, text="Polinomios de Taylor y McLaurin", font=("Arial", 20))
titulo.pack(pady=10, side=tk.TOP)

## Definición de variables de Tkinter##
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
etiqueta2 = tk.Label(opciones, text="Grados de los polinomios")
etiqueta2.pack(padx=10)
grad1 = tk.Entry(opciones, width=25, textvariable=g1_ui)
grad1.pack(padx=10, pady=2)
grad2 = tk.Entry(opciones, width=25, textvariable=g2_ui)
grad2.pack(padx=10, pady=2)
grad3 = tk.Entry(opciones, width=25, textvariable=g3_ui)
grad3.pack(padx=10, pady=2)

# Campos de texto para los puntos [a, b] de la evaluación
etiqueta3 = tk.Label(opciones, text="Puntos de la recta [a, b]")
etiqueta3.pack(padx=10)
punto1 = tk.Entry(opciones, width=25, textvariable=a_ui)
punto1.pack(padx=10, pady=2)
punto2 = tk.Entry(opciones, width=25, textvariable=b_ui)
punto2.pack(padx=10, pady=2)

# Cantidad de puntos a Evaluar
etiqueta5 = tk.Label(opciones, text="Cantidad de puntos")
etiqueta5.pack(padx=10)
pts = tk.Entry(opciones, width=25, textvariable=n_ui)
pts.pack(padx=10, pady=2)

# Lista de las funciones disponibles
etiqueta = tk.Label(opciones, text="Funciones")
etiqueta.pack(padx=10)
opc = tk.StringVar(value="")
funcs = tk.Listbox(opciones, selectmode=tk.SINGLE, width=25, height=5, listvariable=opc)
funcs.pack(padx=10, pady=2)

# Llenado de la lista de funciones
for item in ["Exponente: e^x", "Exponente: e^-x", "Seno: sen(x)", "Coseno: cos(x)", "Seno hiperbólico: senh(x)", "Coseno hiperbólico: cosh(x)", "Logaritmo natural: ln(1+x)"]:
  funcs.insert(tk.END, item)

# Boton que realiza el cálculo
calc = tk.Button(opciones, text="Calcular", width=20,command=lambda:setGraph(a_ui, b_ui, n_ui, g1_ui, g2_ui, g3_ui, funcs) )
calc.pack(padx=20, pady=10)

# Inicio de la ventana maximizada
root.state("zoomed")
root.mainloop()
# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from pulp import * # Carga Pulp 
from calculo import *
from tkinter import messagebox
from grafico import *


def ecuacion(): # X = X1  Y = X2
	# Coeficientes Funcion Obejtivo
	R1A1 = float
	R1B1 = float
	R1C1 = float
	R2A2 = float
	R2B2 = float
	R2C2 = float
	R3A3 = float
	R3B3 = float
	R3C3 = float
	R1S = float
	R2S = float
	R3S = float
	N = int
	

	# Sentido de la optimización
	if (OPT.get() == 'MAX'):
		Optimo = LpMaximize
	else:
		Optimo = LpMinimize
	
	# Coeficientes de funcion objetivo
	try:
		FOX1 = float(OX1.get()) 
		FOX2 = float(OX2.get())
	except:
		messagebox.showerror("Error", "Ingrese Valores Válidos NO nulos en la función objetivo.")
		pass

	# Cantidad de restricciones
	N = int(CantRes.get())

	# Coeficientes Restriccion 1
	try:
		R1A1 = float(R1X1.get())
		R1B1 = float(R1X2.get())
		R1C1 = float(R1C.get())
	except:
		messagebox.showerror("Error", "Ingrese Valores Válidos NO nulos en la restriccion 1.")
		pass 

	# Sentido de la Restricción 1
	if  (R1Signo.get() =='>='):
  		 R1S = 1
	elif (R1Signo.get() =='<='):
  		  R1S = -1 
	else:
		R1S = 0

	# Coeficientes Restriccion 2
	if N >= 2:
		try:
		    R2A2 = float(R2X1.get())
		    R2B2 = float(R2X2.get())
		    R2C2 = float(R2C.get())
		    
		    
		except:
		    messagebox.showerror("Error", "Ingrese Valores Válidos NO nulos en la restriccion 2.")
		    pass 

	# Sentido de la Restricción 2
	if  (R2Signo.get() =='>='):
		R2S = 1
	elif (R2Signo.get() =='<='):
		R2S = -1 
	else:
		R2S = 0

	# Coeficientes Restriccion 3
	if N == 3:
		try:
		    R3A3 = float(R3X1.get())
		    R3B3 = float(R3X2.get())
		    R3C3 = float(R3C.get())	
        
		except:
		    messagebox.showerror("Error", "Ingrese Valores Válidos NO nulos en la restriccion 3.")
		    pass 

		# Sentido de la Restricción 3	
		if  (R3Signo.get() =='>='):
			R3S = 1
		elif (R3Signo.get() =='<='):
			R3S = -1 
		else:
			R3S = 0
	
	# Armar los parámetros del modelo
	try:
		FunObj = [FOX1,FOX2]
		if N == 1:
			Rest = [[R1A1,R1B1,R1C1,R1S]]
		if N == 2:
			Rest = [[R1A1,R1B1,R1C1,R1S],[R2A2,R2B2,R2C2,R2S]]
		if N == 3:
			Rest = [[R1A1,R1B1,R1C1,R1S],[R2A2,R2B2,R2C2,R2S], [R3A3,R3B3,R3C3,R3S]]
	    # Resolver el problema
		problema = resolver(FunObj,Rest,Optimo, N)	

		
	# Si el problema tiene solución, grafica
		if problema[3] == "Optimal": 
			graficar(FunObj, Rest, problema, N)
			
    	# Si el problema no tiene solución, muestra la ventana 
		else:	
			root = Tk()
			frame = Frame(root)
			frame.pack()
			bottomframe = Frame(root)
			bottomframe.pack( side = BOTTOM )
    		# Mostramos el resultado	
			Label(root, text = "El tipo de problema es: " + str(problema[3])).pack()
	except:
		pass
def CantResUpdate(event):
	sel = int(CantRes.get())
	if sel == 1:
		# Oculta Restricción 2 y Restricción 3
		restriccion2.pack_forget()
		restriccion3.pack_forget()
	elif sel == 2:
		# Habilita Restricción 2 y oculta Restricción 3
		restriccion2.pack()
		restriccion3.pack_forget()
	else:
		# Habilita Restricción 2 y Restricción 3
		restriccion2.pack()
		restriccion3.pack()

# Define la ventana principal de la aplicación
raiz = Tk()

# Define el ancho y el alto
raiz.geometry('400x250') 

# Define el título de la ventana
raiz.title('Programacion Lineal - Método Gráfico')

# Definir las variables asociadas a la función objetivo
band2 = bool
R1Signo = StringVar()
R2Signo = StringVar()
R3Signo = StringVar()
OPT = StringVar()
OX1 = StringVar()
OX2 = StringVar()
R1X1 = StringVar()
R1X2 = StringVar()
R2X1 = StringVar()
R2X2 = StringVar()
R3X1 = StringVar()
R3X2 = StringVar()
R1C = StringVar()
R2C = StringVar()
R3C = StringVar()
CantRes = StringVar()

# Define los labels de la función objetivo
funcionObjetivo = Frame(raiz, width = '400', height = '100' )
funcionObjetivo.pack(side = TOP)
Label(funcionObjetivo, text ="Ingrese la funcion objetivo: ", pady = '5').pack(side = TOP)
Label(funcionObjetivo, text = " Z =  ").pack(side = LEFT)
Entry(funcionObjetivo, width = '5', textvariable = OX1).pack(side = LEFT)
Label(funcionObjetivo, text = " X1 +").pack(side = LEFT)
Entry(funcionObjetivo, width = '5', textvariable = OX2).pack(side = LEFT)
Label(funcionObjetivo, text = " X2 ").pack(side = LEFT)
combo = ttk.Combobox(funcionObjetivo, values = ('MAX','MIN'), width = '5',textvariable = OPT, state = 'readonly').pack(side = LEFT)

# Cantidad de restricciones
cantidadRestricciones = Frame(raiz, width = '400', height = '100')
cantidadRestricciones.pack(side = TOP)
Label(cantidadRestricciones, text = "¿Cuántas restricciones tiene su problema?").pack(side = TOP)
ComboRestricciones = ttk.Combobox(cantidadRestricciones, values = ('1', '2', '3'), width = '5', textvariable = CantRes, state = 'readonly')
ComboRestricciones.current(2)
ComboRestricciones.pack(side = TOP)
ComboRestricciones.bind("<<ComboboxSelected>>", CantResUpdate)

# Restriccion 1
restriccion1 = Frame(raiz, width = '400', height = '100' )
restriccion1.pack(side = TOP)
Label(restriccion1, text ="Ingrese las restricciones: ", pady = '5').pack(side = TOP)
Label(restriccion1, text='R1: ').pack(side = LEFT)
Entry(restriccion1, width = '5',textvariable = R1X1).pack(side = LEFT)
Label(restriccion1, text = " X1 +").pack(side = LEFT)
Entry(restriccion1, width = '5',textvariable = R1X2).pack(side = LEFT)
Label(restriccion1, text = " X2 ").pack(side = LEFT)
ttk.Combobox(restriccion1, values = ('>=','<=','='), width = '5',textvariable = R1Signo, state = 'readonly').pack(side = LEFT)
Entry(restriccion1, width = '5', textvariable = R1C).pack(side = LEFT, padx=(5,0))

# Restriccion 2
restriccion2 = Frame(raiz, width = '400', height = '100')
restriccion2.pack(side = TOP)


Label(restriccion2, text='R2: ').pack(side = LEFT)
Entry(restriccion2, width = '5',textvariable = R2X1).pack(side = LEFT)
Label(restriccion2, text = " X1 +").pack(side = LEFT)
Entry(restriccion2, width = '5',textvariable = R2X2).pack(side = LEFT)
Label(restriccion2, text = " X2 ").pack(side = LEFT)
ttk.Combobox(restriccion2, values = ('>=','<=','='), width = '5', textvariable = R2Signo, state = 'readonly').pack(side = LEFT)
Entry(restriccion2, width = '5', textvariable = R2C).pack(side = LEFT, padx=(5,0))

# Restriccion 3
restriccion3 = Frame(raiz, width = '400', height = '100')
restriccion3.pack(side = TOP)
Label(restriccion3, text='R3: ').pack(side = LEFT)
Entry(restriccion3, width = '5',textvariable = R3X1).pack(side = LEFT)
Label(restriccion3, text = " X1 +").pack(side = LEFT)
Entry(restriccion3, width = '5',textvariable = R3X2).pack(side = LEFT)
Label(restriccion3, text = " X2 ").pack(side = LEFT)
ttk.Combobox(restriccion3, values = ('>=','<=','='), width = '5', textvariable = R3Signo, state = 'readonly').pack(side = LEFT)
Entry(restriccion3, width = '5', textvariable = R3C).pack(side = LEFT, padx=(5,0))

# Botón Resolver
ttk.Button(raiz, text='Resolver', command= ecuacion).pack(side = BOTTOM, pady=(10,10))

# Bucle principal de la aplicación
raiz.mainloop()

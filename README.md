# ProgLinealApp
Una aplicación genial para Programación Lineal

	Tenemos 2 partes el módulo de cálculo "testing.py" y el punto de entrada al modulo "entryPoint.py"
	Desde la UI nos pasaron los datos coeficientes y demas, el punto de entrada los recibe y le pasa los parametros al modulo de cálculo.
	En entryPoint hay una funcion resolver(obj,restricciones,tipoProblema) 
	donde: obj son los coeficientes de la funcion objetivo, restricciones (del problema), tipoProblema (max o min)

# Veamos un ejemplo en detalle

	Maximize
	Funcion_Objetivo: 0.013 x1 + 0.008 x2
	Subject To
	c1: x1 + 3 x2 <= 30
	c2: 6 x1 + 2 x2 <= 20
	c3: x1 + 5 x2 <= 40


	obj = [0.013,0.008]
	restricciones = [[1,3,30, -1],[6,2,20, -1],[1,5,40, -1]] #restricciones
	tipoProblema = LpMaximize
	resolver(obj,restricciones,tipoProblema)
	los primeros 2 parametros de restricciones son los coeficientes de la restricciones, 
	el 3ro es el termino independiente y 
	el 4to (1,0,-1) >=, ==, <= respectivamente


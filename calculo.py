# Importar módulo pulp
from pulp import *


def resolver(obj,k,tipoProblema, n):
    # Definimos el PL
    prob = LpProblem("yourProblem", tipoProblema)
    
    # Variables de decisión
    x1=LpVariable("x1",0,None)
    x2=LpVariable("x2",0,None)


    # Definimos la función objetivo
    prob += obj[0]*x1 + obj[1]*x2, "Funcion Objetivo"

    # Definimos las restricciones
    i = 0
    while i < n:
        constraint = LpAffineExpression([ (x1,k[i][0]), (x2,k[i][1])])
        a = LpConstraint(e=constraint, sense= k[i][3], name="c" + str(i), rhs= k[i][2]) 
        prob += a 
        i += 1

    # Resolver el problema
    prob.solve()
    result = []
   
   # Colocar el valor de las variables de decisión
    result.append(prob.objective.value())
    for v in prob.variables():
         result.append(v.varValue)

    # Para conocer la factibilidad del problema
    result.append(LpStatus[prob.status])
    return result
  
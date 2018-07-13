from matplotlib import pyplot                                               
import numpy as np
# x = (c-b*y)/a
def f(x, c1, c2, b):
    if c2 == 0:
        return b / c1
    return (b - c1*x)/c2

def puntosTabla(obj, k, n):
    # Primero se obtienen los puntos factibles: A * X = B
    rest = k
    rest.append([1, 0, 0, 1])
    rest.append([0, 1, 0, 1])
    data = []
    i = 0
    while i < (len(rest) - 1):
        c11 = rest[i][0]
        c12 = rest[i][1]
        b1 = rest[i][2]
        j = i + 1
        while j < len(rest):
            c21 = rest[j][0]
            c22 = rest[j][1]
            b2 = rest[j][2]
            A = np.array([[c11, c12], [c21, c22]])
            B = np.array([[b1], [b2]])
            # X = [[x1], [x2]]
            try:
                X = np.linalg.inv(A).dot(B)
                arr = [X[0][0], X[1][0]]
                if not (arr in data):
                    data.append(arr)
            except:
                pass
            j += 1
        i += 1
    # Luego se tienen que obtener los valores de slacks por cada punto
    i = 0
    rest.pop()
    rest.pop()
    while i < len(data):
        x1 = data[i][0]
        x2 = data[i][1]
        # Para x1 y x2 se deben recorrer todas las restricciones
        j = 0
        while j < len(rest):
            c1 = rest[j][0]
            c2 = rest[j][1]
            b = rest[j][2]
            signo = rest[j][3] * (-1)
            s = (b - c1 * x1 - c2 * x2) * signo
            if signo == 0:
                s = "-"
            data[i].append(s)
            j += 1
        i += 1
    
    # Ahora agregamos el valor de Z en cada punto
    i = 0
    while i < len(data):
        x1 = data[i][0]
        x2 = data[i][1]
        c1 = obj[0]
        c2 = obj[1]
        z = (c1 * x1) + (c2 * x2)
        data[i].append(z)
        i += 1
    return data

def valorMayorX(data):
    i = 0
    arr = []
    while i < len(data):
        arr.append(data[i][0])
        i += 1
    xmax = max(arr)
    xmax = xmax + 0.4 * xmax
    return xmax

def limpiarTabla(tabla):
    i = 0
    arr = []
    while i < len(tabla):
        j = 0
        while j < len(tabla[i]):
            if tabla[i][j] != "-":
                if round(tabla[i][j], 5) < 0:
                    arr.append(tabla[i])
            j += 1
        i += 1
    i = 0
    while i < len(arr):
        try:
            tabla.remove(arr[i])
        except:
            pass
        i += 1

def redondearValores(tabla):
    i = 0
    while i < len(tabla):
        j = 0
        while j < len(tabla[i]):
            if tabla[i][j] != "-":
                tabla[i][j] = abs(round(tabla[i][j], 2))
            j += 1
        i += 1
    
def dibujarTabla(data, n, tabax):
    columns = ["x1", "x2"]
    i = 1 
    while i < (n + 1):
        columns.append("x" + str(i + 2))
        i += 1
    columns.append("z")
    rows = []
    char = ord('A')
    i = 0
    while i < len(data):
        rows.append(chr(char))
        char += 1
        i += 1
    tabax.axis("off")
    # Redondear los valores de la tabla antes de mostrarlos
    redondearValores(data)
    tabax.table(cellText=data, rowLabels=rows, colLabels=columns, loc="center")

def puntosFactibles(tabla, ax):
    i = 0
    while i < len(tabla):
        ax.plot([tabla[i][0]], [tabla[i][1]], marker='o', markersize=7, color="blue")
        i += 1

def graficar(obj, k, solucion, n):
    fig, (ax, tabax) = pyplot.subplots(nrows=2)

    # Definiciones para la tabla
    data = puntosTabla(obj, k, n)

    # Definiciones para la gráfica
    # Obtenemos el punto de los datos con valor mayor de X

    xmax = valorMayorX(data)
    x = np.arange(0, xmax, 0.01)

    # Limpiamos la tabla
    limpiarTabla(data)
    
    # Dibujamos la tabla
    dibujarTabla(data, n, tabax)
    
    # Dibujamos la gráfica
    i = 0
    while i < n:
        y = f(x, k[i][0], k[i][1], k[i][2])
        if k[i][1] == 0:
            ax.axvline(x = y)
        else:
            ax.plot(x, y)
        i += 1 
    
    # Dibujamos los ejes
    ax.axvline(x = 0, color = 'k')
    ax.axhline(y = 0, color = 'k')
    
    # Marcamos puntos factibles
    puntosFactibles(data, ax)    
    
    # Marcamos el optimo
    ax.plot([solucion[1]], [solucion[2]], marker='o', markersize=10, color="red")
    
    # Titulo de la gráfica
    s = "{0} | Z = {1} | x1 = {2} | x2 = {3}".format(solucion[3], solucion[0], solucion[1], solucion[2])
    
    # Configuración de la gráfica
    ax.autoscale(enable = True, axis = 'y', tight = True)
    ax.set_title(s)
    ax.set_ylim(ymin = -1)
    
    # Mostrar el gráfico completo
    pyplot.tight_layout()
    pyplot.show()

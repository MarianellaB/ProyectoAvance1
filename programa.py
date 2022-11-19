from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator 

app = QtWidgets.QApplication([])

primera = uic.loadUi("pantallaPrincipal.ui") # cargo las interfaces
valores = uic.loadUi("IngresarNumeroDeVariables_y_NumeroDeRestricciones.ui")
funcRestr = uic.loadUi("funcionObjetivo_y_retricciones.ui")
solucion = uic.loadUi("mostrarSolucion.ui")


def ventana1(): 
    primera.hide() #cerramos la ventana principal
    valores.show()  # abrimos la ventana de los valores

def BtnContinuar():
    valores.hide()
    funcRestr.show()
    
def BtnVolver():
    funcRestr.hide()
    primera.show()
    
def BtnVolver2():
    funcRestr.hide()
    valores.show()  
    
def Btncontinuar2():
    valores.hide()
    solucion.show()

def coeficientesFunObjetivo():
    X1 = funcRestr.textEdit.text() # X1 funcion objetivo
    X2 = funcRestr.textEdit_3.text() # X2 funcion objetivo
    
    a = -1000000
    
    coeFuncion = [X1, X2, 0, 0, 0, a]
    b = ""
    for i in range(len(coeFuncion)):
        b += str(coeFuncion[i]) + "\n"
    return b


def coeRestriciones():
    TI1 = funcRestr.textEdit_6.text()  # termino independiente restriccion 1
    TI2 = funcRestr.textEdit_9.text()  # termino independiente restriccion 2 
    TI3 = funcRestr.textEdit_12.text()   # termino independiente restriccion 3
    
    coeficientesRest = [TI1, TI2, TI3]
    b = ""
    for i in range(len(coeficientesRest)):
        b += str(coeficientesRest[i]) + "\n"
    return b

def coefi():    
    X11 = funcRestr.textEdit_2.text()  # X1 restriccion 1 
    X21 = funcRestr.textEdit_5.text()  # X2 restriccion 1

    X12 = funcRestr.textEdit_7.text()  # X1 restriccion 2 
    X22 = funcRestr.textEdit_8.text()   # X2 restriccion 2

    X13 = funcRestr.textEdit_10.text()  # X1 restriccion 3 
    X23 = funcRestr.textEdit_11.text()   # X2 restriccion 3
    
    def comp1():
        mayorMenor1 = funcRestr.seleccionador_menorMayor.currentText()
        return mayorMenor1
    def comp2():
        mayorMenor2 = funcRestr.seleccionador_menorMayor_2.currentText()
        return mayorMenor2
    def comp3():    
        mayorMenor3 = funcRestr.seleccionador_menorMayor_3.currentText()
        return mayorMenor3
    
    S11, S21, S31 = 0, 0, 0
    S12, S22, S32 = 0, 0, 0
    S13, S23, S33 = 0, 0, 0
    A1, A2, A3 = 0, 0, 0
    if comp1() == "≤":
        S11 = 1
        S21 = 0
        S31 = 0
    elif comp1() == "≥":
        S11 = -1
        S21 = 0
        S31 = 0
        A1 = 1
    if comp2() == '≤':
        S22 = 1
        S12 = 0
        S32 = 0
    elif comp2() == "≥":
        S22 = -1
        A2 = 1
    
    if comp3() == "≤":
        S33 = 1
        S13 = 0
        S23 = 0
    elif comp3() == "≥":
        S33 = -1
        A3 = 1
    
    
    vars = [[X11, X21, S11, S21, S31, A1],
            [X12, X22, S12, S22, S32, A2],
            [X13, X23, S13, S23, S33, A3]]
    
    b = ""
    for i in range(len(vars)):
        for j in range(len(vars[0])):
            b += str(vars[i][j]) + " "
        b += " \n"
    return b


A = [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]]

def MostrarMatrizA():
    matr = ""
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = coefi()
            matr = A[i][j]
            solucion.espacioMatrizA.setText(matr)
    matr = ""        

def mostrarCoeRest():
    coef = [0, 0, 0]
    coeficientes = ""
    for i in range(len(coef)):
        coef[i] = coeRestriciones()
        coeficientes = coef[i]
        solucion.espacioVectorCoeficientes.setText(str(coeficientes))
        
def mostrarVectorCostos():
    a = -100000
    coefun = [0, 0, 0, 0, 0, a]
    costos = ""
    for i in range(len(coefun)):
        coefun[i] = coeficientesFunObjetivo()
        costos = coefun[i]
        solucion.espacioVectorCostos.setText(str(costos))

def botones():
    primera.boton1.clicked.connect(ventana1)  # cuando presiono el boton maximizar (boton prueba) hace el llamdado a la funcion ventana1
    valores.Btn_continuar.clicked.connect(BtnContinuar)
    valores.Btn_volver.clicked.connect(BtnVolver)
    funcRestr.Btn_volver.clicked.connect(BtnVolver2)
    funcRestr.Btn_continuar.clicked.connect(Btncontinuar2)
    funcRestr.Btn_continuar.clicked.connect(MostrarMatrizA)
    funcRestr.Btn_continuar.clicked.connect(mostrarCoeRest)
    funcRestr.Btn_continuar.clicked.connect(mostrarVectorCostos)
    




botones()
primera.show() #mantiene la primera ventana abierta
app.exec()  # mantiene el rpograma ejecutandose en ciclo infinito hasta darle cerrar

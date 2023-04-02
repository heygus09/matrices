import math
from PySide6 import *
from PySide6.QtWidgets import *

import sys
import sympy
from sympy import *

from formmatrices import *

##matriz A
a=[]
##matriz B
b=[]
##matriz resultado
resultado=[]

class FormularioParcial (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
    ##buttons.    
        self.ui.btn_Sumar.clicked.connect(self.sumaMatrices)
        self.ui.btn_Restar.clicked.connect(self.restaMatrices)
        self.ui.btn_Multiplicar.clicked.connect(self.multiplicacionMatrices)
        self.ui.btn_Transpuesta.clicked.connect(self.transpuestaMatriz)
        self.ui.btn_Determinante.clicked.connect(self.determinanteMatriz)
        self.ui.btn_Adjunta.clicked.connect(self.adjuntaMatriz)
        self.ui.btn_Inversa.clicked.connect(self.inversaMatriz)
        self.ui.btn_MetodoAdj.clicked.connect(self.metodoAdjunta)
        self.ui.btn_MetodoCramer.clicked.connect(self.metodoCramer)


    ##suma de matrices    
    def sumaMatrices(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)

        ##matriz A
        a[0][0]=float(self.ui.txt_A00.text())
        a[0][1]=float(self.ui.txt_A01.text())
        a[0][2]=float(self.ui.txt_A02.text())
        a[1][0]=float(self.ui.txt_A10.text())
        a[1][1]=float(self.ui.txt_A11.text())
        a[1][2]=float(self.ui.txt_A12.text())
        a[2][0]=float(self.ui.txt_A20.text())
        a[2][1]=float(self.ui.txt_A21.text())
        a[2][2]=float(self.ui.txt_A22.text())

        ##matriz B
        b[0][0]=float(self.ui.txt_B00.text())
        b[0][1]=float(self.ui.txt_B01.text())
        b[0][2]=float(self.ui.txt_B02.text())
        b[1][0]=float(self.ui.txt_B10.text())
        b[1][1]=float(self.ui.txt_B11.text())
        b[1][2]=float(self.ui.txt_B12.text())
        b[2][0]=float(self.ui.txt_B20.text())
        b[2][1]=float(self.ui.txt_B21.text())
        b[2][2]=float(self.ui.txt_B22.text())
        
        ##matriz resultado
        ##matriz A + matriz B
        resultado[0][0]=a[0][0]+b[0][0]
        resultado[0][1]=a[0][1]+b[0][1]
        resultado[0][2]=a[0][2]+b[0][2]
        resultado[1][0]=a[1][0]+b[1][0]
        resultado[1][1]=a[1][1]+b[1][1]
        resultado[1][2]=a[1][2]+b[1][2]
        resultado[2][0]=a[2][0]+b[2][0]
        resultado[2][1]=a[2][1]+b[2][1]
        resultado[2][2]=a[2][2]+b[2][2]
        
        ##mostrar matriz resultado
        self.ui.lbl_AB00.setText(str(resultado[0][0]))
        self.ui.lbl_AB01.setText(str(resultado[0][1]))
        self.ui.lbl_AB02.setText(str(resultado[0][2]))
        self.ui.lbl_AB10.setText(str(resultado[1][0]))
        self.ui.lbl_AB11.setText(str(resultado[1][1]))
        self.ui.lbl_AB12.setText(str(resultado[1][2]))
        self.ui.lbl_AB20.setText(str(resultado[2][0]))
        self.ui.lbl_AB21.setText(str(resultado[2][1]))
        self.ui.lbl_AB22.setText(str(resultado[2][2]))

    ##resta de matrices
    def restaMatrices(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)
        
        ##matriz A
        a[0][0]=float(self.ui.txt_a00.text())
        a[0][1]=float(self.ui.txt_a01.text())
        a[0][2]=float(self.ui.txt_a02.text())
        a[1][0]=float(self.ui.txt_a10.text())
        a[1][1]=float(self.ui.txt_a11.text())
        a[1][2]=float(self.ui.txt_a12.text())
        a[2][0]=float(self.ui.txt_a20.text())
        a[2][1]=float(self.ui.txt_a21.text())
        a[2][2]=float(self.ui.txt_a22.text())

        ##matriz B
        b[0][0]=float(self.ui.txt_b00.text())
        b[0][1]=float(self.ui.txt_b01.text())
        b[0][2]=float(self.ui.txt_b02.text())
        b[1][0]=float(self.ui.txt_b10.text())
        b[1][1]=float(self.ui.txt_b11.text())
        b[1][2]=float(self.ui.txt_b12.text())
        b[2][0]=float(self.ui.txt_b20.text())
        b[2][1]=float(self.ui.txt_b21.text())
        b[2][2]=float(self.ui.txt_b22.text())
        
        ##matriz resultado
        ##matriz A - matriz B
        resultado[0][0]=a[0][0]-b[0][0]
        resultado[0][1]=a[0][1]-b[0][1]
        resultado[0][2]=a[0][2]-b[0][2]
        resultado[1][0]=a[1][0]-b[1][0]
        resultado[1][1]=a[1][1]-b[1][1]
        resultado[1][2]=a[1][2]-b[1][2]
        resultado[2][0]=a[2][0]-b[2][0]
        resultado[2][1]=a[2][1]-b[2][1]
        resultado[2][2]=a[2][2]-b[2][2]
        
        ##mostrar matriz resultado
        self.ui.lbl_ab00.setText(str(resultado[0][0]))
        self.ui.lbl_ab01.setText(str(resultado[0][1]))
        self.ui.lbl_ab02.setText(str(resultado[0][2]))
        self.ui.lbl_ab10.setText(str(resultado[1][0]))
        self.ui.lbl_ab11.setText(str(resultado[1][1]))
        self.ui.lbl_ab12.setText(str(resultado[1][2]))
        self.ui.lbl_ab20.setText(str(resultado[2][0]))
        self.ui.lbl_ab21.setText(str(resultado[2][1]))
        self.ui.lbl_ab22.setText(str(resultado[2][2]))

    ##multiplicacion de matrices
    def multiplicacionMatrices(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0]*3)
                resultado.append([0]*3)
        
        ##matriz A
        a[0][0]=float(self.ui.txt_ma00.text())
        a[0][1]=float(self.ui.txt_ma01.text())
        a[0][2]=float(self.ui.txt_ma02.text())
        a[1][0]=float(self.ui.txt_ma10.text())
        a[1][1]=float(self.ui.txt_ma11.text())
        a[1][2]=float(self.ui.txt_ma12.text())
        a[2][0]=float(self.ui.txt_ma20.text())
        a[2][1]=float(self.ui.txt_ma21.text())
        a[2][2]=float(self.ui.txt_ma22.text())

        ##matriz B
        b[0][0]=float(self.ui.txt_mb00.text())
        b[0][1]=float(self.ui.txt_mb01.text())
        b[0][2]=float(self.ui.txt_mb02.text())
        b[1][0]=float(self.ui.txt_mb10.text())
        b[1][1]=float(self.ui.txt_mb11.text())
        b[1][2]=float(self.ui.txt_mb12.text())
        b[2][0]=float(self.ui.txt_mb20.text())
        b[2][1]=float(self.ui.txt_mb21.text())
        b[2][2]=float(self.ui.txt_mb22.text())
        
        ##matriz resultado
        ##matriz A * matriz B
        resultado[0][0]=a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0]
        resultado[0][1]=a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1]
        resultado[0][2]=a[0][0]*b[0][2] + a[0][1]*b[1][2] + a[0][2]*b[2][2]
        resultado[1][0]=a[1][0]*b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0]
        resultado[1][1]=a[1][0]*b[0][1] + a[1][1]*b[1][1] + a[1][2]*b[2][1]
        resultado[1][2]=a[1][0]*b[0][2] + a[1][1]*b[1][2] + a[1][2]*b[2][2]
        resultado[2][0]=a[2][0]*b[0][0] + a[2][1]*b[1][0] + a[2][2]*b[2][0]
        resultado[2][1]=a[2][0]*b[0][1] + a[2][1]*b[1][1] + a[2][2]*b[2][1]
        resultado[2][2]=a[2][0]*b[0][2] + a[2][1]*b[1][2] + a[2][2]*b[2][2]
        
        ##mostrar matriz resultado
        self.ui.lbl_abm00.setText(str(resultado[0][0]))
        self.ui.lbl_abm01.setText(str(resultado[0][1]))
        self.ui.lbl_abm02.setText(str(resultado[0][2]))
        self.ui.lbl_abm10.setText(str(resultado[1][0]))
        self.ui.lbl_abm11.setText(str(resultado[1][1]))
        self.ui.lbl_abm12.setText(str(resultado[1][2]))
        self.ui.lbl_abm20.setText(str(resultado[2][0]))
        self.ui.lbl_abm21.setText(str(resultado[2][1]))
        self.ui.lbl_abm22.setText(str(resultado[2][2]))
    
    ##transpuesta de matriz
    def transpuestaMatriz(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                resultado.append([0]*3)
        ##matriz A
        a[0][0]=float(self.ui.txt_ta00.text())
        a[0][1]=float(self.ui.txt_ta01.text())
        a[0][2]=float(self.ui.txt_ta02.text())
        a[1][0]=float(self.ui.txt_ta10.text())
        a[1][1]=float(self.ui.txt_ta11.text())
        a[1][2]=float(self.ui.txt_ta12.text())
        a[2][0]=float(self.ui.txt_ta20.text())
        a[2][1]=float(self.ui.txt_ta21.text())
        a[2][2]=float(self.ui.txt_ta22.text())

        ##matriz transpuesta
        resultado[0][0]=a[0][0]
        resultado[0][1]=a[1][0]
        resultado[0][2]=a[2][0]
        resultado[1][0]=a[0][1]
        resultado[1][1]=a[1][1]
        resultado[1][2]=a[2][1]
        resultado[2][0]=a[0][2]
        resultado[2][1]=a[1][2]
        resultado[2][2]=a[2][2]

        ##mostrar matriz transpuesta
        self.ui.lbl_at00.setText(str(resultado[0][0]))
        self.ui.lbl_at01.setText(str(resultado[0][1]))
        self.ui.lbl_at02.setText(str(resultado[0][2]))
        self.ui.lbl_at10.setText(str(resultado[1][0]))
        self.ui.lbl_at11.setText(str(resultado[1][1]))
        self.ui.lbl_at12.setText(str(resultado[1][2]))
        self.ui.lbl_at20.setText(str(resultado[2][0]))
        self.ui.lbl_at21.setText(str(resultado[2][1]))
        self.ui.lbl_at22.setText(str(resultado[2][2]))
    
    ##determinante de matriz
    def determinanteMatriz(self):
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
        ##matriz A
        a[0][0]=float(self.ui.txt_da00.text())
        a[0][1]=float(self.ui.txt_da01.text())
        a[0][2]=float(self.ui.txt_da02.text())
        a[1][0]=float(self.ui.txt_da10.text())
        a[1][1]=float(self.ui.txt_da11.text())
        a[1][2]=float(self.ui.txt_da12.text())
        a[2][0]=float(self.ui.txt_da20.text())
        a[2][1]=float(self.ui.txt_da21.text())
        a[2][2]=float(self.ui.txt_da22.text())

        ##determinante
        ##|D|=DP-DS
        det=a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1]-a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[0][0]*a[1][2]*a[2][1]

        ##mostrar determinante
        self.ui.lbl_determinante.setText(str(det))
    
    ##matriz adjunta
    def adjuntaMatriz(self):
        ##mm = matriz menor
        mm = []
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                mm.append([0]*3)
                resultado.append([0]*3)
        ##matriz a
        a[0][0]=float(self.ui.txt_Ma00.text())
        a[0][1]=float(self.ui.txt_Ma01.text())
        a[0][2]=float(self.ui.txt_Ma02.text())
        a[1][0]=float(self.ui.txt_Ma10.text())
        a[1][1]=float(self.ui.txt_Ma11.text())
        a[1][2]=float(self.ui.txt_Ma12.text())
        a[2][0]=float(self.ui.txt_Ma20.text())
        a[2][1]=float(self.ui.txt_Ma21.text())
        a[2][2]=float(self.ui.txt_Ma22.text())

        ##sacando matriz menor
        ##matriz cofactores
        mm[0][0]=a[1][1]*a[2][2]-a[1][2]*a[2][1]
        mm[0][1]=-(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        mm[0][2]=a[1][0]*a[2][1]-a[1][1]*a[2][0]
        mm[1][0]=-(a[0][1]*a[2][2]-a[0][2]*a[2][1])
        mm[1][1]=a[0][0]*a[2][2]-a[0][2]*a[2][0]
        mm[1][2]=-(a[0][0]*a[2][1]-a[0][1]*a[2][0])
        mm[2][0]=a[0][1]*a[1][2]-a[0][2]*a[1][1]
        mm[2][1]=-(a[0][0]*a[1][2]-a[0][2]*a[1][0])
        mm[2][2]=a[0][0]*a[1][1]-a[0][1]*a[1][0]

        ##transponer matriz cofactores
        ##resultado = matriz adjunta
        resultado[0][0]=mm[0][0]
        resultado[0][1]=mm[1][0]
        resultado[0][2]=mm[2][0]
        resultado[1][0]=mm[0][1]
        resultado[1][1]=mm[1][1]
        resultado[1][2]=mm[2][1]
        resultado[2][0]=mm[0][2]
        resultado[2][1]=mm[1][2]
        resultado[2][2]=mm[2][2]

        ##mostrar matriz adjunta
        self.ui.lbl_adj00.setText(str(resultado[0][0]))
        self.ui.lbl_adj01.setText(str(resultado[0][1]))
        self.ui.lbl_adj02.setText(str(resultado[0][2]))
        self.ui.lbl_adj10.setText(str(resultado[1][0]))
        self.ui.lbl_adj11.setText(str(resultado[1][1]))
        self.ui.lbl_adj12.setText(str(resultado[1][2]))
        self.ui.lbl_adj20.setText(str(resultado[2][0]))
        self.ui.lbl_adj21.setText(str(resultado[2][1]))
        self.ui.lbl_adj22.setText(str(resultado[2][2]))

    ##matriz inversa
    def inversaMatriz(self):
        ##mm = matriz menor
        mm = []
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                mm.append([0]*3)
                resultado.append([0]*3)
        
        ##matriz a
        a[0][0]=float(self.ui.txt_Ia00.text())
        a[0][1]=float(self.ui.txt_Ia01.text())
        a[0][2]=float(self.ui.txt_Ia02.text())
        a[1][0]=float(self.ui.txt_Ia10.text())
        a[1][1]=float(self.ui.txt_Ia11.text())
        a[1][2]=float(self.ui.txt_Ia12.text())
        a[2][0]=float(self.ui.txt_Ia20.text())
        a[2][1]=float(self.ui.txt_Ia21.text())
        a[2][2]=float(self.ui.txt_Ia22.text())

        ##det = Dp - Ds
        ##sacamos el determinante de la matriz A
        det=a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1]-a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[0][0]*a[1][2]*a[2][1]

        ##matriz adjunta
        ##sacando matriz menor
        ##tambien aplicamos la matriz de signos
        mm[0][0]=a[1][1]*a[2][2]-a[1][2]*a[2][1]
        mm[0][1]=-(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        mm[0][2]=a[1][0]*a[2][1]-a[1][1]*a[2][0]
        mm[1][0]=-(a[0][1]*a[2][2]-a[0][2]*a[2][1])
        mm[1][1]=a[0][0]*a[2][2]-a[0][2]*a[2][0]
        mm[1][2]=-(a[0][0]*a[2][1]-a[0][1]*a[2][0])
        mm[2][0]=a[0][1]*a[1][2]-a[0][2]*a[1][1]
        mm[2][1]=-(a[0][0]*a[1][2]-a[0][2]*a[1][0])
        mm[2][2]=a[0][0]*a[1][1]-a[0][1]*a[1][0]

        ##transponer matriz de cofactores
        ##resultado = matriz adjunta
        resultado[0][0]=mm[0][0]
        resultado[0][1]=mm[1][0]
        resultado[0][2]=mm[2][0]
        resultado[1][0]=mm[0][1]
        resultado[1][1]=mm[1][1]
        resultado[1][2]=mm[2][1]
        resultado[2][0]=mm[0][2]
        resultado[2][1]=mm[1][2]
        resultado[2][2]=mm[2][2]

        ##mostrar matriz inversa
        ##1/det * matriz adjunta
        self.ui.lbl_inv00.setText(str(resultado[0][0]/det))
        self.ui.lbl_inv01.setText(str(resultado[0][1]/det))
        self.ui.lbl_inv02.setText(str(resultado[0][2]/det))
        self.ui.lbl_inv10.setText(str(resultado[1][0]/det))
        self.ui.lbl_inv11.setText(str(resultado[1][1]/det))
        self.ui.lbl_inv12.setText(str(resultado[1][2]/det))
        self.ui.lbl_inv20.setText(str(resultado[2][0]/det))
        self.ui.lbl_inv21.setText(str(resultado[2][1]/det))
        self.ui.lbl_inv22.setText(str(resultado[2][2]/det))

    ##matriz metodo adjunta
    def metodoAdjunta(self):
        ##mm = matriz menor
        mm = []
        adjunta = []
        inversa = []
        for i in range(3):
            for j in range(3):
                a.append([0]*3)
                b.append([0])
                mm.append([0]*3)
                adjunta.append([0]*3)
                inversa.append([0]*3)
                resultado.append([0])
        
        ##cosntruir 2 matrices A y B
        ##matriz A
        a[0][0]=float(self.ui.txt_EcAdj00.text())
        a[0][1]=float(self.ui.txt_EcAdj01.text())
        a[0][2]=float(self.ui.txt_EcAdj02.text())
        a[1][0]=float(self.ui.txt_EcAdj10.text())
        a[1][1]=float(self.ui.txt_EcAdj11.text())
        a[1][2]=float(self.ui.txt_EcAdj12.text())
        a[2][0]=float(self.ui.txt_EcAdj20.text())
        a[2][1]=float(self.ui.txt_EcAdj21.text())
        a[2][2]=float(self.ui.txt_EcAdj22.text())

        ##matriz B
        b[0][0]=float(self.ui.txt_EcMb00.text())
        b[1][0]=float(self.ui.txt_EcMb10.text())
        b[2][0]=float(self.ui.txt_EcMb20.text())
        
        ##determinante de la matriz A
        ##det = Dp - Ds, el signo menos aplica para toda la diagonal secundaria
        det=a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1]-a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[0][0]*a[1][2]*a[2][1]

        ##sacando MM
        ##tambien aplicamos la matriz de signos
        ##matriz cofactores
        mm[0][0] = a[1][1]*a[2][2]-a[1][2]*a[2][1]
        mm[0][1] = -(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        mm[0][2] = a[1][0]*a[2][1]-a[1][1]*a[2][0]
        mm[1][0] = -(a[0][1]*a[2][2]-a[0][2]*a[2][1])
        mm[1][1] = a[0][0]*a[2][2]-a[0][2]*a[2][0]
        mm[1][2] = -(a[0][0]*a[2][1]-a[0][1]*a[2][0])
        mm[2][0] = a[0][1]*a[1][2]-a[0][2]*a[1][1]
        mm[2][1] = -(a[0][0]*a[1][2]-a[0][2]*a[1][0])
        mm[2][2] = a[0][0]*a[1][1]-a[0][1]*a[1][0]

        ##transponer matriz cofactores
        ##matriz adjunta
        adjunta[0][0]=mm[0][0]
        adjunta[0][1]=mm[1][0]
        adjunta[0][2]=mm[2][0]
        adjunta[1][0]=mm[0][1]
        adjunta[1][1]=mm[1][1]
        adjunta[1][2]=mm[2][1]
        adjunta[2][0]=mm[0][2]
        adjunta[2][1]=mm[1][2]
        adjunta[2][2]=mm[2][2]

        ##matriz adjunta por el determinante de la matriz A
        ##matriz inversa
        inversa [0][0] = adjunta[0][0]/det
        inversa [0][1] = adjunta[0][1]/det
        inversa [0][2] = adjunta[0][2]/det
        inversa [1][0] = adjunta[1][0]/det
        inversa [1][1] = adjunta[1][1]/det
        inversa [1][2] = adjunta[1][2]/det
        inversa [2][0] = adjunta[2][0]/det
        inversa [2][1] = adjunta[2][1]/det
        inversa [2][2] = adjunta[2][2]/det

        ##Multiplicar la inversa por la matriz B
        ##matriz por el metodo adjunto
        resultado[0][0]=inversa[0][0]*b[0][0] + inversa[0][1]*b[1][0] + inversa[0][2]*b[2][0]
        resultado[1][0]=inversa[1][0]*b[0][0] + inversa[1][1]*b[1][0] + inversa[1][2]*b[2][0]
        resultado[2][0]=inversa[2][0]*b[0][0] + inversa[2][1]*b[1][0] + inversa[2][2]*b[2][0]

        ##mostrar matriz por metodo adjunto
        self.ui.lbl_Mc00.setText(str(resultado[0][0]))
        self.ui.lbl_Mc10.setText(str(resultado[1][0]))
        self.ui.lbl_Mc20.setText(str(resultado[2][0]))

    ##matriz por metodo de cramer
    def metodoCramer(self):
        ##construir 4 matrices
        ##matriz sistema
        Msys = []
        ##matriz Mx
        Mx = []
        ##matriz My
        My = []
        ##matriz Mz
        Mz = []
        for i in range(3):
            for j in range(3):
                Msys.append([0]*3)
                Mx.append([0]*3)
                My.append([0]*3)
                Mz.append([0]*3)
               
        ##matriz Msys
        Msys[0][0]=float(self.ui.txt_EcS00.text())
        Msys[0][1]=float(self.ui.txt_EcS01.text())
        Msys[0][2]=float(self.ui.txt_EcS02.text())
        Msys[1][0]=float(self.ui.txt_EcS10.text())
        Msys[1][1]=float(self.ui.txt_EcS11.text())
        Msys[1][2]=float(self.ui.txt_EcS12.text())
        Msys[2][0]=float(self.ui.txt_EcS20.text())
        Msys[2][1]=float(self.ui.txt_EcS21.text())
        Msys[2][2]=float(self.ui.txt_EcS22.text())

        ##matriz Mx
        Mx[0][0]=float(self.ui.txt_EcC00.text())
        Mx[0][1]=float(self.ui.txt_EcS01.text())
        Mx[0][2]=float(self.ui.txt_EcS02.text())
        Mx[1][0]=float(self.ui.txt_EcC10.text())
        Mx[1][1]=float(self.ui.txt_EcS11.text())
        Mx[1][2]=float(self.ui.txt_EcS12.text())
        Mx[2][0]=float(self.ui.txt_EcC20.text())
        Mx[2][1]=float(self.ui.txt_EcS21.text())
        Mx[2][2]=float(self.ui.txt_EcS22.text())
        
        ##matriz My
        My[0][0]=float(self.ui.txt_EcS00.text())
        My[0][1]=float(self.ui.txt_EcC00.text())
        My[0][2]=float(self.ui.txt_EcS02.text())
        My[1][0]=float(self.ui.txt_EcS10.text())
        My[1][1]=float(self.ui.txt_EcC10.text())
        My[1][2]=float(self.ui.txt_EcS12.text())
        My[2][0]=float(self.ui.txt_EcS20.text())
        My[2][1]=float(self.ui.txt_EcC20.text())
        My[2][2]=float(self.ui.txt_EcS22.text())

        ##matriz Mz
        Mz[0][0]=float(self.ui.txt_EcS00.text())
        Mz[0][1]=float(self.ui.txt_EcS01.text())
        Mz[0][2]=float(self.ui.txt_EcC00.text())
        Mz[1][0]=float(self.ui.txt_EcS10.text())
        Mz[1][1]=float(self.ui.txt_EcS11.text())
        Mz[1][2]=float(self.ui.txt_EcC10.text())
        Mz[2][0]=float(self.ui.txt_EcS20.text())
        Mz[2][1]=float(self.ui.txt_EcS21.text())
        Mz[2][2]=float(self.ui.txt_EcC20.text())

        ##calcular determinantes
        ## det = DP - DS
        ##determinante de la matriz sistema
        detsys = Msys[0][0]*Msys[1][1]*Msys[2][2] + Msys[0][1]*Msys[1][2]*Msys[2][0] + Msys[0][2]*Msys[1][0]*Msys[2][1] - Msys[0][2]*Msys[1][1]*Msys[2][0] - Msys[0][1]*Msys[1][0]*Msys[2][2] - Msys[0][0]*Msys[1][2]*Msys[2][1]
        
        ##determinante de la matriz Mx
        detx = Mx[0][0]*Mx[1][1]*Mx[2][2] + Mx[0][1]*Mx[1][2]*Mx[2][0] + Mx[0][2]*Mx[1][0]*Mx[2][1] - Mx[0][2]*Mx[1][1]*Mx[2][0] - Mx[0][1]*Mx[1][0]*Mx[2][2] - Mx[0][0]*Mx[1][2]*Mx[2][1]

        ##determinante de la matriz My
        dety = My[0][0]*My[1][1]*My[2][2] + My[0][1]*My[1][2]*My[2][0] + My[0][2]*My[1][0]*My[2][1] - My[0][2]*My[1][1]*My[2][0] - My[0][1]*My[1][0]*My[2][2] - My[0][0]*My[1][2]*My[2][1]

        ##determinante de la matriz Mz
        detz = Mz[0][0]*Mz[1][1]*Mz[2][2] + Mz[0][1]*Mz[1][2]*Mz[2][0] + Mz[0][2]*Mz[1][0]*Mz[2][1] - Mz[0][2]*Mz[1][1]*Mz[2][0] - Mz[0][1]*Mz[1][0]*Mz[2][2] - Mz[0][0]*Mz[1][2]*Mz[2][1]
        
        ##se calcula el valor de x, y, z 
        ##det x,y,z / determinante del sistema
        x = detx/detsys
        y = dety/detsys
        z = detz/detsys

        #mostrar resultados
        ##se muestra lo que equiovale a x
        self.ui.lbl_rCramer00.setText(str(x))
        ##se muestra lo que equiovale a y
        self.ui.lbl_rCramer10.setText(str(y))
        ##se muestra lo que equiovale a z
        self.ui.lbl_rCramer20.setText(str(z))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = FormularioParcial()
    myapp.show()
    sys.exit(app.exec())

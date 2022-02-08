#juego de 3 en raya
# 1º intento de 3 en raya - clase tablero

from jugador import Jugador

class Tablero():
    #lista, matriz del tablero 3x3
    turno=0
    #matriz puede hacerse con lista= [[" "]*3]*3 --> genera una matriz de 3x3 
    matriz_tablero=[
        ["00","01","02"],
        ["10","11","12"],
        ["20","21","22"]
    ]
    def __init__(self,jugador1,jugador2):
        #crea los jugadores y comprueba que no tienen la misma marca elegida
        self.jugador1=jugador1
        self.jugador2=jugador2
        self.comprobar_marca()
    
    def comprobar_marca(self):
        #mientras la marca sea igual pide al jugador 2 una marca distinta 
        while self.jugador1.pieza == self.jugador2.pieza:
            print("la marca del jugador 2 no puede ser igual a jugador 1")
            self.jugador2.cambia_tu_pieza()

    def mostrar_estado_tablero(self):
        #imprime el estado actual de juego
        for i in self.matriz_tablero:
            datos=""
            for j in i:
                datos=datos +" " + j
            print(datos)
    
    #tirada del jugador 1 -- si quiere poner la pieza en un sitio con pieza le decimos que elija otro lugar
    #devuelve true o false segun pueda o no hacer el movicmento
    def tirada_j1(self):
        try:
            print("turno jugador: ", self.jugador1.nombre)
            x=int(input("coordena x: "))
            y=int(input("coordenada Y: "))
            if self.matriz_tablero[x][y] == self.jugador1.pieza:
                print("ya pertenece al jugador: ", self.jugador1.nombre)
            elif self.matriz_tablero[x][y] == self.jugador2.pieza:
                print("ya pertenece al jugador: ", self.jugador1.nombre)
            else:
                tirada=self.jugador1.turno(x,y)
                self.matriz_tablero[tirada[0]][tirada[1]]=self.jugador1.pieza
                return True
            return False
        except:
            print("datos no validos")
            return False
            

    #tirada del jugador 2 -- si quiere poner la pieza en un sitio con pieza le decimos que elija otro lugar
    #devuelve true o false segun pueda o no hacer el movicmento
    def tirada_j2(self):
        try:
            print("turno jugador: ", self.jugador2.nombre)
            x=int(input("coordena x: "))
            y=int(input("coordenada Y: "))
            if self.matriz_tablero[x][y] == self.jugador1.pieza:
                print("ya pertenece al jugador: ", self.jugador1.nombre)
            elif self.matriz_tablero[x][y] == self.jugador2.pieza:
                print("ya pertenece al jugador: ", self.jugador1.nombre)
            else:
                tirada=self.jugador2.turno(x,y)#tupla que guarda x e y
                self.matriz_tablero[tirada[0]][tirada[1]]=self.jugador2.pieza
                return True
            return False
        except:
            print("datos no validos")
            return False
            

    def comprobar_ganador1(self):
        #si ha ganado uno
        if self.matriz_tablero[0][0]==self.jugador1.pieza and self.matriz_tablero[0][1]==self.jugador1.pieza and self.matriz_tablero[0][2]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[1][0]==self.jugador1.pieza and self.matriz_tablero[1][1]==self.jugador1.pieza and self.matriz_tablero[1][2]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[2][0]==self.jugador1.pieza and self.matriz_tablero[2][1]==self.jugador1.pieza and self.matriz_tablero[2][2]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][0]==self.jugador1.pieza and self.matriz_tablero[1][0]==self.jugador1.pieza and self.matriz_tablero[2][0]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][2]==self.jugador1.pieza and self.matriz_tablero[1][1]==self.jugador1.pieza and self.matriz_tablero[2][1]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][2]==self.jugador1.pieza and self.matriz_tablero[1][2]==self.jugador1.pieza and self.matriz_tablero[2][2]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][0]==self.jugador1.pieza and self.matriz_tablero[1][1]==self.jugador1.pieza and self.matriz_tablero[2][2]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][2]==self.jugador1.pieza and self.matriz_tablero[1][1]==self.jugador1.pieza and self.matriz_tablero[2][0]==self.jugador1.pieza:
            print("GANADOR: " ,self.jugador1.nombre)
            self.mostrar_estado_tablero()
            exit(0)

    def comprobar_ganador2(self):
        #si ha ganado uno
        if self.matriz_tablero[0][0]==self.jugador2.pieza and self.matriz_tablero[0][1]==self.jugador2.pieza and self.matriz_tablero[0][2]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[1][0]==self.jugador2.pieza and self.matriz_tablero[1][1]==self.jugador2.pieza and self.matriz_tablero[1][2]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[2][0]==self.jugador2.pieza and self.matriz_tablero[2][1]==self.jugador2.pieza and self.matriz_tablero[2][2]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][0]==self.jugador2.pieza and self.matriz_tablero[1][0]==self.jugador2.pieza and self.matriz_tablero[2][0]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][2]==self.jugador2.pieza and self.matriz_tablero[1][1]==self.jugador2.pieza and self.matriz_tablero[2][1]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][2]==self.jugador2.pieza and self.matriz_tablero[1][2]==self.jugador2.pieza and self.matriz_tablero[2][2]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            self.mostrar_estado_tablero()
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][0]==self.jugador2.pieza and self.matriz_tablero[1][1]==self.jugador2.pieza and self.matriz_tablero[2][2]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            self.mostrar_estado_tablero()
            exit(0)
        elif self.matriz_tablero[0][2]==self.jugador2.pieza and self.matriz_tablero[1][1]==self.jugador2.pieza and self.matriz_tablero[2][0]==self.jugador2.pieza:
            print("GANADOR: " ,self.jugador2.nombre)
            exit(0)
    
    #cuidado en el bucel porque la comprobacion al no ser par salta del 8 al 10 y nunca terminaba - se comprueba en cada suma de partida
    def partida(self):
        while self.turno <= 9:
            self.turno+=1
            print("turno= ",self.turno)
            turno1=False
            turno2=False
            while turno1==False and self.turno<= 9:
                turno1=self.tirada_j1()
                self.comprobar_ganador1()
                self.comprobar_ganador2()
            self.turno+=1
            print("turno= ",self.turno)
            self.mostrar_estado_tablero()
            while turno2==False  and self.turno<= 9:
                turno2=self.tirada_j2()
                self.comprobar_ganador1()
                self.comprobar_ganador2()
            self.mostrar_estado_tablero()
        print("EMPATE")
            

j1=Jugador("juan",12,"X")
j2=Jugador("laura",12,"w")

tablero=Tablero(j1,j2)
print(tablero.jugador1)
print(tablero.jugador2)
#tablero.mostrar_estado_tablero()
#tablero.tirada_j1()
#tablero.mostrar_estado_tablero()
#print(tablero.tirada_j2())
#tablero.mostrar_estado_tablero()
tablero.partida()
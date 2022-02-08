#los 2 jugadores que juegan al 3 en raya 

class Jugador():
       

    def __init__(self,nombre,edad,pieza):
        self.nombre=nombre
        self.edad=edad
        self.pieza=pieza.upper()

    def cambia_tu_pieza(self):
        self.pieza = str(input("introduce tu marca para jugar: "))
        self.pieza=self.pieza.upper()

    def __str__(self):
        return f"Datos del jugador: \nnombre: {self.nombre}\nedad: {self.edad}\npieza: {self.pieza}"

    def turno(self,x,y):
        turno=(x,y)
        
        return turno
import random
import tkinter as tk
import time
class CapaManager:
    def __init__(self):
        self.capas = []

    def agregar_capa(self, capa):
        #print(f'Capas antes de agregar: {self.capas}')  # Añade esta línea
        self.capas.append(capa)
        #print(f'Capas después de agregar: {self.capas}')  # Añade esta línea

    def obtener_capas(self):
        return self.capas   
    
    def obtener_num_capas(self):
        return len(self.capas)

    def obtener_dimensiones_capa(self):
        if self.capas:
            return len(self.capas[0]), len(self.capas[0][0])
        return 0, 0  # Si no hay capas, devuelve 0,0


    def obtener_vecinos(self, num_capa, fila, columna, num_capas, filas, columnas):
        # Asumiendo vecindad de Moore en 3D entre la misma celda y capas adyacentes
        vecinos = []
        #print(num_capa, fila, columna, num_capas, filas, columnas)
        # Vecinos dentro de la misma capa
        for i in range(max(0, fila - 1), min(fila + 2, filas)):
            for j in range(max(0, columna - 1), min(columna + 2, columnas)):
                if (i, j) != (fila, columna):  # Evitar la celda actual
                    vecinos.append((num_capa, i, j))  # Mismo número de capa
                    #print("vecinos misma capa",vecinos)
        # Vecino en la capa anterior (capa inferior)
        if num_capa > 0:
            vecinos.append((num_capa - 1, fila, columna))
            #print("vecinos capa inferior",vecinos)
        # Vecino en la capa siguiente (capa superior)
        if num_capa < num_capas - 1:
            vecinos.append((num_capa + 1, fila, columna))
            #print("vecimos capa superior",vecinos)
        return vecinos


    def determinar_nuevo_estado(self, estado_actual, estados_vecinos):
        # Define los parámetros de transición del modelo SEIR
        tasa_infeccion = 0.4  # Probabilidad de pasar de S a E cuando se está en contacto con I
        tasa_incubacion = 0.9  # Probabilidad de pasar de E a I
        tasa_recuperacion = 0.2  # Probabilidad de pasar de I a R
        tasa_reinfeccion = 0.2 # Probabilidad de pasar de R a I


        nuevo_estado = estado_actual  # Por defecto, el estado no cambia a menos que se cumplan las condiciones

        if estado_actual == 'S':
            # Si la celda actual es susceptible (S), verificamos si hay vecinos infectados (I)
            vecinos_infectados = estados_vecinos.count('I')
            print("S",vecinos_infectados)
            if vecinos_infectados > 0:
                # La probabilidad de infección aumenta con el número de vecinos infectados
                #print("Sus",(1 - (1 - tasa_infeccion)**vecinos_infectados))
                if random.random() < (tasa_infeccion *vecinos_infectados):
                    nuevo_estado = 'E'  # La celda se convierte en expuesta (E)
                    
        elif estado_actual == 'E':
            vecinos_infectados = estados_vecinos.count('I')
            print("E",vecinos_infectados)
            if vecinos_infectados > 0:
                #print("Exp",(1 - (1 - tasa_incubacion)**vecinos_infectados))
                # Si la celda está expuesta (E), puede convertirse en infectada (I) o seguir expuesta
                if random.random() < (tasa_incubacion*vecinos_infectados):
                    nuevo_estado = 'I'  # La celda se convierte en infectada (I)
                    
        elif estado_actual == 'I':
            # Si la celda está infectada (I), puede recuperarse (R) o seguir infectada
            if random.random() < tasa_recuperacion:
                nuevo_estado = 'R'  # La celda se convierte en recuperada (R)

        elif estado_actual == 'R':
            vecinos_infectados = estados_vecinos.count('I')
            #print("R",vecinos_infectados)
            if vecinos_infectados > 0:
                #print("Rec",(1 - (1 - tasa_reinfeccion)**vecinos_infectados))
                # Si la celda está recuperada (R), puede convertirse en expuesta (e) o seguir recuperada
                if random.random() < (tasa_reinfeccion*vecinos_infectados):
                    nuevo_estado = 'S'  # La celda se convierte en expuesta (I)
        return nuevo_estado


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

        # Vecinos dentro de la misma capa
        for i in range(max(0, fila - 1), min(fila + 2, filas)):
            for j in range(max(0, columna - 1), min(columna + 2, columnas)):
                if (i, j) != (fila, columna):  # Evitar la celda actual
                    vecinos.append((num_capa, i, j))  # Mismo número de capa

        # Vecino en la capa anterior (capa inferior)
        if num_capa > 0:
            vecinos.append((num_capa - 1, fila, columna))

        # Vecino en la capa siguiente (capa superior)
        if num_capa < num_capas - 1:
            vecinos.append((num_capa + 1, fila, columna))

        return vecinos

    def actualizar_capas(self):
        nuevas_capas = [capa.copy() for capa in self.capas]
        registrar = open("cambios.txt", "a")

        # Probabilidades de transición entre estados
        tasa_infeccion = 0.7
        tasa_incubacion = 0.5
        tasa_recuperacion = 0.2
        tasa_reinfeccion = 0.6

        for num_capa, capa in enumerate(self.capas):
            for fila in range(len(capa)):
                for columna in range(len(capa[fila])):
                    estado_actual = nuevas_capas[num_capa][fila][columna]

                    if estado_actual['S'] > 0:
                        
                        probabilidad_infeccion = tasa_infeccion
                        #print("prob Infeccion",probabilidad_infeccion)
                        cambios = self.generar_cambios(estado_actual['S'], probabilidad_infeccion)
                        nuevas_capas[num_capa][fila][columna]['S'] -= cambios
                        nuevas_capas[num_capa][fila][columna]['E'] += cambios
                        registrar.write("Quitamos a S {} y Agregamos a E {}\n".format(cambios, cambios))
                        
                    if estado_actual['E'] > 0:
                
                        probabilidad_incubacion = tasa_incubacion
                        #print("prob Incubacion",probabilidad_incubacion)
                        cambios = self.generar_cambios(estado_actual['E'], probabilidad_incubacion)
                        nuevas_capas[num_capa][fila][columna]['E'] -= cambios
                        nuevas_capas[num_capa][fila][columna]['I'] += cambios
                        registrar.write("Quitamos a E {} y Agregamos a I {}\n".format(cambios, cambios))
                        
                    if estado_actual['I'] > 0:
                        probabilidad_recuperacion = tasa_recuperacion
                        #print("prob recuperacion",probabilidad_recuperacion )
                        cambios = self.generar_cambios(estado_actual['I'], probabilidad_recuperacion)
                        nuevas_capas[num_capa][fila][columna]['I'] -= cambios
                        nuevas_capas[num_capa][fila][columna]['R'] += cambios
                        registrar.write("Quitamos a I {} y Agregamos a R {}\n".format(cambios, cambios))
                        

                    if estado_actual['R'] > 0:
                        probabilidad_reinfeccion = tasa_reinfeccion  
                        #print("prob reinfectar",probabilidad_reinfeccion)
                        cambios = self.generar_cambios(estado_actual['R'], probabilidad_reinfeccion)
                        nuevas_capas[num_capa][fila][columna]['R'] -= cambios
                        nuevas_capas[num_capa][fila][columna]['S'] += cambios
                        registrar.write("Quitamos a R {} y Agregamos a S {}\n".format(cambios, cambios))
                        registrar.write("\n")
        # Actualizamos las capas originales con los nuevos estados
        self.capas = nuevas_capas

    def generar_cambios(self, poblacion, probabilidad):
        cambios = 0
        for _ in range(poblacion):
            if random.random() < probabilidad:
                cambios += 1
        return cambios

    def imprimir_capas(self):
        for num, capa in enumerate(self.capas):
            print(f"Capa {num}:")
            for fila in capa:
                fila_str = [str(estado) for estado in fila]  # Convertir estados a strings
                print(" ".join(fila_str))




    #def ejecutar_simulacion(self, pasos):
    #    for paso in range(pasos):
    #        print(f"Estado de la simulación en el paso {paso}:")
    #        self.imprimir_capas()  # Imprime el estado actual de las capas
    #        self.actualizar_capas()  # Actualiza las capas para el siguiente paso
    #        print("\n")  # Espacio entre pasos para mejor visualización
    def ejecutar_simulacion(self, pasos):
        
        for paso in range(pasos):
            print(f"Estado de la simulación en el paso {paso} antes de actualizar:")
            self.imprimir_capas()  # Imprime el estado actual de las capas antes de actualizar
            self.actualizar_capas()  # Actualiza las capas para el siguiente paso
            print(f"Estado de la simulación en el paso {paso} después de actualizar:")
            self.imprimir_capas()  # Imprime el estado actual de las capas después de actualizar
            print("\n")  # Espacio entre pasos para mejor visualización


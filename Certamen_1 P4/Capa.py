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

        # Vecino en la capa inferior
        if num_capa > 0:
            vecinos.append((num_capa - 1, fila, columna))

        # Vecino en la capa superior
        if num_capa < num_capas - 1:
            vecinos.append((num_capa + 1, fila, columna))

        return vecinos

    def transitar_poblacion_entre_celdas(self, probabilidad):
        registrar = open("cambios_celdas.txt", "a")
        nuevas_capas = [capa.copy() for capa in self.capas]

        for num_capa, capa in enumerate(self.capas):
            for fila in range(len(capa)):
                for columna in range(len(capa[fila])):
                    estado_actual = nuevas_capas[num_capa][fila][columna]

                    # Pasamos la poblacion actual total
                    poblacion_total = sum(estado_actual.values())
                    poblacion_maxima = 100 #determinamos la poblacion para efectos de sobrepoblacion

                    if poblacion_total > poblacion_maxima:
                        # Registra las celdas con sobrepoblación
                        # borrar txt cuando corran el codigo
                        registro_sobrepoblacion = f"Capa {num_capa}, Celda ({fila}, {columna}) tiene sobrepoblación ({poblacion_total} > {poblacion_maxima})"
                        registrar.write(registro_sobrepoblacion + "\n")

                    # Verificamos que hay población.
                    if poblacion_total > 0:
                        vecinos = self.obtener_vecinos(num_capa, fila, columna, len(self.capas), len(capa), len(capa[fila]))

                        for estado_origen in estado_actual:
                            for vecino in vecinos: #formato vecino (1,1,1)
                                vecino_capa, vecino_fila, vecino_columna = vecino
                                estado_destino = nuevas_capas[vecino_capa][vecino_fila][vecino_columna]

                                # Verifica si el vecino tiene sobrepoblación antes de transferir población
                                poblacion_vecino = sum(estado_destino.values())
                                if poblacion_vecino <= poblacion_maxima:
                                    # Calcula la población que puede transitar desde el estado_origen al estado_destino
                                    poblacion_transitada = int(estado_actual[estado_origen] * probabilidad)

                                    # Asegura que la población transitada no supere lo que tiene la celda actual
                                    poblacion_transitada = min(poblacion_transitada, estado_actual[estado_origen])

                                    # Transfiere la población a la celda vecina
                                    estado_actual[estado_origen] -= poblacion_transitada
                                    estado_destino[estado_origen] += poblacion_transitada

                                    # Registra los cambios en el archivo incluyendo información de capa y celda
                                    registro = f"Capa {num_capa}, Celda ({fila}, {columna}) -> Capa {vecino_capa}, Celda ({vecino_fila}, {vecino_columna}): "
                                    registro += f"{estado_origen} -> {estado_origen} ({poblacion_transitada})"
                                    registrar.write(registro + "\n")

        # Actualiza las capas originales con los nuevos estados
        self.capas = nuevas_capas

    
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
                        
                        #print("prob Infeccion",probabilidad_infeccion)
                        cambios = self.generar_cambios(estado_actual['S'], tasa_infeccion)
                        nuevas_capas[num_capa][fila][columna]['S'] -= cambios
                        nuevas_capas[num_capa][fila][columna]['E'] += cambios
                        registrar.write("Quitamos a S {} y Agregamos a E {}\n".format(cambios, cambios))
                        
                    if estado_actual['E'] > 0:
                
                        #print("prob Incubacion",probabilidad_incubacion)
                        cambios = self.generar_cambios(estado_actual['E'], tasa_incubacion)
                        nuevas_capas[num_capa][fila][columna]['E'] -= cambios
                        nuevas_capas[num_capa][fila][columna]['I'] += cambios
                        registrar.write("Quitamos a E {} y Agregamos a I {}\n".format(cambios, cambios))
                        
                    if estado_actual['I'] > 0:
                        #print("prob recuperacion",probabilidad_recuperacion )
                        cambios = self.generar_cambios(estado_actual['I'], tasa_recuperacion)
                        nuevas_capas[num_capa][fila][columna]['I'] -= cambios
                        nuevas_capas[num_capa][fila][columna]['R'] += cambios
                        registrar.write("Quitamos a I {} y Agregamos a R {}\n".format(cambios, cambios))
                        

                    if estado_actual['R'] > 0:

                        #print("prob reinfectar",probabilidad_reinfeccion)
                        cambios = self.generar_cambios(estado_actual['R'], tasa_reinfeccion)
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
                fila_str = [str(estado) for estado in fila]  # Pasa los estados a strings
                print(" ".join(fila_str))


    def ejecutar_simulacion(self, pasos,probabilidad):
        
        for paso in range(pasos):
            print(f"Estado de la simulación en el paso {paso} antes de actualizar:")
            self.imprimir_capas()  # Imprime el estado actual de las capas antes de actualizar
            self.actualizar_capas()  # Actualiza las capas para el siguiente paso
            self.transitar_poblacion_entre_celdas(probabilidad)
            print(f"Estado de la simulación en el paso {paso} después de actualizar:")
            self.imprimir_capas()  # Imprime el estado actual de las capas después de actualizar
            print("\n")  # Espacio entre pasos para mejorar la visualización


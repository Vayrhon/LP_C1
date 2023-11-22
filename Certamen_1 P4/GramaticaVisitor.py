import random
from Capa import CapaManager
import random
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    def __init__(self, capa_manager):
        super().__init__()  # Añadir aquí la lista de capas.
        self.capa_manager = capa_manager

    def get_capas(self):
        return self.capa_manager.obtener_capas()  # Método para obtener todas las capas.

    # Visit a parse tree produced by GramaticaParser#programa.
    def visitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        self.visitChildren(ctx)
        return self.capa_manager.obtener_capas()  # Corrección aquí

    # Visit a parse tree produced by GramaticaParser#CAPA.
    def visitCAPA(self, ctx:GramaticaParser.CAPAContext):
        capa_id = ctx.ID().getText()  # Obtener el ID de la capa
        dimensiones_texto = ctx.INT()  # Obtener las dimensiones de la capa
        dimensiones = [int(d.getText()) for d in dimensiones_texto]

        # Crear la capa con una distribución de población para cada celda
        capa = []
        for i in range(dimensiones[0]):
            fila = []
            for j in range(dimensiones[1]):
                # Distribución aleatoria de la población en cada celda
                total_por_celda = 70  # Valor Inicial de poblacion en la celda
                fila.append(self.inicializar_poblacion(total_por_celda))
            capa.append(fila)

        self.capa_manager.agregar_capa(capa)
        print("Capa",capa_id,capa)

        return {"id": capa_id, "capa": capa}

    def inicializar_poblacion(self, total_por_celda):
        poblacion_celda = {'S': 0, 'E': 0, 'I': 0, 'R': 0}
        for estado in poblacion_celda:
            if estado == 'I':  # Asegurar que siempre haya al menos un infectado
                poblacion_celda[estado] = random.randint(1, total_por_celda)
            else:
                max_valor = max(0, total_por_celda - poblacion_celda['I'])
                poblacion_celda[estado] = random.randint(0, max_valor)
            total_por_celda -= poblacion_celda[estado]
            if total_por_celda <= 0:
                break
        poblacion_celda['S'] += total_por_celda  # Asegurarse de que la suma total sea igual a total_por_celda
        return poblacion_celda

            
    def visitVECINOS(self, ctx:GramaticaParser.VECINOSContext):
        self.num_capas = self.capa_manager.obtener_num_capas()
        self.filas, self.columnas = self.capa_manager.obtener_dimensiones_capa()
        id_capa = int(ctx.INT(0).getText())  
        fila = int(ctx.INT(1).getText())
        columna = int(ctx.INT(2).getText())

        vecinos = self.capa_manager.obtener_vecinos(id_capa, fila, columna, self.num_capas, self.filas, self.columnas)
        print(vecinos)
        return vecinos
    
    def visitSIMULACION(self, ctx:GramaticaParser.SIMULACIONContext):
        pasos = int(ctx.INT(0).getText())
        print(pasos)
        probabilidad = int(ctx.INT(1).getText())
        probabilidad = probabilidad/10
        print(probabilidad)
        #print("Capas",self.capa_manager.obtener_capas())
        self.capa_manager.ejecutar_simulacion(pasos, probabilidad)

del GramaticaParser
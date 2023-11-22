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

        # Estados posibles para la simulación SEIR
        # Las proporciones de S, E, y R se ajustan para dejar espacio para al menos 1 I
        estados = ['S'] * 50 + ['E'] * 20 + ['I'] * 3 + ['R'] * 27  # Ajustar las proporciones como sea necesario

        # Crear la capa con un estado aleatorio para cada celda
        capa = [[random.choice(estados) for _ in range(dimensiones[1])] for _ in range(dimensiones[0])]

        # Asegúrate de que haya al menos un infectado
        # Selecciona una celda aleatoria y cambia su estado a 'I'
        fila_aleatoria = random.randint(0, dimensiones[0] - 1)
        columna_aleatoria = random.randint(0, dimensiones[1] - 1)
        capa[fila_aleatoria][columna_aleatoria] = 'I'

        self.capa_manager.agregar_capa(capa)
        return {"id": capa_id, "capa": capa}
        
    def visitVECINOS(self, ctx:GramaticaParser.VECINOSContext):
        self.num_capas = self.capa_manager.obtener_num_capas()
        self.filas, self.columnas = self.capa_manager.obtener_dimensiones_capa()
        id_capa = int(ctx.INT(0).getText())  # Aquí asumimos que ID es un número
        fila = int(ctx.INT(1).getText())
        columna = int(ctx.INT(2).getText())

        vecinos = self.capa_manager.obtener_vecinos(id_capa, fila, columna, self.num_capas, self.filas, self.columnas)
        print(vecinos)
        return vecinos
    
    def visitSIMULACION(self, ctx:GramaticaParser.SIMULACIONContext):
        pasos = int(ctx.INT().getText())  # Asumiendo que tienes un token NUMERO que define el número de pasos
        self.capa_manager.ejecutar_simulacion(pasos)

del GramaticaParser
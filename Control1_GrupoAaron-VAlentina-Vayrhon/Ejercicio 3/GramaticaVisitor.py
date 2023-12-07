# Generated from Gramatica.g4 by ANTLR 4.13.1

from antlr4 import *
import turtle as t
from turtle import *


if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.
class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#programa.
    def visitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        # Configurar la forma de la tortuga como "turtle"
        t.shape("turtle")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GramaticaParser#comando.
    def visitComando(self, ctx:GramaticaParser.ComandoContext):
        return self.visitChildren(ctx)


        # Visit a parse tree produced by GramaticaParser#MOVER2.
    def visitMOVER2(self, ctx:GramaticaParser.MOVER2Context):
        text = ctx.getText()
        
        # Verificar que el texto esté en el formato esperado
        if text.startswith("mover(") and text.endswith(")"):
            # Eliminar "mover(" y ")" del texto
            text = text.replace("mover(", "").replace(")", "")
            
            # Encuentra la posición de la coma
            comma_position = text.find(",")
            
            if comma_position != -1:
                # Divide el texto en partes usando la coma como separador
                x_str = text[:comma_position].strip()
                y_str = text[comma_position + 1:].strip()
                
                # Convierte los valores de x e y a enteros
                try:
                    x = int(x_str)
                    y = int(y_str)
                    
                    # Calcula el ángulo hacia las nuevas coordenadas (x, y)
                    angle = t.towards(x, y)
                    
                    # Obtiene la distancia hacia las coordenadas (x, y)
                    distance = t.distance(x, y)

                    # Establece la dirección de la tortuga al ángulo calculado
                    t.setheading(angle)
                    
                    # Mueve la tortuga hacia las coordenadas (x, y)
                    t.forward(distance)
                    print(angle)
                    return self.visitChildren(ctx)
                
                except ValueError:
                    print("Error: Los valores de x e y deben ser números enteros.")
                

            else:
                print("Error: El formato del texto debe ser 'mover(x, y)' donde x e y son números enteros.")
        else:
            print("Error: El formato del texto debe ser 'mover(x, y)' donde x e y son números enteros encerrados en paréntesis.")


    # Visit a parse tree produced by GramaticaParser#MOVER1.
    def visitMOVER1(self, ctx:GramaticaParser.MOVER1Context):
        t.forward(int(ctx.INT().getText()))
        return self.visitChildren(ctx)
    # Visit a parse tree produced by GramaticaParser#MOVER1.
    def visitMOVER1(self, ctx:GramaticaParser.MOVER1Context):
        x = int(ctx.INT().getText())
        
        # Verificar si el valor es negativo y ajustarlo en consecuencia
        if '-' in ctx.getText():
            x *= -1

        # Mover la tortuga hacia adelante en la dirección actual
        t.forward(x)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GramaticaParser#ROTAR2.
    def visitROTAR2(self, ctx:GramaticaParser.ROTAR2Context):
        x = int(ctx.INT(0).getText())
        y = int(ctx.INT(1).getText())
        
        # Calcular el ángulo necesario para rotar la tortuga hacia (x, y)
        angulo = t.towards(x, y)
        t.left(angulo)
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GramaticaParser#ROTAR1.
    def visitROTAR1(self, ctx:GramaticaParser.ROTAR1Context):
        # Girar la tortuga a la izquierda en el ángulo especificado
        t.left(int(ctx.INT().getText()))
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by GramaticaParser#MOVERROTAR.
    def visitMOVERROTAR(self, ctx:GramaticaParser.MOVERROTARContext):
        x = int(ctx.INT(0).getText())
        y = int(ctx.INT(1).getText())
        
        # Calcular el ángulo necesario para mover la tortuga a (x, y)
        angulo = t.towards(x, y)
        print("1",angulo)
        t.left(angulo)
        
        # Mover la tortuga a la posición (x, y)
        t.goto(x, y)  
        
        # Girar la tortuga en un ángulo adicional
        angulo2 = int(ctx.INT(2).getText())
        t.left(angulo2 + angulo)
        print("2",angulo2 + angulo)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GramaticaParser#ENCENDER.
    def visitENCENDER(self, ctx:GramaticaParser.ENCENDERContext):
        print("Se bajó el lápiz")
        # Bajar el lápiz de la tortuga
        t.pendown()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GramaticaParser#APAGAR.
    def visitAPAGAR(self, ctx:GramaticaParser.APAGARContext):
        print("Se levantó el lápiz")
        # Levantar el lápiz de la tortuga
        t.penup()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#MOVERROTAR2.
    def visitMOVERROTAR2(self, ctx:GramaticaParser.MOVERROTAR2Context):
        x = int(ctx.INT(0).getText())

        
        # Calcular el ángulo necesario para mover la tortuga a (x, y)
        t.forward(x)
        # Mover la tortuga a la posición (x, y)
        
        # Girar la tortuga en un ángulo adicional
        angulo = int(ctx.INT(1).getText())
        t.left(angulo)
        return self.visitChildren(ctx)

del GramaticaParser
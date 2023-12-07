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
        t.shape("turtle")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#comando.
    def visitComando(self, ctx:GramaticaParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#MOVER2.
    #def visitMOVER2(self, ctx:GramaticaParser.MOVER2Context):
    #def visitMOVER2(self, ctx:GramaticaParser.MOVER2Context):
    #    x = int(ctx.INT(0).getText())
    #    y = int(ctx.INT(1).getText())
        

    #    if '-' in ctx.getText():
    #        x *= -1

    #    if x < 0:
    #        angle = 180 - t.towards(-x, y)
    #    else:
    #        angle = t.towards(x, y)

        # Mueve la tortuga a las coordenadas (x, y)
    #   t.goto(x, y)
        
        # Establece la dirección de la tortuga al ángulo calculado
        #print(angle)
    #    t.setheading(angle)
        
    #    return self.visitChildren(ctx)

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
        t.left(int(ctx.INT().getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ENCENDER.
    def visitENCENDER(self, ctx:GramaticaParser.ENCENDERContext):
        print("Se bajó el lápiz")
        t.pendown()    
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#APAGAR.
    def visitAPAGAR(self, ctx:GramaticaParser.APAGARContext):
        print("Se levantó el lápiz")
        t.penup()
        return self.visitChildren(ctx)



del GramaticaParser
# Generated from Gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
import turtle as t
from turtle import *
import time

if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    current_x = 0

    
    # Visit a parse tree produced by GramaticaParser#programa.
    def visitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        t.shape("turtle")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#comando.
    def visitComando(self, ctx:GramaticaParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#MOVER2.
    def visitMOVER2(self, ctx:GramaticaParser.MOVER2Context):
        x = int(ctx.INT(0).getText())
        y = int(ctx.INT(1).getText())
        #print(x,y)
        angulo = t.towards(x,y)
        t.left(angulo)
        t.goto(x,y)
        return self.visitChildren(ctx)



    # Visit a parse tree produced by GramaticaParser#MOVER1.
    def visitMOVER1(self, ctx:GramaticaParser.MOVER1Context):
        x = int(ctx.INT().getText())
        if '-' in ctx.getText():
            x *= -1

        t.forward(x)
        print(t.position())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ROTAR2.
    def visitROTAR2(self, ctx:GramaticaParser.ROTAR2Context):
        x = int(ctx.INT(0).getText())
        y = int(ctx.INT(1).getText())

        angulo = t.towards(x,y)
        t.left(angulo)
        
        return self.visitChildren(ctx)
        


    # Visit a parse tree produced by GramaticaParser#ROTAR1.
    def visitROTAR1(self, ctx:GramaticaParser.ROTAR1Context):
        t.left(int(ctx.INT().getText()))
        print(t.heading())
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by GramaticaParser#MOVERROTAR.
    def visitMOVERROTAR1(self, ctx:GramaticaParser.MOVERROTAR1Context):
        
        x = int(ctx.INT(0).getText())
        y = int(ctx.INT(1).getText())
        angulo = t.towards(x,y)
        t.left(angulo)
        t.goto(x,y)  
        angulo = int(ctx.INT(2).getText())
        t.left(angulo)
        print(t.position())
        print(t.heading())
        return self.visitChildren(ctx)
    
    def visitMOVERROTAR2(self, ctx:GramaticaParser.MOVERROTAR2Context):

        distancia = int(ctx.INT(0).getText())
        t.forward(distancia)  # Mover hacia adelante la distancia indicada
        angulo_adicional = int(ctx.INT(1).getText())
        t.left(angulo_adicional)  # Rotar un ángulo adicional
        print(t.position())
        print(t.heading())
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by GramaticaParser#LOOP.
    def visitLOOP(self, ctx:GramaticaParser.LOOPContext):
        x = int(ctx.INT().getText())
        for iteration in range(x):
           print(iteration)
           time.sleep(2)
           self.visit(ctx.accion())  # Visita el nodo de la acción especificada
        #return self.visitChildren(ctx)
    # def visitLOOP(self, ctx:GramaticaParser.LOOPContext):
    #     x = int(ctx.INT().getText())
    #     print(x)
    #     for iteration in range(x):
    #         time.sleep(2)
    #         accion_ctx = ctx.accion()
    #         accion_texto = accion_ctx.getText()
    #         print(accion_texto)
    #         num_comas = accion_texto.count(',')
    #         print(type(accion_ctx))
    #         if num_comas == 1:
    #             # Asumiendo que las acciones con dos argumentos tienen una coma en su texto
    #             arg1 = int(accion_ctx.INT(0).getText())
    #             print(arg1)
    #             arg2 = int(accion_ctx.INT(1).getText())
    #             print(arg2)
    #             self.visit(accion_ctx)
    #             print(t.position())
    #             print(t.heading())
    #         elif num_comas == 0:
    #             arg = int(accion_ctx.INT().getText())
    #             # Asume que todas las acciones con un solo argumento son manejadas por el mismo método visitante
    #             self.visit(accion_ctx)
    #     return self.visitChildren(ctx)
    # def visitLOOP(self, ctx:GramaticaParser.LOOPContext):
    #         x = int(ctx.INT().getText()) # Inicializa las coordenadas actuales a (0, 0)
    #         for iteration in range(x):
    #             time.sleep(2)
    #             accion_ctx = ctx.accion()
    #             accion_texto = accion_ctx.getText()
    #             num_comas = accion_texto.count(',')
    #             if num_comas == 1:
    #                 self.visit(accion_ctx)
    #             elif num_comas == 0:
    #                 self.visit(accion_ctx)
    #         return self.visitChildren(ctx)
    
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
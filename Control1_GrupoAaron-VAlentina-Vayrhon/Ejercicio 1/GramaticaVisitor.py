# Generated from Gramatica.g4 by ANTLR 4.13.1


from antlr4 import *
import turtle as t
from turtle import *
import time as tm


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

 # vengo altri
    # Visit a parse tree produced by GramaticaParser#accion.
    def visitAccion(self, ctx:GramaticaParser.AccionContext):
        if ctx.MOVER():
            x = int(ctx.INT(0).getText())
            if len(ctx.INT()) > 1:
                y = int(ctx.INT(1).getText())
                t.left(x) 
                t.forward(y)  
            else:
                t.forward(x)
        elif ( ctx.ENCENDER()):
            print("Se bajó el lápiz")
            t.pendown()
        elif ( ctx.APAGAR() ):
            print("Se levantó el lápiz")

            t.penup()
        return self.visitChildren(ctx)



del GramaticaParser

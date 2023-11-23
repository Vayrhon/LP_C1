# Generated from Gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,48,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,46,8,2,1,2,0,0,3,0,2,4,0,0,48,0,7,1,0,0,0,2,17,1,0,0,0,
        4,45,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,3,4,2,0,14,
        15,5,11,0,0,15,18,1,0,0,0,16,18,5,11,0,0,17,13,1,0,0,0,17,16,1,0,
        0,0,18,3,1,0,0,0,19,20,5,5,0,0,20,21,5,1,0,0,21,22,5,9,0,0,22,23,
        5,2,0,0,23,24,5,3,0,0,24,25,5,1,0,0,25,26,5,8,0,0,26,27,5,4,0,0,
        27,28,5,8,0,0,28,46,5,2,0,0,29,30,5,7,0,0,30,31,5,1,0,0,31,32,5,
        8,0,0,32,33,5,2,0,0,33,34,5,3,0,0,34,35,5,1,0,0,35,36,5,8,0,0,36,
        37,5,4,0,0,37,38,5,8,0,0,38,46,5,2,0,0,39,40,5,6,0,0,40,41,5,1,0,
        0,41,42,5,8,0,0,42,43,5,4,0,0,43,44,5,8,0,0,44,46,5,2,0,0,45,19,
        1,0,0,0,45,29,1,0,0,0,45,39,1,0,0,0,46,5,1,0,0,0,3,9,17,45
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "','", "'capa'", 
                     "'simulacion'", "'vecinos'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CAPA", "SIMULACION", "VECINOS", "INT", 
                      "ID", "V_ID", "NEWLINE", "WS" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_accion = 2

    ruleNames =  [ "programa", "comando", "accion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    CAPA=5
    SIMULACION=6
    VECINOS=7
    INT=8
    ID=9
    V_ID=10
    NEWLINE=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GramaticaParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ComandoContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ComandoContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = GramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.comando()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2272) != 0)):
                    break

            self.state = 11
            self.match(GramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accion(self):
            return self.getTypedRuleContext(GramaticaParser.AccionContext,0)


        def NEWLINE(self):
            return self.getToken(GramaticaParser.NEWLINE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_comando

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = GramaticaParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.accion()
                self.state = 14
                self.match(GramaticaParser.NEWLINE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(GramaticaParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_accion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CAPAContext(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CAPA(self):
            return self.getToken(GramaticaParser.CAPA, 0)
        def ID(self):
            return self.getToken(GramaticaParser.ID, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCAPA" ):
                return visitor.visitCAPA(self)
            else:
                return visitor.visitChildren(self)


    class VECINOSContext(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VECINOS(self):
            return self.getToken(GramaticaParser.VECINOS, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVECINOS" ):
                return visitor.visitVECINOS(self)
            else:
                return visitor.visitChildren(self)


    class SIMULACIONContext(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIMULACION(self):
            return self.getToken(GramaticaParser.SIMULACION, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSIMULACION" ):
                return visitor.visitSIMULACION(self)
            else:
                return visitor.visitChildren(self)



    def accion(self):

        localctx = GramaticaParser.AccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_accion)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = GramaticaParser.CAPAContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(GramaticaParser.CAPA)
                self.state = 20
                self.match(GramaticaParser.T__0)
                self.state = 21
                self.match(GramaticaParser.ID)
                self.state = 22
                self.match(GramaticaParser.T__1)
                self.state = 23
                self.match(GramaticaParser.T__2)
                self.state = 24
                self.match(GramaticaParser.T__0)
                self.state = 25
                self.match(GramaticaParser.INT)
                self.state = 26
                self.match(GramaticaParser.T__3)
                self.state = 27
                self.match(GramaticaParser.INT)
                self.state = 28
                self.match(GramaticaParser.T__1)
                pass
            elif token in [7]:
                localctx = GramaticaParser.VECINOSContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(GramaticaParser.VECINOS)
                self.state = 30
                self.match(GramaticaParser.T__0)
                self.state = 31
                self.match(GramaticaParser.INT)
                self.state = 32
                self.match(GramaticaParser.T__1)
                self.state = 33
                self.match(GramaticaParser.T__2)
                self.state = 34
                self.match(GramaticaParser.T__0)
                self.state = 35
                self.match(GramaticaParser.INT)
                self.state = 36
                self.match(GramaticaParser.T__3)
                self.state = 37
                self.match(GramaticaParser.INT)
                self.state = 38
                self.match(GramaticaParser.T__1)
                pass
            elif token in [6]:
                localctx = GramaticaParser.SIMULACIONContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(GramaticaParser.SIMULACION)
                self.state = 40
                self.match(GramaticaParser.T__0)
                self.state = 41
                self.match(GramaticaParser.INT)
                self.state = 42
                self.match(GramaticaParser.T__3)
                self.state = 43
                self.match(GramaticaParser.INT)
                self.state = 44
                self.match(GramaticaParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






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
        4,1,13,82,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,80,8,2,1,2,0,0,3,0,2,4,0,0,91,0,7,1,0,0,0,2,15,
        1,0,0,0,4,79,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,
        0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,12,0,0,13,16,
        1,0,0,0,14,16,5,12,0,0,15,11,1,0,0,0,15,14,1,0,0,0,16,3,1,0,0,0,
        17,18,5,8,0,0,18,19,5,1,0,0,19,20,5,11,0,0,20,21,5,2,0,0,21,22,5,
        11,0,0,22,80,5,3,0,0,23,24,5,8,0,0,24,25,5,4,0,0,25,26,5,11,0,0,
        26,27,5,5,0,0,27,28,5,11,0,0,28,80,5,3,0,0,29,30,5,8,0,0,30,31,5,
        4,0,0,31,32,5,11,0,0,32,33,5,2,0,0,33,34,5,11,0,0,34,80,5,3,0,0,
        35,36,5,8,0,0,36,37,5,1,0,0,37,38,5,11,0,0,38,39,5,5,0,0,39,40,5,
        11,0,0,40,80,5,3,0,0,41,42,5,8,0,0,42,43,5,1,0,0,43,44,5,11,0,0,
        44,80,5,3,0,0,45,46,5,8,0,0,46,47,5,4,0,0,47,48,5,11,0,0,48,80,5,
        3,0,0,49,50,5,7,0,0,50,51,5,1,0,0,51,52,5,11,0,0,52,53,5,2,0,0,53,
        54,5,11,0,0,54,80,5,3,0,0,55,56,5,7,0,0,56,57,5,1,0,0,57,58,5,11,
        0,0,58,80,5,3,0,0,59,60,5,7,0,0,60,61,5,1,0,0,61,62,5,8,0,0,62,63,
        5,1,0,0,63,64,5,11,0,0,64,65,5,2,0,0,65,66,5,11,0,0,66,67,5,6,0,
        0,67,68,5,11,0,0,68,80,5,3,0,0,69,70,5,7,0,0,70,71,5,1,0,0,71,72,
        5,8,0,0,72,73,5,1,0,0,73,74,5,11,0,0,74,75,5,6,0,0,75,76,5,11,0,
        0,76,80,5,3,0,0,77,80,5,9,0,0,78,80,5,10,0,0,79,17,1,0,0,0,79,23,
        1,0,0,0,79,29,1,0,0,0,79,35,1,0,0,0,79,41,1,0,0,0,79,45,1,0,0,0,
        79,49,1,0,0,0,79,55,1,0,0,0,79,59,1,0,0,0,79,69,1,0,0,0,79,77,1,
        0,0,0,79,78,1,0,0,0,80,5,1,0,0,0,3,9,15,79
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'(-'", "',-'", "') +'", 
                     "'rotar'", "'mover'", "'encender'", "'apagar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ROTAR", "MOVER", 
                      "ENCENDER", "APAGAR", "INT", "NEWLINE", "WS" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_accion = 2

    ruleNames =  [ "programa", "comando", "accion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ROTAR=7
    MOVER=8
    ENCENDER=9
    APAGAR=10
    INT=11
    NEWLINE=12
    WS=13

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6016) != 0)):
                    break

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
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.accion()
                self.state = 12
                self.match(GramaticaParser.NEWLINE)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
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



    class ENCENDERContext(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENCENDER(self):
            return self.getToken(GramaticaParser.ENCENDER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitENCENDER" ):
                return visitor.visitENCENDER(self)
            else:
                return visitor.visitChildren(self)


    class ROTAR1Context(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROTAR(self):
            return self.getToken(GramaticaParser.ROTAR, 0)
        def INT(self):
            return self.getToken(GramaticaParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitROTAR1" ):
                return visitor.visitROTAR1(self)
            else:
                return visitor.visitChildren(self)


    class MOVERROTAR2Context(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROTAR(self):
            return self.getToken(GramaticaParser.ROTAR, 0)
        def MOVER(self):
            return self.getToken(GramaticaParser.MOVER, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMOVERROTAR2" ):
                return visitor.visitMOVERROTAR2(self)
            else:
                return visitor.visitChildren(self)


    class MOVER1Context(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOVER(self):
            return self.getToken(GramaticaParser.MOVER, 0)
        def INT(self):
            return self.getToken(GramaticaParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMOVER1" ):
                return visitor.visitMOVER1(self)
            else:
                return visitor.visitChildren(self)


    class APAGARContext(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def APAGAR(self):
            return self.getToken(GramaticaParser.APAGAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAPAGAR" ):
                return visitor.visitAPAGAR(self)
            else:
                return visitor.visitChildren(self)


    class MOVER2Context(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOVER(self):
            return self.getToken(GramaticaParser.MOVER, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMOVER2" ):
                return visitor.visitMOVER2(self)
            else:
                return visitor.visitChildren(self)


    class ROTAR2Context(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROTAR(self):
            return self.getToken(GramaticaParser.ROTAR, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitROTAR2" ):
                return visitor.visitROTAR2(self)
            else:
                return visitor.visitChildren(self)


    class MOVERROTARContext(AccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.AccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROTAR(self):
            return self.getToken(GramaticaParser.ROTAR, 0)
        def MOVER(self):
            return self.getToken(GramaticaParser.MOVER, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMOVERROTAR" ):
                return visitor.visitMOVERROTAR(self)
            else:
                return visitor.visitChildren(self)



    def accion(self):

        localctx = GramaticaParser.AccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_accion)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = GramaticaParser.MOVER2Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(GramaticaParser.MOVER)
                self.state = 18
                self.match(GramaticaParser.T__0)
                self.state = 19
                self.match(GramaticaParser.INT)
                self.state = 20
                self.match(GramaticaParser.T__1)
                self.state = 21
                self.match(GramaticaParser.INT)
                self.state = 22
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 2:
                localctx = GramaticaParser.MOVER2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(GramaticaParser.MOVER)
                self.state = 24
                self.match(GramaticaParser.T__3)
                self.state = 25
                self.match(GramaticaParser.INT)
                self.state = 26
                self.match(GramaticaParser.T__4)
                self.state = 27
                self.match(GramaticaParser.INT)
                self.state = 28
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 3:
                localctx = GramaticaParser.MOVER2Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(GramaticaParser.MOVER)
                self.state = 30
                self.match(GramaticaParser.T__3)
                self.state = 31
                self.match(GramaticaParser.INT)
                self.state = 32
                self.match(GramaticaParser.T__1)
                self.state = 33
                self.match(GramaticaParser.INT)
                self.state = 34
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 4:
                localctx = GramaticaParser.MOVER2Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(GramaticaParser.MOVER)
                self.state = 36
                self.match(GramaticaParser.T__0)
                self.state = 37
                self.match(GramaticaParser.INT)
                self.state = 38
                self.match(GramaticaParser.T__4)
                self.state = 39
                self.match(GramaticaParser.INT)
                self.state = 40
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 5:
                localctx = GramaticaParser.MOVER1Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.match(GramaticaParser.MOVER)
                self.state = 42
                self.match(GramaticaParser.T__0)
                self.state = 43
                self.match(GramaticaParser.INT)
                self.state = 44
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 6:
                localctx = GramaticaParser.MOVER1Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.match(GramaticaParser.MOVER)
                self.state = 46
                self.match(GramaticaParser.T__3)
                self.state = 47
                self.match(GramaticaParser.INT)
                self.state = 48
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 7:
                localctx = GramaticaParser.ROTAR2Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.match(GramaticaParser.ROTAR)
                self.state = 50
                self.match(GramaticaParser.T__0)
                self.state = 51
                self.match(GramaticaParser.INT)
                self.state = 52
                self.match(GramaticaParser.T__1)
                self.state = 53
                self.match(GramaticaParser.INT)
                self.state = 54
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 8:
                localctx = GramaticaParser.ROTAR1Context(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 55
                self.match(GramaticaParser.ROTAR)
                self.state = 56
                self.match(GramaticaParser.T__0)
                self.state = 57
                self.match(GramaticaParser.INT)
                self.state = 58
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 9:
                localctx = GramaticaParser.MOVERROTARContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.match(GramaticaParser.ROTAR)
                self.state = 60
                self.match(GramaticaParser.T__0)
                self.state = 61
                self.match(GramaticaParser.MOVER)
                self.state = 62
                self.match(GramaticaParser.T__0)
                self.state = 63
                self.match(GramaticaParser.INT)
                self.state = 64
                self.match(GramaticaParser.T__1)
                self.state = 65
                self.match(GramaticaParser.INT)
                self.state = 66
                self.match(GramaticaParser.T__5)
                self.state = 67
                self.match(GramaticaParser.INT)
                self.state = 68
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 10:
                localctx = GramaticaParser.MOVERROTAR2Context(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 69
                self.match(GramaticaParser.ROTAR)
                self.state = 70
                self.match(GramaticaParser.T__0)
                self.state = 71
                self.match(GramaticaParser.MOVER)
                self.state = 72
                self.match(GramaticaParser.T__0)
                self.state = 73
                self.match(GramaticaParser.INT)
                self.state = 74
                self.match(GramaticaParser.T__5)
                self.state = 75
                self.match(GramaticaParser.INT)
                self.state = 76
                self.match(GramaticaParser.T__2)
                pass

            elif la_ == 11:
                localctx = GramaticaParser.ENCENDERContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 77
                self.match(GramaticaParser.ENCENDER)
                pass

            elif la_ == 12:
                localctx = GramaticaParser.APAGARContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 78
                self.match(GramaticaParser.APAGAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






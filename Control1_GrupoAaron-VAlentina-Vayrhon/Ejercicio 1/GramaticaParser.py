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
        4,1,9,32,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,1,
        1,1,1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,30,8,2,1,2,0,0,3,0,2,4,0,0,33,0,7,1,0,0,0,2,15,1,0,0,0,4,
        29,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,8,0,0,13,16,1,0,0,0,14,
        16,5,8,0,0,15,11,1,0,0,0,15,14,1,0,0,0,16,3,1,0,0,0,17,18,5,4,0,
        0,18,19,5,1,0,0,19,20,5,7,0,0,20,30,5,2,0,0,21,22,5,4,0,0,22,23,
        5,1,0,0,23,24,5,7,0,0,24,25,5,3,0,0,25,26,5,7,0,0,26,30,5,2,0,0,
        27,30,5,5,0,0,28,30,5,6,0,0,29,17,1,0,0,0,29,21,1,0,0,0,29,27,1,
        0,0,0,29,28,1,0,0,0,30,5,1,0,0,0,3,9,15,29
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'mover'", "'encender'", 
                     "'apagar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MOVER", "ENCENDER", "APAGAR", "INT", "NEWLINE", "WS" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_accion = 2

    ruleNames =  [ "programa", "comando", "accion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MOVER=4
    ENCENDER=5
    APAGAR=6
    INT=7
    NEWLINE=8
    WS=9

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 368) != 0)):
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
            if token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.accion()
                self.state = 12
                self.match(GramaticaParser.NEWLINE)
                pass
            elif token in [8]:
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

        def MOVER(self):
            return self.getToken(GramaticaParser.MOVER, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.INT)
            else:
                return self.getToken(GramaticaParser.INT, i)

        def ENCENDER(self):
            return self.getToken(GramaticaParser.ENCENDER, 0)

        def APAGAR(self):
            return self.getToken(GramaticaParser.APAGAR, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_accion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccion" ):
                return visitor.visitAccion(self)
            else:
                return visitor.visitChildren(self)




    def accion(self):

        localctx = GramaticaParser.AccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_accion)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(GramaticaParser.MOVER)
                self.state = 18
                self.match(GramaticaParser.T__0)
                self.state = 19
                self.match(GramaticaParser.INT)
                self.state = 20
                self.match(GramaticaParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(GramaticaParser.MOVER)
                self.state = 22
                self.match(GramaticaParser.T__0)
                self.state = 23
                self.match(GramaticaParser.INT)
                self.state = 24
                self.match(GramaticaParser.T__2)
                self.state = 25
                self.match(GramaticaParser.INT)
                self.state = 26
                self.match(GramaticaParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(GramaticaParser.ENCENDER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(GramaticaParser.APAGAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






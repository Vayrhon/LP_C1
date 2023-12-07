# Generated from Gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,64,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,4,6,49,8,6,11,6,12,6,50,1,7,3,7,54,8,7,1,7,1,7,1,8,4,8,
        59,8,8,11,8,12,8,60,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,1,0,2,1,0,48,57,2,0,9,9,32,32,66,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,21,1,0,0,0,5,23,1,0,0,0,
        7,25,1,0,0,0,9,31,1,0,0,0,11,40,1,0,0,0,13,48,1,0,0,0,15,53,1,0,
        0,0,17,58,1,0,0,0,19,20,5,40,0,0,20,2,1,0,0,0,21,22,5,41,0,0,22,
        4,1,0,0,0,23,24,5,44,0,0,24,6,1,0,0,0,25,26,5,109,0,0,26,27,5,111,
        0,0,27,28,5,118,0,0,28,29,5,101,0,0,29,30,5,114,0,0,30,8,1,0,0,0,
        31,32,5,101,0,0,32,33,5,110,0,0,33,34,5,99,0,0,34,35,5,101,0,0,35,
        36,5,110,0,0,36,37,5,100,0,0,37,38,5,101,0,0,38,39,5,114,0,0,39,
        10,1,0,0,0,40,41,5,97,0,0,41,42,5,112,0,0,42,43,5,97,0,0,43,44,5,
        103,0,0,44,45,5,97,0,0,45,46,5,114,0,0,46,12,1,0,0,0,47,49,7,0,0,
        0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,14,
        1,0,0,0,52,54,5,13,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,
        55,56,5,10,0,0,56,16,1,0,0,0,57,59,7,1,0,0,58,57,1,0,0,0,59,60,1,
        0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,6,8,0,0,63,
        18,1,0,0,0,4,0,50,53,60,1,6,0,0
    ]

class GramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    MOVER = 4
    ENCENDER = 5
    APAGAR = 6
    INT = 7
    NEWLINE = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'mover'", "'encender'", "'apagar'" ]

    symbolicNames = [ "<INVALID>",
            "MOVER", "ENCENDER", "APAGAR", "INT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "MOVER", "ENCENDER", "APAGAR", 
                  "INT", "NEWLINE", "WS" ]

    grammarFileName = "Gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



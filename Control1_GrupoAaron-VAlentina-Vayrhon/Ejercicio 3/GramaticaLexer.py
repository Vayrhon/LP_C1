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
        4,0,13,88,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,4,10,73,8,10,11,
        10,12,10,74,1,11,3,11,78,8,11,1,11,1,11,1,12,4,12,83,8,12,11,12,
        12,12,84,1,12,1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,1,0,2,1,0,48,57,2,0,9,9,32,32,90,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,
        0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,
        0,7,33,1,0,0,0,9,36,1,0,0,0,11,39,1,0,0,0,13,43,1,0,0,0,15,49,1,
        0,0,0,17,55,1,0,0,0,19,64,1,0,0,0,21,72,1,0,0,0,23,77,1,0,0,0,25,
        82,1,0,0,0,27,28,5,40,0,0,28,2,1,0,0,0,29,30,5,44,0,0,30,4,1,0,0,
        0,31,32,5,41,0,0,32,6,1,0,0,0,33,34,5,40,0,0,34,35,5,45,0,0,35,8,
        1,0,0,0,36,37,5,44,0,0,37,38,5,45,0,0,38,10,1,0,0,0,39,40,5,41,0,
        0,40,41,5,32,0,0,41,42,5,43,0,0,42,12,1,0,0,0,43,44,5,114,0,0,44,
        45,5,111,0,0,45,46,5,116,0,0,46,47,5,97,0,0,47,48,5,114,0,0,48,14,
        1,0,0,0,49,50,5,109,0,0,50,51,5,111,0,0,51,52,5,118,0,0,52,53,5,
        101,0,0,53,54,5,114,0,0,54,16,1,0,0,0,55,56,5,101,0,0,56,57,5,110,
        0,0,57,58,5,99,0,0,58,59,5,101,0,0,59,60,5,110,0,0,60,61,5,100,0,
        0,61,62,5,101,0,0,62,63,5,114,0,0,63,18,1,0,0,0,64,65,5,97,0,0,65,
        66,5,112,0,0,66,67,5,97,0,0,67,68,5,103,0,0,68,69,5,97,0,0,69,70,
        5,114,0,0,70,20,1,0,0,0,71,73,7,0,0,0,72,71,1,0,0,0,73,74,1,0,0,
        0,74,72,1,0,0,0,74,75,1,0,0,0,75,22,1,0,0,0,76,78,5,13,0,0,77,76,
        1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,5,10,0,0,80,24,1,0,0,0,
        81,83,7,1,0,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,
        0,0,0,85,86,1,0,0,0,86,87,6,12,0,0,87,26,1,0,0,0,4,0,74,77,84,1,
        6,0,0
    ]

class GramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    ROTAR = 7
    MOVER = 8
    ENCENDER = 9
    APAGAR = 10
    INT = 11
    NEWLINE = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "'(-'", "',-'", "') +'", "'rotar'", "'mover'", 
            "'encender'", "'apagar'" ]

    symbolicNames = [ "<INVALID>",
            "ROTAR", "MOVER", "ENCENDER", "APAGAR", "INT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "ROTAR", 
                  "MOVER", "ENCENDER", "APAGAR", "INT", "NEWLINE", "WS" ]

    grammarFileName = "Gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



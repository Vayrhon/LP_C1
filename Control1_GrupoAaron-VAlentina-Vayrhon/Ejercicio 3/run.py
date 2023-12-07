import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaVisitor import GramaticaVisitor

if __name__ == '__main__':
    while (True):
        if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
        else:
            input_stream = InputStream(sys.stdin.readline())

        lexer = GramaticaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = GramaticaParser(token_stream)
        tree = parser.programa()

        visitor = GramaticaVisitor()
        visitor.visit(tree)

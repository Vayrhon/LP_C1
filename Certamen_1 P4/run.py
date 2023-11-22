import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaVisitor import GramaticaVisitor
from Capa import CapaManager

if __name__ == '__main__':
    capa_manager = CapaManager()

    # Comprobar si se ha proporcionado el archivo de entrada como argumento
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        print("No se proporcionó un archivo de entrada.")
        sys.exit(1)  # Salir si no se proporcionó el archivo de entrada

    lexer = GramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GramaticaParser(token_stream)
    tree = parser.programa()

    # Utilizar la misma instancia de CapaManager
    visitor = GramaticaVisitor(capa_manager)
    visitor.visit(tree)

    #capas_originales = capa_manager.capas_iniciales  # Obtén las capas usando CapaManager
    #print("capas", capas_originales)

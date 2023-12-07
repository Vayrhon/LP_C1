grammar Gramatica;

programa: comando+ ;

comando: accion NEWLINE 
       | NEWLINE
       ;

accion:  MOVER '('INT','INT')' #MOVER2
       | MOVER '('INT')'       #MOVER1
       | ROTAR '('INT','INT')' #ROTAR2
       | MOVER '(-'INT',-'INT')' #MOVER2
       | MOVER '(-'INT','INT')' #MOVER2
       | MOVER '('INT',-'INT')' #MOVER2
       | ROTAR '('INT')'       #ROTAR1
       | ENCENDER              #ENCENDER
       | APAGAR                #APAGAR
       ; 

ROTAR: 'rotar';
MOVER: 'mover'; 
ENCENDER: 'encender';
APAGAR: 'apagar';
INT: [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
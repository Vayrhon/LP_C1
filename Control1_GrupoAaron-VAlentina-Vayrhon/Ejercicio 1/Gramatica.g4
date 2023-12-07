grammar Gramatica;

programa: comando+ ;

comando: accion NEWLINE
       | NEWLINE
       ;

accion:  MOVER '('INT')' 
       | MOVER '('INT','INT')'
       | ENCENDER 
       | APAGAR
       ; 

MOVER: 'mover'; 
ENCENDER: 'encender';
APAGAR: 'apagar';
INT: [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
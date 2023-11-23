grammar Gramatica;

// Reglas
programa: comando+ EOF;

comando: accion NEWLINE 
       | NEWLINE
       ;

accion: CAPA '(' ID ')' ':' '(' INT ',' INT ')'  #CAPA
    //| SIMULACION '(' INT ')'                     #SIMULACION
    | VECINOS '(' INT ')' ':' '('INT ',' INT')'     #VECINOS

    ;

// Tokens
CAPA: 'capa';          

VECINOS: 'vecinos';
INT: [0-9]+; 
ID: [a-zA-Z][0-9]+; 
NEWLINE: '\r'? '\n' ;
WS: [ \t\r\n]+ -> skip;               
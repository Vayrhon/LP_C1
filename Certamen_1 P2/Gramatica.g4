grammar Gramatica;

// Reglas
programa: comando+ EOF;

comando: accion NEWLINE 
       | NEWLINE
       ;

accion: CAPA '(' ID ')' ':' '(' INT ',' INT ')'  #CAPA
    | VECINOS '(' INT ')' ':' '('INT ',' INT')'     #VECINOS
    | SIMULACION '(' INT ')'                     #SIMULACION

    ;

// Tokens
CAPA: 'capa';                // Identificador
SIMULACION: 'simulacion';
VECINOS: 'vecinos';
//ESTADO: 'estado';
//VECINDAD: 'vecindad';
//REGLA: 'regla';
//TRANSICION: 'transicion';
INT: [0-9]+; 
ID: [a-zA-Z][0-9]+; 
V_ID: [a-zA-Z_][a-zA-Z_0-9]*;  // Identificador de Vecindad                       // Número entero
NEWLINE: '\r'? '\n' ;
WS: [ \t\r\n]+ -> skip;               // Espacios en blanco
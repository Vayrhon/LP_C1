grammar Gramatica;

programa: comando+ ;

comando: accion NEWLINE 
       | NEWLINE
       ;
//rotar(mover(20,20) + 90)
accion:  MOVER '('INT','INT')'                   #MOVER2
       | MOVER '(-'INT',-'INT')' #MOVER2
       | MOVER '(-'INT','INT')' #MOVER2
       | MOVER '('INT',-'INT')' #MOVER2
       | MOVER '('INT')'                         #MOVER1
       | MOVER '(-'INT')'                        #MOVER1
       | ROTAR '('INT','INT')'                   #ROTAR2
       | ROTAR '('INT')'                         #ROTAR1
       | ROTAR '('MOVER '('INT','INT') +' INT')' #MOVERROTAR
       | ROTAR '('MOVER '('INT') +' INT')' #MOVERROTAR2  
       | ENCENDER                                #ENCENDER
       | APAGAR                                  #APAGAR
       ; 

ROTAR: 'rotar';
MOVER: 'mover'; 
ENCENDER: 'encender';
APAGAR: 'apagar';
INT: [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
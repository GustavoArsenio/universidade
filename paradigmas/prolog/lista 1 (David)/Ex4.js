var NUMEBRS=new Array()
NUMEBRS.push(01)
NUMEBRS.push(10)
NUMEBRS.push(02)
NUMEBRS.push(20)

// Retornando maior valor
var FILTRAR_MAIOR_VALOR = (value1 , value2)  => (value1 > value2) ? value1 : value2

NUMEBRS.reduce( FILTRAR_MAIOR_VALOR )
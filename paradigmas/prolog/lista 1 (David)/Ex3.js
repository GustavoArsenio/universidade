var NUMEBRS=new Array()
NUMEBRS.push(01)
NUMEBRS.push(10)
NUMEBRS.push(02)
NUMEBRS.push(20)

// Verificando se eh divisivel por 10 e retornando apenas os pertencentes
var PRINTAR_MULTIPLOS_DE_10 = value => ! (value % 10) && console.log(value)
NUMEBRS.forEach(PRINTAR_MULTIPLOS_DE_10)
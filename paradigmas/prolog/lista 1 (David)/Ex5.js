// Salário Bruto até      900 (inclusive) - isento
// Salário Bruto até      1500 (inclusive) - desconto de 5%
// Salário Bruto até      2500 (inclusive) - desconto de 10%
// Salário Bruto acima de 2500 - desconto de 20%

var Salarios_Brutos = new Array()

Salarios_Brutos.push(0800)
Salarios_Brutos.push(1400)
Salarios_Brutos.push(2400)
Salarios_Brutos.push(2600)

// Configurando Descontos

var ISENTO      = salario => (salario <= 0900)                       ? salario        : salario
var DESCONTO_5  = salario => (salario >  0900) && (salario <= 1500)  ? salario * 0.95 : salario
var DESCONTO_10 = salario => (salario >  1500) && (salario <= 2500)  ? salario * 0.90 : salario
var DESCONTO_20 = salario => (salario >  2500)                       ? salario * 0.75 : salario



Salarios_Brutos.map(ISENTO).map(DESCONTO_5).map(DESCONTO_10).map(DESCONTO_20)
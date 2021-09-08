#!/bin/sh
INPUT_FILE="input.txt"

gfortran ./calculadora_seletiva.f90 -o my_program
for op in $(seq 1 9);do
    
    echo " Operacao: $op"
    echo ${op}      >        ${INPUT_FILE}
    echo "Numeros: "
    echo "2 3"      | tee -a ${INPUT_FILE}
    ./my_program <        ${INPUT_FILE}
    echo  '\n\n\n'
done
rm ${INPUT_FILE}
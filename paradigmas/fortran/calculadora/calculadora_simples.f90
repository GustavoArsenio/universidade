program calculadora
    implicit none
    character :: operador
    real      :: A,B
    print *, '┌-----------------------------------------------------┐'
    print *, '| Digite a formula(simples) e separado por espaços :  |'
    print *, '|  Ex:  1 + 2                                         |'
    print *, '|       1 * 2                                         |'
    print *, '└-----------------------------------------------------┘'
    read (*,*) A, operador, B


    if (operador == '**') then
        print *, a, '  ** ' , b , ' = ', a  ** b
    else if (operador == '*') then
        print *, a, '  *  ' , b , ' = ', a  *  b
    else if (operador == '/') then
        print *, a, '  /  ' , b , ' = ', a  /  b
    else if (operador == '+') then
        print *, a, '  +  ' , b , ' = ', a  +  b
    else if (operador == '-') then
        print *, a, '  -  ' , b , ' = ', a  -  b
    end if


end program calculadora
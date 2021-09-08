program calculadora
    integer :: operador
    ! call system('clear')
    print *, '┌-------------------------------┐'
    print *, '| 1 - SOMA                      |'
    print *, '| 2 - SUBTRAÇÃO                 |'
    print *, '| 3 - MULTIPLICAÇÃO             |'
    print *, '| 4 - DIVISÃO                   |'
    print *, '| 5 - ELEVAR NUMERO AO QUADRADO |'
    print *, '| 6 - ELEVAR NUMERO AO CUBO     |'
    print *, '| 7 - RAIZ QUADRADA             |'
    print *, '| 8 - RAIZ CÚBICA               |'
    print *, '| 9 - LOGARITMO                 |'
    print *, '└-------------------------------┘'
    read (*,*) operador

    print *,    '┌------------------------------------------------------------------┐'    

    if (operador .LE. 4) then
        CALL DOIS_VALORES(operador)
    else
        CALL UM_VALOR(operador)
    end if 
    
    print *,    '└------------------------------------------------------------------┘'
    
end program calculadora
SUBROUTINE DOIS_VALORES(op) 
    IMPLICIT NONE
    integer :: op
    real    :: A,B
    print *,'|>>> Digite os valores de A e B. (Separados por espaços)           |'
    read (*,*) A, B
    select case (op)
    case (1)
        write (*,*) '|***                            SOMA                            ***|'
        write (*,*) '|    ', A, '   + ', B, ' = ', A+B,                                '|'
    case (2)
        write (*,*) '|***                          SUBTRAÇÃO                         ***|'
        write (*,*) '|    ', A, '   - ', B, ' = ', A-B,                                '|'
    case (3)
        write (*,*) '|***                        MULTIPLICAÇÃO                       ***|'
        write (*,*) '|    ', A, '   * ', B, ' = ', A*B,                                '|'
    case (4)
        write (*,*) '|***                           DIVISÃO                          ***|'
        write (*,*) '|    ', A, '   / ', B, ' = ', A/B,                                '|'
    end select  
END

SUBROUTINE UM_VALOR(op)
    IMPLICIT NONE
        integer :: op
        real    :: A
        print *,'|>>> Digite os valores de A.                                       |'
        read (*,*) A
        SELECT CASE (op)
        case (5)
            write (*,*) '|***                  ELEVAR NUMEROS AO QUADRADO                ***|'
            write (*,*) '|    ', A, '   ^   2 = '    , A ** 2,              '               |'
        case (6)
            write (*,*) '|***                    ELEVAR NUMEROS AO CUBO                  ***|'
            write (*,*) '|    ', A, '   ^   3 = '    , A ** 3,              '               |'
        case (7)
            write (*,*) '|***                        RAIZ QUADRADA                       ***|'
            write (*,*) '|   √', A, '   =   '        , sqrt(A),         '                   |'
        case (8)
            write (*,*) '|***                         RAIZ CUBICA                        ***|'
            write (*,*) '|  ³√', A, '   =   '        ,A ** ( 1.0 / 3.0),'                   |'
        case (9)
            write (*,*) '|***                          LOGARITMO                         ***|'
            write (*,*) '|LOG(', A, ')  =   '        , log(A),          '                   |'
        end select  
END


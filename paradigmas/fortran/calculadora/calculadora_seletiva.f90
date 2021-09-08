program calculadora

    character :: operador
    real      :: A,B
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

    print *,' >>> Digite os valores de A e B. (Separados por espaços)'
    read (*,*) A, B

    print *,    '┌------------------------------------------------------------------┐'
    select case (operador)
    case ('1')
        write (*,*) '|***                            SOMA                            ***|'
        write (*,*) '|    ', A, '   + ', B, ' = ', A+B,                                '|'
    case ('2')
        write (*,*) '|***                          SUBTRAÇÃO                         ***|'
        write (*,*) '|    ', A, '   - ', B, ' = ', A-B,                                '|'
    case ('3')
        write (*,*) '|***                        MULTIPLICAÇÃO                       ***|'
        write (*,*) '|    ', A, '   * ', B, ' = ', A*B,                                '|'
    case ('4')
        write (*,*) '|***                           DIVISÃO                          ***|'
        write (*,*) '|    ', A, '   / ', B, ' = ', A/B,                                '|'
    case ('5')
        write (*,*) '|***                  ELEVAR NUMEROS AO QUADRADO                ***|'
        write (*,*) '|    ', A, '   ^   2 = '    , A ** 2,              '               |'
        write (*,*) '|    ', B, '   ^   2 = '    , B ** 2,              '               |'
    case ('6')
        write (*,*) '|***                    ELEVAR NUMEROS AO CUBO                  ***|'
        write (*,*) '|    ', A, '   ^   3 = '    , A ** 3,              '               |'
        write (*,*) '|    ', B, '   ^   3 = '    , B ** 3,              '               |'
    case ('7')
        write (*,*) '|***                        RAIZ QUADRADA                       ***|'
        write (*,*) '|   √', A, '   =   '        , sqrt(A),         '                   |'
        write (*,*) '|   √', B, '   =   '        , sqrt(B),         '                   |'
    case ('8')
        write (*,*) '|***                         RAIZ CUBICA                        ***|'
        write (*,*) '|  ³√', A, '   =   '        ,A ** ( 1.0 / 3.0),'                   |'
        write (*,*) '|  ³√', B, '   =   '        ,B ** ( 1.0 / 3.0),'                   |'
    case ('9')
        write (*,*) '|***                          LOGARITMO                         ***|'
        write (*,*) '|LOG(', A, ')  =   '        , log(A),          '                   |'
        write (*,*) '|LOG(', B, ')  =   '        , log(B),          '                   |'
    end select
    
    print *,    '└------------------------------------------------------------------┘'

end program calculadora

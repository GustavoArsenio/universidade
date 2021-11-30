casado(marcelo, juliana).
casado(leia, han).

programador(han).
programador(juliana).
programador(marcos).

filhos(juliana,2).
filhos(marcelo,3).
filhos(leia,1).
filhos(han,1).

viagem(leia,japao).
viagem(han,japao).
viagem(juliana,eua).
viagem(marcos,portugal).

is_casado(Pessoa) :-
    casado(Pessoa,_) |
    casado(_,Pessoa) .

tem_filhos(Pessoa) :- 
    filhos(Pessoa,_).

vai_comprar_nos_eua(Pessoa) :-
    is_casado(Pessoa),
    tem_filhos(Pessoa),
    viagem(Pessoa,eua).
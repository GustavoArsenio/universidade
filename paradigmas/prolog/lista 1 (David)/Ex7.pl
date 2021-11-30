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

esta_viajando_negocios(Pessoa) :-
    programador(Pessoa),
    \+ is_casado(Pessoa).

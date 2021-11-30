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

esta_viajando(Pessoa1,Pessoa2) :-
    casado(Pessoa1,Pessoa2)|
    casado(Pessoa2,Pessoa1),
    viagem(Pessoa1,Local),
    viagem(Pessoa2,Local).
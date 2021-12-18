homem(reginaldo).
homem(bento).
homem(horacio).
homem(meu_tio).

genitor(reginaldo,bento).
genitor(reginaldo,meu_tio).
genitor(bento,horacio).



%// TIO
tio(Tio, Sobrinho) :-
    genitor(Pai, Sobrinho),
    genitor(Avo, Pai),
    genitor(Avo, Tio),
    homem(Tio),
    \+ Tio == Pai.
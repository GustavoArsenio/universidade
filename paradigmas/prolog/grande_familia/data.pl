homem(edgar).
homem(marcio).
homem(rodrigo).
homem(romeu).
homem(roberto).

mulher(julieta).
mulher(maria).
mulher(marcia).
mulher(marta).
mulher(rose).


pai_mae(edgar, julieta).
pai_mae(maria, julieta).

pai_mae(edgar, marcio).
pai_mae(maria, marcio).

pai_mae(rodrigo, romeu).
pai_mae(marcia, romeu).

pai_mae(marcio, roberto).
pai_mae(marta, roberto).

pai_mae(marcio, rose).
pai_mae(marta, rose).

%// Pais
pai(PessoaUm, PessoaDois) :-
    pai_mae(PessoaUm, PessoaDois) ,
    homem(PessoaUm).
mae(PessoaUm, PessoaDois) :-
    pai_mae(PessoaUm, PessoaDois) ,
    mulher(PessoaUm).


%// Irmao ao Irma
mesmos_pais(PessoaUm, PessoaDois) :-
    pai_mae(Pais, PessoaUm) ,
    pai_mae(Pais, PessoaDois) ,
    \+ PessoaUm = PessoaDois.

irmao(PessoaUm, PessoaDois) :-
    mesmos_pais(PessoaUm, PessoaDois) ,
    homem(PessoaUm).
irma(PessoaUm,  PessoaDois) :-
    mesmos_pais(PessoaUm, PessoaDois) ,
    mulher(PessoaUm).

%// Avós
avos(PessoaUm, PessoaDois) :-
    pai_mae( Pais, PessoaDois) ,
    pai_mae(PessoaUm, Pais).

avoo(PessoaUm, PessoaDois) :-
    avos(PessoaUm, PessoaDois) ,
    homem(PessoaUm).
avoh(PessoaUm, PessoaDois) :-
    avos(PessoaUm, PessoaDois) ,
    mulher(PessoaUm).

%// Neto
neto(PessoaUm, PessoaDois) :-
    avos(PessoaDois, PessoaUm).


%// Tios e Primos
tio_tia(PessoaUm, PessoaDois) :- 
    pai_mae(Pais, PessoaDois) ,
    mesmos_pais(Pais ,
    PessoaUm).

tio(PessoaUm, PessoaDois) :- 
    tio_tia(PessoaUm, PessoaDois) ,
    irmao(PessoaUm).

tia(PessoaUm, PessoaDois) :- 
    tio_tia(PessoaUm, PessoaDois) ,
    irma(PessoaUm).


primo(PessoaUm, PessoaDois) :-
    tio_tia(Tios, PessoaUm), pai_mae(Tios, PessoaDois).
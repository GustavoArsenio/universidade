curso(engenharia, programacao).
curso(engenharia, estrutura_de_dados).
curso(engenharia, paradigmas).
%// Ajustado o nome do TCC -> Valores(Strings) nao podem ser em maiusculo
curso(engenharia, tcc).

aluno(jose).

matricula(jose, engenharia).

%// Ex1
pegar_materias(Aluno, Materia) :-
    matricula(Aluno,Curso),
    curso(Curso,Materia).

%// Ex2
valida_materia(Materia, Curso) :-
    curso(Curso,Materia).
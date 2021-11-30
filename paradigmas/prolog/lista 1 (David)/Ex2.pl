curso(engenharia, programacao).
curso(engenharia, estrutura_de_dados).
curso(engenharia, paradigmas).
%// Ajustado o nome do TCC -> Valores(Strings) nao podem ser em maiusculo
curso(engenharia, tcc).

aluno(jose).

matricula(jose, engenharia).

valida_materia(Materia, Curso) :-
    curso(Curso,Materia).
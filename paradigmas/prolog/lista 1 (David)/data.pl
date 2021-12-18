curso(engenharia, programacao).
curso(engenharia, estrutura_de_dados).
curso(engenharia, paradigmas).
%// Ajustado o nome do TCC -> Valores(Strings) nao podem ser em maiusculo
curso(engenharia, tcc).

aluno(jose).

matricula(jose, engenharia).

pegar_materias(Nome_Aluno, Nome_Materia) :-
    matricula(Nome_Aluno,Curso),
    curso(Curso,Nome_Materia).
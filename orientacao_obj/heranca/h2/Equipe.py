from Aluno import Aluno
from functools import reduce

class Equipe():
    def __init__(self,**kwargs):
        self.lista_de_participantes = kwargs['lista_de_participantes']
        self.projeto                = kwargs['projeto']
        GerenciadorEquipe.get_instance().add(self)
    
    def __str__(self):
        return f' Equipe NOME_PROJETO={self.projeto}, LISTA_DE_PARTICIPANTES={self.lista_de_participantes}'


class GerenciadorEquipe():
    __instance = None
    def __init__(self,**kwargs):
        if self.__instance is not None:
            return __instance
        
        self.lst_todas_as_equipes = []
        GerenciadorEquipe.__instance = self

    def add_list(self,lst_nova_equipe):
            for nova_equipe in lst_nova_equipe:
                self.add_equipe(nova_equipe)

    def add_equipe(self,nova_equipe:Equipe):
        projeto       = nova_equipe.projeto
        list_list_personas = [equipe.lista_de_participantes for equipe in self.lst_todas_as_equipes if equipe.projeto == projeto ]

        list_personas =   list_list_personas if len(list_list_personas) == 0 else set(reduce( lambda lista_personas_ant,lista_personas_pos: lista_personas_ant + lista_personas_pos , list_list_personas))

        for persona in nova_equipe.lista_de_participantes:
            if persona in list_personas:
                raise ValueError(f' Aluno: {persona} já incluso no projeto {projeto}')
    
        self.lst_todas_as_equipes.append(nova_equipe)

    @staticmethod
    def get_instance():
        return GerenciadorEquipe.__instance
        
    def add(self,nova_equipe:Equipe):
        switecher_types={
            Equipe : self.add_equipe,
            list   : self.add_list
        }
        function_to_add = switecher_types[type(nova_equipe)]
        function_to_add(nova_equipe)
    
    def __str__(self):
        return f' Equipes: {[str(item) for item in self.lst_todas_as_equipes]} '


if __name__ == '__main__':
    ge = GerenciadorEquipe()
    
    aluno1  = Aluno( nome='Aluno1' , cpf = '111.111.111/11' )
    aluno2  = Aluno( nome='Aluno2' , cpf = '222.222.222/22' )
    aluno3  = Aluno( nome='Aluno3' , cpf = '333.333.333/33' )
    aluno4  = Aluno( nome='Aluno4' , cpf = '444.444.444/44' )

    equipe1 = Equipe( projeto = 'Teste_1', lista_de_participantes=[ aluno1                          ] )
    equipe2 = Equipe( projeto = 'Teste_2', lista_de_participantes=[ aluno2, aluno1,                 ] )
    equipe3 = Equipe( projeto = 'Teste_3', lista_de_participantes=[ aluno3, aluno2,  aluno1         ] )
    equipe4 = Equipe( projeto = 'Teste_4', lista_de_participantes=[ aluno4, aluno3,  aluno2, aluno1 ] )

    print(ge)
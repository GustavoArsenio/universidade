class Aluno():
    def __init__(self,**kwargs):
        self.nome = kwargs['nome']
        self.cpf  = kwargs['cpf']

    def __str__(self):
        return f' Aluno de Nome={self.nome}, CPF={self.cpf}'
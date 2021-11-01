import os
import json

class Gerenciador_clientes():
    def __init__(self,path_info):
        self.path_info     = path_info
        self.clientes_dict = {}
    
    def load_meta_dados(self):
        for path_cliente_file in os.listdir(self.path_info):
            __FILE    = open(os.path.join(self.path_info,path_cliente_file),'r+')
            __cliente = json.load(__FILE)
            if 'path' in __cliente:
                self.clientes_dict[__cliente['nome']] = Cliente(**__cliente)
            else:
                self.clientes_dict[__cliente['nome']] = Cliente(**__cliente,path=path_cliente_file)


    def add_cliente(self,cliente):
        CLIENTE_EXISTE = self.clientes_dict.get(cliente.nome,False)
        if CLIENTE_EXISTE is False:
            print(self.clientes_dict)
            path_new_client = cliente.path = f'{self.path_info}/{cliente.nome}.json'
            self.clientes_dict[cliente.nome] = cliente

            with open(cliente.path, 'w', encoding='utf-8') as f:
                json.dump(cliente.json_format(), f, ensure_ascii=False, indent=4)
        else:
            print('Usuario já cadastrado')

    def remove_cliente(self,nome_cliente):
        CLIETEN_EXISTE = self.clientes_dict.get(nome_cliente,False)
        if CLIETEN_EXISTE:
            os.remove(self.clientes_dict[nome_cliente].path)
            del       self.clientes_dict[nome_cliente]
        else:
            print('usuario Não existe')
        pass

    def update_cliente(self):
        pass

class Cliente():
    def __init__(self,nome,cpf,endereco,path=None):
        self.nome     = nome
        self.cpf      = cpf
        self.endereco = endereco
        self.path     = path
    
    def json_format(self):
        return { "nome":f"{self.nome}" , "cpf":f"{self.cpf}", "endereco":f"{self.endereco}", "path":f"{self.path}" }

    def __str__(self):
        return f' Nome: {self.nome} | CPF: {self.cpf} | Endereco: {self.endereco} | Path: {self.path}'

if __name__ == '__main__':
    gen = Gerenciador_clientes(path_info='/home/garsenio/projects/on_git/projetos_git/universidade/sistemas_distribuidos/Sockets/server/data')
    gen.load_meta_dados()

    TEST_CLIENT = Cliente(nome='Teste',cpf='111.111.111/11',endereco=' Rua teste ')

    gen.add_cliente(TEST_CLIENT)
    gen.remove_cliente('Teste')
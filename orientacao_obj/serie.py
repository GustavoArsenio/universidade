class Serie():
    def __init__(self, nome, categoria, data_lancamento,sinopse):
        self.nome = nome
        self.sinopse = sinopse
        self.categoria = categoria
        self.data_lancamento = data_lancamento
        self.__avaliacoes__ = [0]
        self.plataformas = []
    
    def add_avaliacao(self,nota):
        self.__avaliacoes__.append(nota)
    
    def get_avaliacao(self):
        return sum(self.__avaliacoes__) / len(self.__avaliacoes__)
    
    def add_plataformas(self,nome):
        self.plataformas.append(nome)
    
    def get_plataformas(self):
        return self.plataformas
    
    def __str__(self):
        return f"""
                    A serie {self.nome} foi lançada na data {self.data_lancamento} e possui atualmente nota {self.get_avaliacao()}.
                    Categoria {self.categoria}
                    Segue abaixo a sinopse: 
                        {self.sinopse}
                """

if __name__ == "__main__":
    serie1 = Serie('Mr Robot','Ficção cientifica','24/05/2015','Elliot (Rami Malek) é um jovem programador que trabalha como engenheiro de segurança virtual durante o dia, e como hacker vigilante durante a noite. Elliot se vê numa encruzilhada quando o líder (Christian Slater) de um misterioso grupo de hacker o recruta para destruir a firma que ele é pago para proteger.')
    print(serie1)
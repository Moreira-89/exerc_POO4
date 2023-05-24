class Arquivo:
    def __init__(self, nome, tipo, tamanho):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho

    def obter_tamanho(self):
        return self.tamanho

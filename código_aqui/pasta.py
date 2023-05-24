class Pasta:
    def __init__(self, nome):
        self.nome = nome
        self.subpastas = []
        self.arquivos = []

    def adicionar_subpasta(self, subpasta):
        self.subpastas.append(subpasta)

    def remover_subpasta(self, subpasta):
        self.subpastas.remove(subpasta)

    def adicionar_arquivo(self, arquivo):
        self.arquivos.append(arquivo)

    def remover_arquivo(self, arquivo):
        self.arquivos.remove(arquivo)

    def obter_tamanho_total(self):
        tamanho_total = 0
        for subpasta in self.subpastas:
            tamanho_total += subpasta.obter_tamanho_total()
        for arquivo in self.arquivos:
            tamanho_total += arquivo.obter_tamanho()
        return tamanho_total

    def excluir_recursivamente(self):
        for subpasta in self.subpastas:
            subpasta.excluir_recursivamente()
        for arquivo in self.arquivos:
            self.remover_arquivo(arquivo)

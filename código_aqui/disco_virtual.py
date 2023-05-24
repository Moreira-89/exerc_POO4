from pasta import Pasta


class DiscoVirtual:
    def __init__(self):
        self.pastas = []

    def criar_pasta(self, nome):
        pasta = Pasta(nome)
        self.pastas.append(pasta)

    def remover_pasta(self, pasta):
        self.pastas.remove(pasta)

    def obter_pasta(self, nome):
        for pasta in self.pastas:
            if pasta.nome == nome:
                return pasta
        return None

    def obter_tamanho_pasta(self, nome):
        pasta = self.obter_pasta(nome)
        if pasta:
            return pasta.obter_tamanho_total()
        return 0

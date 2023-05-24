__Nome__: Lucas M. A. Rodrigues

__Prof. Dr.__ Leandro Luque

## Prática 07: Orientado a Objeto

### O que temos que fazer? 
Projete, implemente o código e crie o diagrama de sequência para o seguinte cenário:
* Você foi convidado a implementar um disco virtual, como o GDrive. Nele, o usuário pode criar pastas (tem nome), subpastas e submeter arquivos (nome, tipo de arquivo, tamanho). Sua implementação deve ter métodos para calcular o tamanho total de uma pasta (somando subpastas e arquivos), bem como excluir arquivos e pastas (recursivamente - se excluir uma pasta, exclui todos os arquivos e subpastas).
* O diagrama de sequência pode ser criado para o cenário de criação das pastas, arquivos etc e da chamada do método de cálculo de tamanho de uma pasta.

***
### Minha Resolução 
__Classe arquivo.py__:
```
class Arquivo:
    def __init__(self, nome, tipo, tamanho):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho

    def obter_tamanho(self):
        return self.tamanho
```
__Classe pasta.py__:
```
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
```
__Classe disco_virtual.py__:
```
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
```
__Classe prog_principal.py__:
```
from arquivo import Arquivo
from disco_virtual import DiscoVirtual

# Criar uma instância do DiscoVirtual
disco_virtual = DiscoVirtual()

# Criar uma pasta chamada "Minha Pasta"
disco_virtual.criar_pasta("Minha Pasta")

# Obter a pasta "Minha Pasta"
pasta = disco_virtual.obter_pasta("Minha Pasta")

# Adicionar um arquivo na pasta
arquivo1 = Arquivo("Documento1", "txt", 100)
pasta.adicionar_arquivo(arquivo1)

# Calcular o tamanho total da pasta
tamanho_total = pasta.obter_tamanho_total()
print("Tamanho total da pasta:", tamanho_total)

# Remover o arquivo da pasta
pasta.remover_arquivo(arquivo1)

# Excluir a pasta e seus conteúdos
pasta.excluir_recursivamente()
```
***


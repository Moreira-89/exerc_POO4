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

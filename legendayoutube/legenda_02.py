import re

# Configuração
arquivo_entrada = 'legendas.txt'
arquivo_saida = 'legendas_com_links.txt'
link_base = 'https://youtu.be/pUG7_03G_Ac?t='

# Função para converter timestamp m:ss para segundos
def converter_para_segundos(timestamp):
    minutos, segundos = map(int, timestamp.split(':'))
    return minutos * 60 + segundos

# Lê o conteúdo do arquivo original
with open(arquivo_entrada, 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Processa cada linha, procurando timestamps
linhas_convertidas = []
padrao_timestamp = re.compile(r'^(\d{1,2}:\d{2})$')

for linha in linhas:
    linha = linha.rstrip('\n')
    match = padrao_timestamp.match(linha)
    if match:
        tempo = match.group(1)
        segundos = converter_para_segundos(tempo)
        nova_linha = f"[{tempo}]({link_base}{segundos})" #gerar 'mascara' de linkk \({tempo}\)
        linhas_convertidas.append(nova_linha)
    else:
        linhas_convertidas.append(linha)

# Grava o novo conteúdo em um arquivo separado
with open(arquivo_saida, 'w', encoding='utf-8') as file:
    for linha in linhas_convertidas:
        file.write(linha + '\n')

print(f"Timestamps convertidos e linkados. Arquivo salvo como '{arquivo_saida}'.")

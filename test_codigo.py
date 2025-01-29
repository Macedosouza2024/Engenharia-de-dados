import pandas as pd
import ssl
import os

# Para ignorar problemas com SSL, se necessário
ssl._create_default_https_context = ssl._create_unverified_context

# URL do arquivo HTML
url = 'https://www.in.gov.br/en/web/dou/-/portaria-gm/ms-n-3.493-de-10-de-abril-de-2024-553573811'

# Lista para armazenar as tabelas
tabelas_csv = []

try:
    # Lê todas as tabelas do HTML
    tabelas = pd.read_html(url, header=1)

    # Filtra a partir da quinta tabela (índice 5)
    tabelas_a_partir_da_quinta = tabelas[5:]

    # Verifica se há tabelas disponíveis
    if tabelas_a_partir_da_quinta:
        for i, tabela in enumerate(tabelas_a_partir_da_quinta, start=5):
            # Exibe a tabela
            print(f"Tabela {i}:")
            print(tabela)
            print("\n---\n")

            # Salva a tabela em um arquivo CSV
            nome_arquivo = f"tabela_{i}.csv"
            tabela.to_csv(nome_arquivo, index=False)
            tabelas_csv.append(nome_arquivo)
            print(f"Tabela {i} salva como {nome_arquivo}")

        # Junta todas as tabelas em um único arquivo CSV
        dataframes = [pd.read_csv(arquivo) for arquivo in tabelas_csv]
        tabela_unificada = pd.concat(dataframes, ignore_index=True)
        tabela_unificada.to_csv("tabelas_unificadas.csv", index=False)
        print("Todas as tabelas foram unificadas no arquivo 'tabelas_unificadas.csv'.")
    else:
        print("Não há tabelas disponíveis a partir do índice 5.")

except ValueError as e:
    print(f"Erro ao ler tabelas do HTML: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

indices = pd.read_csv('tabelas_unificadas.csv')
print(indices)

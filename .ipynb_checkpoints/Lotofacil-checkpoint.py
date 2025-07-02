import pandas as pd
import itertools
from tqdm import tqdm

# Caminho para o arquivo XLS da Lotofácil
CAMINHO_ARQUIVO = '/Users/viniciuslima/Downloads/loto_facil_asloterias_ate_concurso_3361_crescente.xls'  # Altere para o caminho correto

try:
    df = pd.read_excel(CAMINHO_ARQUIVO, skiprows=6)
    print("Arquivo carregado com sucesso!")
    print(df.head())
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho.")
except Exception as e:
    print(f"Outro erro ocorreu: {e}")

def carregar_resultados(caminho):
    # Lê o arquivo XLS, pulando as 6 primeiras linhas
    df = pd.read_excel(caminho, skiprows=6)

    # Nomes das colunas com as dezenas sorteadas
    colunas_dezenas = [f'bola {i}' for i in range(1, 16)]

    # Extrai os resultados como listas de inteiros ordenadas
    resultados = df[colunas_dezenas].dropna().astype(int).values.tolist()
    resultados_ordenados = {tuple(sorted(linha)) for linha in resultados}
    
    return resultados_ordenados

def gerar_combinacoes_nao_sorteadas(resultados_existentes):
    # Gera todas as combinações possíveis de 15 números entre 1 e 25
    todas_combinacoes = itertools.combinations(range(1, 26), 15)

    # Filtra as combinações que ainda não ocorreram
    nao_sorteadas = [comb for comb in tqdm(todas_combinacoes, total=3268760) if comb not in resultados_existentes]
    return nao_sorteadas

def main():
    print("Carregando resultados existentes...")
    resultados_existentes = carregar_resultados(CAMINHO_ARQUIVO)
    print(f"{len(resultados_existentes)} combinações já sorteadas.")

    print("Gerando combinações não sorteadas (isso pode demorar)...")
    combinacoes_nao_sorteadas = gerar_combinacoes_nao_sorteadas(resultados_existentes)

    print(f"{len(combinacoes_nao_sorteadas)} combinações nunca sorteadas.")
    
    # Salvar resultado como CSV
    pd.DataFrame(combinacoes_nao_sorteadas).to_csv('combinacoes_nao_sorteadas.csv', index=False)
    print("Arquivo 'combinacoes_nao_sorteadas.csv' salvo com sucesso.")

if __name__ == '__main__':
    main()
import threading as th
import pandas as pd
from time import time
import os

lista_pastas = ["\\Justiça Estadual", "\\Justiça do Trabalho", "\\Justiça Federal", "\\Justiça Militar Estadual", "\\Tribunal Superior Eleitoral"]
threads = []
BaseDados = {}
Lock = th.Lock()

def read_csv(nome_pasta):
    PastaAtual = os.path.dirname(os.path.abspath(__file__))
    local = PastaAtual + nome_pasta
    lista_csv = [f for f in os.listdir(local) if f.endswith('.csv')]
        
    df_concat = pd.DataFrame()
    
#with Lock:
    for arquivo in lista_csv:
        df = pd.read_csv(os.path.join(local, arquivo))
        df_concat = pd.concat([df_concat, df], ignore_index=True)
        
    BaseDados[nome_pasta] = df_concat # -> Gera um dicionario onde: a chave é a pasta para os arquivos e o valor é um dataframe com a concatenacao dos dfs daquela pasta

t0 = time()
for nome_pasta in lista_pastas:
    thread = th.Thread(target=lambda: read_csv(nome_pasta))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

t1 = time()

#print(BaseDados['\\Justiça Federal'])
print("Tempo paralelo: ", t1 - t0)

# ------------------------------------------------------------------ Fórmulas

def meta1(dados):
    cnm1 = dados['casos_novos_2025'].sum()
    julgadom1  = dados['julgados_2025'].sum()
    desm1 = dados['dessobrestados_2025'].sum()
    susm1 = dados['suspensos_2025'].sum()

    meta1 = (julgadom1 / ((cnm1 + desm1) - susm1)) * 100
    print(meta1)
    
meta1(BaseDados['\\Justiça Estadual']) # -> Para executar cada meta então, basta informar o dict com a chave que corresponde ao orgão ao qual a meta deve ser aplicada

# -------------------------------------------------------- Gerar Compilado.csv      

def concat_arquivos():
    PastaAtual = os.path.dirname(os.path.abspath(__file__))
    lista_csv = [f for f in os.listdir(PastaAtual) if f.endswith('.csv')]

    print(lista_csv)
    BaseDados = pd.DataFrame()

    for arquivo in lista_csv:
        df = pd.read_csv(os.path.join(PastaAtual, arquivo))
        
        BaseDados = pd.concat([BaseDados, df], ignore_index=True)

    #BaseDados.to_csv('Compilado.csv', index=False, encoding='utf-8') -> Descomentar depois (pra não ficar criando esse arquivo toda hora)
    return BaseDados
    
# dados = concat_arquivos()
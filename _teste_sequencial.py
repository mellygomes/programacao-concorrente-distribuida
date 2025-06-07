import pandas as pd
import os
from time import time 

lista_pastas = ["\\Justiça Estadual", "\\Justiça do Trabalho", "\\Justiça Federal", "\\Justiça Militar Estadual", "\\Tribunal Superior Eleitoral"]
BaseDados = {}

def read_csv(nome_pasta):
    PastaAtual = os.path.dirname(os.path.abspath(__file__))
    local = PastaAtual + nome_pasta
    lista_csv = [f for f in os.listdir(local) if f.endswith('.csv')]
        
    df_concat = pd.DataFrame()
    
    for arquivo in lista_csv:
        df = pd.read_csv(os.path.join(local, arquivo))
        df_concat = pd.concat([df_concat, df], ignore_index=True)
        
    BaseDados[nome_pasta] = df_concat
    
    
t0 = time()
for nome_pasta in lista_pastas:
    read_csv(nome_pasta=nome_pasta)

t1 = time()    

print(BaseDados['\\Justiça Federal'])
print("Tempo sequencial: ", t1 - t0)
import pandas as pd
import os

def concat_arquivos():
    PastaAtual = os.path.dirname(os.path.abspath(__file__))
    lista_csv = [f for f in os.listdir(PastaAtual) if f.endswith('.csv')]

    print(lista_csv)
    BaseDados = pd.DataFrame()

    for arquivo in lista_csv:
        df = pd.read_csv(os.path.join(PastaAtual, arquivo))
        
        BaseDados = pd.concat([BaseDados, df], ignore_index=True)

    #BaseDados.to_csv('Compilado.csv', index=False, encoding='utf-8')
    return BaseDados
    
dados = concat_arquivos()

def meta1(dados):
    cnm1 = dados['casos_novos_2025'].sum() #A soma funcionou.
    julgadom1  = dados['julgados_2025'].sum()
    desm1 = dados['dessobrestados_2025'].sum()
    susm1 = dados['suspensos_2025'].sum()

    meta1 = (julgadom1 / ((cnm1 + desm1) - susm1)) * 100
    print(meta1)
    
meta1(dados)

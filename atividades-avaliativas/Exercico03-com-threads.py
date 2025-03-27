from PIL import Image
from tkinter import Tk, filedialog
from time import time
import threading as th

def converter_para_preto_e_branco_manual_paralelizada():
    try:
        root = Tk()
        root.withdraw()
        threads = []

        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")  # Garante que a imagem esteja no modo RGB
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        # Itera sobre cada pixel da imagem
        for x in range(largura):
            thread = th.Thread(target=lambda: processar_coluna(x, imagem, imagem_preto_branco, altura))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        # Salva a imagem em preto e branco no caminho especificado
        imagem_preto_branco.save(caminho_saida)
        print(f"\nImagem convertida com sucesso! Salva em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

def processar_coluna(x, imagem, imagem_preto_branco, altura):
    for y in range(altura):
        r, g, b = imagem.getpixel((x, y))
        luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
        imagem_preto_branco.putpixel((x, y), luminancia)

def converter_para_preto_e_branco_manual():
    try:
        root = Tk()
        root.withdraw()

        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")  # Garante que a imagem esteja no modo RGB
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        # Itera sobre cada pixel da imagem
        for x in range(largura):
            for y in range(altura):
                r, g, b = imagem.getpixel((x, y))
                luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
                imagem_preto_branco.putpixel((x, y), luminancia)

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        # Salva a imagem em preto e branco no caminho especificado
        imagem_preto_branco.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de uso
if __name__ == "__main__":
    print("\nRealizando conversão de forma paralelo...")

    inicio_p = time()
    converter_para_preto_e_branco_manual_paralelizada()
    fim_p = time()
    t_execucao_paralela = fim_p - inicio_p

    print("\nRealizando conversão de forma sequencial...\n")

    inicio = time()
    converter_para_preto_e_branco_manual()
    fim = time()
    t_execucao_sequencial = fim - inicio
    
    print(f"\nTempo de execução paralela: {t_execucao_paralela:.4f}")
    print(f"Tempo de execução sequencial: {t_execucao_sequencial:.4f}\n")

    print("Resultado do teste: ")
    if t_execucao_paralela < t_execucao_sequencial:
        print(f"A execução paralela foi {(t_execucao_sequencial - t_execucao_paralela):.4f} segundos mais rápida.\n")
    else:
        print(f"A execução sequencial foi {(t_execucao_paralela - t_execucao_sequencial):.4f} segundos mais rápida.\n")

# Resultado do teste:
# A maioria dos testes mostrou que a execução sequencial do algoritmo foi mais rápida que a versão paralelizada.
# Esse resultado pode ser um indicador de que nem sempre a implementação de threads resulta num melhor desempenho.
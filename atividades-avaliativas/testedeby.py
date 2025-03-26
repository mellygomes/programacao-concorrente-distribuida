import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import threading

class BuscaThread(threading.Thread):
    def __init__(self, url, palavra, url_inicial, profundidade_maxima, urls_visitados, resultados, lock):
        super().__init__()
        self.url = url
        self.palavra = palavra
        self.url_inicial = url_inicial
        self.profundidade_maxima = profundidade_maxima
        self.urls_visitados = urls_visitados
        self.resultados = resultados
        self.lock = lock

    def run(self):
        self.buscar_recursivo(self.url, 1)

    def buscar_recursivo(self, url_atual, profundidade_atual):
        if profundidade_atual > self.profundidade_maxima:
            return

        with self.lock:
            if url_atual in self.urls_visitados:
                return
            self.urls_visitados.add(url_atual)

        try:
            print(f"Buscando em: {url_atual} (Profundidade: {profundidade_atual})")
            response = requests.get(url_atual, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            conteudo = soup.get_text().lower()
            palavra_encontrada = self.palavra.lower() in conteudo

            with self.lock:
                self.resultados[url_atual] = palavra_encontrada

            links = soup.find_all('a', href=True)
            threads = []

            for link in links:
                url_completa = urljoin(self.url_inicial, link['href'])
                if url_completa.startswith(self.url_inicial):
                    nova_thread = BuscaThread(
                        url_completa, self.palavra, self.url_inicial,
                        self.profundidade_maxima, self.urls_visitados,
                        self.resultados, self.lock
                    )
                    nova_thread.start()
                    threads.append(nova_thread)

            for t in threads:
                t.join()

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url_atual}: {e}")

def buscar_palavra_no_site(url_inicial, palavra, profundidade_maxima=3):
    urls_visitados = set()
    resultados = {}
    lock = threading.Lock()

    thread_principal = BuscaThread(url_inicial, palavra, url_inicial, profundidade_maxima, urls_visitados, resultados, lock)
    thread_principal.start()
    thread_principal.join()

    return resultados

if __name__ == "__main__":
    url_inicial = input("Digite a URL inicial do site (ex.: https://www.exemplo.com): ")
    palavra = input("Digite a palavra a ser buscada: ")

    resultados = buscar_palavra_no_site(url_inicial, palavra)

    print("\nResultados da busca:")
    for url, encontrada in resultados.items():
        status = "Encontrada" if encontrada else "Não encontrada"
        print(f"{url}: Palavra '{palavra}' {status}")

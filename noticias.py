import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time
import json 

# URL do site alvo
url = 'https://globoesporte.globo.com/futebol/times/flamengo/'


pagina_html = ""

with webdriver.Chrome() as navegador:
    
    navegador.get(url)
    
    try:
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "feed-post-link"))
        )
    except Exception as e:
        print(f"Erro ao carregar a página inicial: {e}")
        pass

    print('Iniciando rolagem para carregar todas as notícias...')
    
    ultima_pagina = navegador.execute_script("return document.body.scrollHeight")
    
    while True:
        navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(3) 
        
        nova_pagina = navegador.execute_script("return document.body.scrollHeight")
        
        if nova_pagina == ultima_pagina:
            print('Fim do carregamento dinâmico.')
            break
            
        ultima_pagina = nova_pagina

    pagina_html = navegador.page_source

pagina = BeautifulSoup(pagina_html, 'html.parser')

lista_noticias = pagina.find_all("a", class_="feed-post-link")
print(f"\n--- Resultado Final ---\nTotal de notícias encontradas: {len(lista_noticias)}")

dados_estruturados = []

for noticia in lista_noticias:

    dados_estruturados.append({
        "titulo": noticia.text.strip(), 
        "link": noticia.get("href")
    })
    
    print(noticia.text)
    print(noticia.get("href"))
    print("#############")

nome_arquivo = 'noticias_flamengo.json'

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(
            dados_estruturados, 
            arquivo, 
            ensure_ascii=False, 
            indent=4            
        )
    print(f"\nSucesso: {len(dados_estruturados)} notícias salvas em '{nome_arquivo}'")

except IOError as e:
    print(f"Erro ao salvar o arquivo JSON: {e}")

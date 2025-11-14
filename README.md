# ⚽ **FLAMENGO SCRAPER – Notícias Dinâmicas do GE** 🔴⚫  
Web scraping com rolagem infinita utilizando Selenium + BeautifulSoup

---

## 📌 **Sobre o Projeto**

Este projeto é um **Web Scraper avançado em Python** capaz de coletar **todas as últimas notícias do Flamengo** diretamente da página oficial do **GE (Globo Esporte)**.

Ele utiliza **automação real do navegador**, simulando o comportamento humano (scroll infinito). Isso permite captar notícias que **não aparecem usando requisições HTTP simples**.

---

## ✨ **Destaques Técnicos**

| Feature | Descrição | Habilidade Demonstrada |
|--------|-----------|------------------------|
| **Scroll Dinâmico** | Simula rolagem contínua até o carregamento completo das notícias. | Automação com Selenium |
| **Gerenciamento de Driver** | Selenium Manager baixa automaticamente o driver correto do Chrome. | Configuração simples e portátil |
| **Análise e Extração** | BeautifulSoup parseia todo o HTML para extrair títulos e links. | Web Scraping eficiente |
| **Persistência de Dados** | Exporta os dados em `noticias_flamengo.json` com formatação organizada. | Manipulação de JSON |

---

## 🛠️ **Tecnologias Utilizadas**

| Tecnologia | Função | Ícone |
|------------|--------|-------|
| **Python 3** | Linguagem principal | 🐍 |
| **Selenium** | Automação do navegador | 🌐 |
| **BeautifulSoup 4** | Parsing e extração de HTML | 🥣 |
| **JSON** | Formato de saída dos dados | 📜 |

---

## ⚙️ **Como Executar o Projeto**

### 📌 **Pré-requisitos**
- Python 3.x instalado  
- Google Chrome instalado  
- Selenium fará o download automático do driver correto ✔️

---

### 1️⃣ **Clonar o Repositório**

```bash
git clone https://github.com/CarlosEduardo-J/noticias-futebol.git
cd noticias-futebol
```

### 2️⃣ **Instalar Dependências**

```bash
pip install selenium beautifulsoup4
```

### 3️⃣ Executar o Script

```bash
python noticias.py
```

## 📁 Estrutura do Projeto
noticias
│── noticias.py
│── noticias_flamengo.json   (gerado após a execução)
│── README.md

## 📂 Saída do Projeto

Após a execução, será criado o arquivo:

noticias_flamengo.json

Formato dos dados:
```json
[
  {
    "titulo": "Título da notícia após limpeza",
    "link": "https://ge.globo.com/link-da-noticia"
  }
]
```

## ⚠️ Aviso Legal

Este projeto foi criado exclusivamente para fins educacionais.
Todo o conteúdo raspado pertence ao Globo Esporte (GE).
Respeite os Termos de Uso, a política de privacidade e o robots.txt do site.
O autor não se responsabiliza por usos indevidos do código.
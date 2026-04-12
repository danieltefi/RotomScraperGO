import requests
from bs4 import BeautifulSoup
from pokemonevent import PokemonEvent

class RotomScraper: # motor de extração (encapsulado)

    def __init__(self):
        self.url = 'https://www.leekduck.com/events/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' # User-Agent acessa a pagina como se fosse um humano utilizando o Mozilla
        }

    def fetch_page(self): # baixa o conteúdo HTML da página
        try: # trata erros
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status() # verifica se o download foi bem-sucedido
            return response.text
        except requests.exceptions.RequestException as e:
            print(f'Erro ao acessar o Leek Duck: {e}')
            return None

    def extrair_eventos(self):
        html = self.fetch_page() # analisa o HTML e retorna uma lista de objetos PokemonEvent
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser') # analisa o HTML
        lista_eventos = []

        cards = soup.select('.event-card-item') # Leek Duck organiza eventos em cards, select() para encontrar os seletores CSS

        for card in cards:
            try:
                nome = card.select_one('.event-text h2').text # extração dos dados usando seletores do site
                data = card.select_one('.event-text p').text
                
                if 'live' in card.get('class', []): # live/upcoming geralmente é uma classe CSS ou etiqueta
                    status = 'Ativo'
                else:
                    status = 'Futuro'
                
                categoria = card.get('data-category', 'Geral')
                
                img_tag = card.select_one('.event-img img') # captura do link da imagem
                link_img = img_tag['src'] if img_tag else ''

                evento = PokemonEvent(nome, data, status, categoria, link_img) # cria o objeto da classe PokemonEvent
                lista_eventos.append(evento)
                
            except AttributeError:
                continue # pula cards que não tenham a estrutura esperada

        return lista_eventos
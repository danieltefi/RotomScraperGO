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

        cards = soup.select('span.event-header-item-wrapper') # Leek Duck organiza eventos em wrappers de header, select() para encontrar os seletores CSS

        for card in cards:
            try:
                nome = card.select_one('h2').text # extração dos dados usando seletores do site
                
                data_raw = card.get('data-event-date-sort', '') # captura data para maior precisão
                if data_raw: # verifica se o site entregou a informação de data
                    data_sem_hora = data_raw.split('T')[0] # .split('T')[0] retira a hora final, [ano-mês-dia]
                    partes = data_sem_hora.split('-') # split('-'): quebra a data onde tem traço ['ano', 'mês', 'dia']
                    data = f"{partes[2]}/{partes[1]}/{partes[0]}" # transforma ano, mês, dia em dia/mês/ano
                else:
                    data = 'Data Indisponível'
                
                if card.find_parent('div', class_='events-section-live'): # verifica se o card está dentro da seção de eventos ativos (happening now)
                    status = 'Ativo'
                else:
                    status = 'Futuro'
                
                categoria_tag = card.select_one('.event-item-wrapper p') # categoria fica no texto do parágrafo do wrapper
                if categoria_tag:
                    categoria = categoria_tag.text
                else:
                    categoria = 'Geral'
                
                img_tag = card.select_one('.event-img-wrapper img') # captura do link da imagem
                if img_tag:
                    link_img = img_tag['src']
                else:
                    link_img = ''

                evento = PokemonEvent(nome, data, status, categoria, link_img) # cria o objeto da classe PokemonEvent
                lista_eventos.append(evento)
                
            except AttributeError:
                continue # pula cards que não tenham a estrutura esperada

        return lista_eventos
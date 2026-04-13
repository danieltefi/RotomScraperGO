import requests
from bs4 import BeautifulSoup
from pokemonevent import PokemonEvent
from datetime import datetime

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
        lista_eventos = [] # guarda todos os eventos encotrados
        nomes_processados = set() # guarda os nomes dos eventos já processados para evitar duplicados no JSON
        
        hoje = datetime.now() # variáveis para os filtros automáticos de mês e status, guarda a data do dia
        mes_atual = hoje.strftime('-%m-') # guarda o mês atual, para filtrar eventos apenas do mês
        data_hoje_comparacao = hoje.strftime('%Y-%m-%d') # formata para o padrao internacional para comparar futuramente se é ativo ou futuro

        cards = soup.select('span.event-header-item-wrapper') # Leek Duck organiza eventos em wrappers de header, select() para encontrar os seletores CSS

        for card in cards:
            try:
                nome = card.select_one('h2').text # extração dos dados usando seletores do site
                
                if nome in nomes_processados: # verifica se o evento já foi adicionado para evitar repetições
                    continue
                
                data_raw = card.get('data-event-date-sort', '') # captura data para maior precisão
                
                if mes_atual not in data_raw: # filtro temporal: pula eventos que não sejam do mês atual
                    continue
                
                if data_raw: # verifica se o site entregou a informação de data
                    data_iso = data_raw.split('T')[0] # formato para comparação [ano-mês-dia]
                    partes = data_iso.split('-') # split('-'): quebra a data onde tem traço ['ano', 'mês', 'dia']
                    data = f"{partes[2]}/{partes[1]}/{partes[0]}" # transforma ano, mês, dia em dia/mês/ano
                    
                    if data_iso <= data_hoje_comparacao: # refinamento do status, compara a data do evento com a data do dia
                        status = 'Ativo' # adiciona eventos como ativo se a data for = ou < que a do dia (menor pq um evento pode ter começado antes e ainda nao finalizou, por isso esta como ativo)
                    else:
                        status = 'Futuro' # adciona eventos como futuro se a data for > que a do dia
                else:
                    data = 'Data Indisponível'
                    status = 'Futuro' # se o evento n tiver data, adiciona em futuro
                
                categoria_tag = card.select_one('.event-item-wrapper p') # categoria fica no texto do parágrafo do wrapper
                if categoria_tag:
                    categoria = categoria_tag.text # captura a categoria e a guarda
                else:
                    categoria = 'Geral' # se erro ou categoria indefinida -> geral
                
                img_tag = card.select_one('.event-img-wrapper img') # captura do link da imagem
                if img_tag:
                    link_img = img_tag['src'] # link da imagem
                else:
                    link_img = '' # sem imagem

                evento = PokemonEvent(nome, data, status, categoria, link_img) # cria o objeto (evento) da classe PokemonEvent
                lista_eventos.append(evento) # adiciona o evento na lista final que será salva no JSON
                nomes_processados.add(nome) # registra que o evento já foi processado para evitar duplicatas
                
            except AttributeError:
                continue # pula cards que não tenham a estrutura esperada

        return lista_eventos
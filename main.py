import json
from datetime import datetime
from rotomscraper import RotomScraper

def main():
    print('Iniciando RotomScraper GO...')
    
    scraper = RotomScraper() # instancia o motor de extração
    
    print('Acessando Leek Duck...') # realiza a raspagem (processamento de conteúdo)
    eventos_objetos = scraper.extrair_eventos()
    
    if not eventos_objetos: # verifica se a lista não está vazia para evitar erros na execução
        print('Nenhum evento encontrado ou erro na conexão.')
        return

    ocorrendo_agora = [] # separa os eventos por status para organizar a estrutura do JSON
    em_breve = []

    for evento in eventos_objetos:
        if evento.status == 'Ativo':
            ocorrendo_agora.append(evento.to_dict()) # to_dict() aplica a abstração definida no pokemonevent.py
        else:
            em_breve.append(evento.to_dict())

    dados_finais = { # organiza os dados para o JSON
        'titulo': 'Eventos do mês atual no Pokémon GO:', # título informativo para o início do arquivo
        'ultima_atualizacao': datetime.now().strftime('%d/%m/%Y %H:%M:%S'), # captura dia, mês, ano hora, minutos, segundos para guardar quando foi feito o arquivo e substituir por um novo na próx
        'total_eventos': len(eventos_objetos),
        'secoes': { # divide os eventos em blocos específicos
            'ocorrendo_agora': ocorrendo_agora,
            'em_breve': em_breve
        }
    }

    try:
        with open('eventos_pokemon.json', 'w', encoding='utf-8') as f: # 'w' abre o arquivo para escrita, se já existir, apaga todo o conteúdo e escreve novamente, encoding='utf-8' para manter a codificação unicode, garantindo que tenha a escrita correta
            json.dump(dados_finais, f, indent=4, ensure_ascii=False) # salva o arquivo criado, ensure_ascii=False evita que o arquivo corrompa os acentos e nomes
                                                                    # indent=4 adiciona 4 espaços de recuo em cada nível, criando estrutura em "escada"        
        print(f'Sucesso! {len(eventos_objetos)} eventos salvos em eventos_pokemon.json')
    
    except Exception as e: # trata erro caso ocorra falha na escrita do arquivo e guarda na variável 'e'
        print(f'Erro ao salvar o arquivo: {e}')

if __name__ == '__main__': # garante que o script só rode se executado diretamente
    main()
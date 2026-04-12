class PokemonEvent: # representa um evento de Pokémon GO extraído da web

    def __init__(self, nome, data_exibicao, status, categoria, link_imagem): # aplica o conceito de abstração ao focar apenas nos dados essenciais
        self.nome = nome.strip() # .strip() retira espaços/quebra de linhas (dados sujos do HTML)
        self.data_exibicao = data_exibicao.strip()
        self.status = status.strip()
        self.categoria = categoria.strip()
        self.link_imagem = link_imagem.strip()

    def to_dict(self): # converte o objeto em um dicionário, preparando para a construção do JSON
        return {
            'nome': self.nome,
            'data_exibicao': self.data_exibicao,
            'status': self.status,
            'categoria': self.categoria,
            'link_imagem': self.link_imagem
        }

    def __str__(self): # define como o objeto será exibido ao usar print()
        return f'[{self.status}] {self.nome} - {self.data_exibicao}'
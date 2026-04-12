# ⚡ RotomScraper GO - Checklist de Desenvolvimento

Detalha as etapas de construção do scraper automatizado para eventos de Pokémon GO, focado em extração limpa, estruturação por orientação a objetos e armazenamento em JSON.

## 🟢 1. Configuração e Arquitetura POO
- [x] Inicializar o repositório Git e configurar `.gitignore`.
- [x] Criar ambiente virtual Python (`venv`) 
- [x] Instalar dependências
- [x] **Arquitetura:** Planejar a classe `PokemonEvent` (modelo de dados).
- [x] **Arquitetura:** Planejar a classe `RotomScraper` (motor de extração).

## 🔵 2. Desenvolvimento do Modelo (Classe PokemonEvent)
- [x] Definir atributos: `nome`, `data_exibicao`, `status` (Live/Upcoming), `categoria` e `link_imagem`.
- [x] Implementar método `to_dict()` para serialização (preparação para o JSON).
- [x] Implementar lógica interna para limpar espaços vazios (`.strip()`) nos atributos.

## 🟡 3. Motor de Captura (Classe RotomScraper)
- [x] Criar método para gerenciar conexão com `User-Agent` (evitar bloqueio do site).
- [x] Implementar loop de extração que instancie um objeto `PokemonEvent` para cada card encontrado.
- [x] **Filtro de Status:** Lógica para identificar se o evento está "Ativo Agora" via CSS.
- [x] **Filtro Temporal:** Lógica para capturar apenas eventos que ocorrem no mês atual.
- [x] Implementar tratamento de exceções (`try/except`) para campos ausentes ou erros de conexão.

## 🟠 4. Persistência e Inteligência JSON
- [ ] Integrar a biblioteca `datetime` para registrar a data da extração no arquivo.
- [ ] Implementar o método `save_to_json()` que salve a lista de objetos de forma organizada.
- [ ] Configurar `indent=4` e `ensure_ascii=False` (para garantir acentos corretos em Português).
- [ ] Garantir que o script sobrescreva o JSON anterior para manter os dados sempre atuais.

## 🔴 5. Finalização e Documentação
- [x] Criar `README.md` com o conceito do projeto (O Rotom como assistente de dados).
- [x] Adicionar instruções de instalação e execução no README.
- [ ] Comentar as funções do código explicando a lógica.
- [ ] Realizar o commit final e push para o GitHub.

---
*Status Atual: 🚀 Em desenvolvimento.*
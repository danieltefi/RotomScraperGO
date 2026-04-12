# RotomScraperGO
> **Monitor Inteligente Eventos Pokémon GO**

## ⚡ Sobre o Projeto

O nome do projeto é inspirado no Pokémon **Rotom**, uma criatura do tipo Elétrico/Fantasma conhecida por sua capacidade única de possuir e controlar aparelhos eletrônicos. No universo Pokémon, o Rotom não apenas habita máquinas, mas as otimiza, transformando-se em ferramentas essenciais como o **Rotom Phone** e a **Rotom Dex** para processar e organizar informações para os treinadores.

### 🔌 A Analogia
Assim como o Pokémon "entra" nos dispositivos para torná-los inteligentes, o **RotomScraper GO** atua como esse espírito digital dentro da web. Ele "consulta" um site de eventos de Pokémon GO para:

* **Infiltrar:** Acessar a estrutura de dados de sites especializados.
* **Processar:** Transformar códigos HTML brutos em informações úteis.
* **Assistir:** Entregar ao usuário final uma agenda clara e organizada dos eventos do mês.

> Em suma, o projeto personifica a natureza do Rotom: uma utilidade digital ágil que converte tecnologia complexa em auxílio prático para a jornada de todo treinador.

## 🛠️ Tecnologias
- **Linguagem:** Python 3
- **Bibliotecas:** BeautifulSoup4, Requests
- **Arquitetura:** Orientação a Objetos (POO)
- **Saída:** JSON estruturado

## ⚙️ Configuração do ambiente
O projeto utiliza **ambiente virtual (venv)** para isolamento de dependências.

### Instalação:
1. **Ative o ambiente:**
   - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - Windows (CMD): `.\venv\Scripts\activate.bat`
   - Linux/macOS: `source venv/bin/activate`
2. **Dependências:** `pip install -r requirements.txt`

### Execução:
- Com o venv ativo: `python main.py`

## 📂 Estrutura de Arquivos

```text
RotomScraperGO/
├── .gitignore           # Define arquivos que o Git deve ignorar
├── CHECKLIST.md         # Acompanhamento do progresso do projeto
├── LICENSE              # Termos de uso e licença do código
├── main.py              # Ponto de entrada e execução
├── pokemonevent.py      # Modelo de dados (Classe PokemonEvent)
├── README.md            # Documentação do projeto
├── requirements.txt     # Lista de dependências (bibliotecas)
└── rotomscraper.py      # Motor de extração e lógica de scraping

---

### 🚧 Status do Projeto: 
*Em desenvolvimento*
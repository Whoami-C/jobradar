# JobRadar

Monitor automatizado de vagas para Dados, BI e tecnologia. O JobRadar consulta fontes de emprego, aplica filtros por cargo, localização, senioridade e idioma, calcula uma pontuação de relevância e envia alertas pelo Telegram.

## O que ele faz

- Consulta múltiplas fontes de vagas em ciclos automatizados
- Filtra cargos e palavras-chave com níveis de confiança
- Remove vagas duplicadas por link e empresa/título
- Calcula score de relevância sem depender de machine learning
- Envia alertas imediatos e resumos diários pelo Telegram
- Armazena histórico e metadados em SQLite
- Executa testes automaticamente pelo GitHub Actions

## Stack

Python, Playwright, SQLite, requests, python-dotenv, Pytest, Telegram Bot API e GitHub Actions.

## Requisitos

- Python 3.11 ou superior
- Git
- Uma conta ou bot do Telegram para receber notificações

## Instalação

```bash
git clone https://github.com/Whoami-C/jobradar.git
cd jobradar
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

Instale as dependências e o navegador do Playwright:

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

Crie um arquivo `.env` na raiz:

```env
TELEGRAM_BOT_TOKEN=seu_token
TELEGRAM_CHAT_ID=seu_chat_id
```

## Execução

Execute uma busca única:

```bash
python main.py --once
```

Para manter o monitor ativo:

```bash
python main.py
```

No Windows, o arquivo `iniciar_jobradar.bat` também pode ser executado com dois cliques.

## Testes

```bash
pytest tests/ -v
```

O histórico local, bancos de dados, logs, ambientes virtuais e credenciais não fazem parte do repositório.

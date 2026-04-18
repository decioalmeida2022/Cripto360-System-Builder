# Cripto360 System Builder Agent Skill 🚀

[🇺🇸 English Version Below]

## 🇧🇷 Português

### Visão Geral
Esta é uma **Skill para Agentes de IA** (Antigravity, Claude Code, Cursor) desenhada para automatizar a criação e validação de robôs de trading profissionais na Binance. Ela utiliza a arquitetura comprovada do **Cripto360 Binance v2**, focando em segurança operacional, gerenciamento de risco rigoroso e dados 100% reais.

### Principais Benefícios
- **Arquitetura Escalável:** Gera projetos modulares (`src/risk`, `src/trading`, `src/connection`).
- **Segurança Nativa:** Bloqueia ordens inválidas ou fora dos limites de risco da conta.
- **Rastreabilidade:** Logs detalhados de cada decisão tomada pelo bot.
- **Dashboard Live:** Template pronto para monitoramento via FastAPI.

### Como Instalar
Para usar esta skill no seu assistente Antigravity ou Claude Code:

1. Clone este repositório.
2. Copie o arquivo `SKILL.md` para a sua pasta de skills local ou global:
   ```bash
   # Exemplo (Global)
   cp SKILL.md ~/.gemini/antigravity/skills/cripto360-system-builder/SKILL.md
   ```

### Como Usar
Após instalada, basta pedir ao seu agente:
> *"Crie um novo bot de trading seguindo o padrão Cripto360 para o par BTC/USDT."*

---

## 🇺🇸 English

### Overview
This is an **AI Agent Skill** (Antigravity, Claude Code, Cursor) designed to automate the creation and validation of professional Binance trading bots. It leverages the proven **Cripto360 Binance v2** architecture, focusing on operational security, rigorous risk management, and 100% real-time data.

### Key Benefits
- **Scalable Architecture:** Generates modular projects (`src/risk`, `src/trading`, `src/connection`).
- **Native Security:** Blocks invalid orders or those exceeding account risk limits.
- **Traceability:** Detailed logs for every decision made by the bot.
- **Live Dashboard:** Ready-to-use template for real-time monitoring via FastAPI.

### Installation
To use this skill with your Antigravity or Claude Code assistant:

1. Clone this repository.
2. Copy the `SKILL.md` file to your local or global skills folder:
   ```bash
   # Example (Global)
   cp SKILL.md ~/.gemini/antigravity/skills/cripto360-system-builder/SKILL.md
   ```

### Usage
Once installed, simply ask your agent:
> *"Create a new trading bot following the Cripto360 pattern for the BTC/USDT pair."*

---

## 📂 Project Structure (Blueprint)
The skill ensures every new bot follows this professional structure:
- `main.py`: Main orchestrator.
- `src/connection`: Exchange client (CCXT).
- `src/trading`: Position management & precision.
- `src/risk`: Mandatory risk validation layer.
- `app_fastapi.py`: Real-time monitoring dashboard.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

© 2026 Décio Almeida & Cripto360.

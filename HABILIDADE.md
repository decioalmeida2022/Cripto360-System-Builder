---
name: cripto360-system-builder
description: Guia especializado e automação para criar novos sistemas de trading baseados na arquitetura Cripto360 (Binance v2), com foco em segurança real e rastreabilidade.
category: development
risk: low
tags: [trading, binance, bot, architecture, crypto, cripto360]
tools: [claude, cursor, windsurf, codex-cli]
date_added: "2026-04-18"
author: decio
compatibility: claude-code
---

# Cripto360 System Builder

## Overview

Esta skill automatiza a criação de novos robôs de trading que seguem os padrões de excelência do **Cripto360 Binance v2**. Ela garante que a arquitetura seja modular, segura e baseada 100% em dados reais da exchange, evitando dashboards com dados simulados e garantindo a correta execução de ordens.

## When to Use This Skill

- Use quando o usuário pedir para "criar um novo bot", "scaffold trading system" ou "seguir padrão Cripto360".
- Use para validar se um sistema existente segue as regras de segurança operacional e risco.
- Use para migrar lógicas de trading simples para uma estrutura robusta de produção.

## How It Works

O assistente analisa o pedido do usuário e aplica o blueprint de diretórios e princípios obrigatórios. Ele deve priorizar a integração com a API real da Binance (via CCXT) e nunca realizar ordens sem passar pela camada de `src/risk`.

## Examples

### Example 1: Iniciando um novo projeto
**User:** "Quero criar um novo bot de trading para Spot na Binance usando o padrão Cripto360."
**Assistant:** "Entendido. Vou gerar a estrutura de diretórios (`src/`, `config/`, `deploy/`) e os arquivos base seguindo o blueprint do Cripto360 System Builder para garantir segurança e rastreabilidade..."

### Example 2: Verificando regras de risco
**User:** "Verifique se meu bot está seguindo o padrão de segurança do Cripto360."
**Assistant:** "Vou auditar o código. Primeiramente, estou verificando os princípios obrigatórios: Fonte de verdade da API, Sizing baseado em Equity real e validação de Precision antes das ordens..."

## Princípios Obrigatórios

1.  **Fonte de verdade:** Usar sempre a Binance API real para status de carteira, ordens e posições.
2.  **Segurança operacional:** Toda entrada deve passar pela camada de risco + restrições técnicas da exchange.
3.  **Transparência:** Todo bloqueio ou decisão de "não entrada" deve gerar um log explícito com a causa.
4.  **Configurabilidade:** Parâmetros e thresholds devem estar em `config/config.json`, nunca hardcoded.
5.  **Composição de capital:** Cálculo de sizing sempre baseado no capital/equity atual consultado via API.

## Blueprint Mínimo de Projeto

Para manter a compatibilidade com o ecossistema Cripto360, o projeto deve seguir esta estrutura:

- `main.py`: Orquestrador principal (loops, execução, social, risco).
- `src/connection`: Cliente da exchange (CCXT wrapper e health checks).
- `src/trading`: Lógica de abertura/fechamento, trailing stop, e gestão de precisão/lote.
- `src/risk`: Camada mandatória de validação de exposição, drawdown e limite diário.
- `src/social`: Conectores externos para sinais de consenso.
- `app_fastapi.py`: Dashboard web live para monitoramento em tempo real.
- `config/config.json`: Parâmetros operacionais e thresholds.
- `docker-compose.vps.yml`: Configuração para deploy direto no Docker.

## Fluxo Padrão de Construção

1.  **Definir Escopo:** Exchange (Spot/Futures), pares monitorados e fontes de sinal.
2.  **Conexão:** Criar camada de conexão com `health_check` robusto.
3.  **Motor de Execução:** Implementar validação de `amount_to_precision`, `min_lot`, `notional_minimo` e `slippage`.
4.  **Camada de Risco:** Implementar pré-validação antes de qualquer chamada a `create_order`.
5.  **Logs Estruturados:** Configurar logs por módulo com separação clara de INFO, WARNING e ERROR.
6.  **Observabilidade:** Criar dashboard live alimentado exclusivamente pelos dados da exchange.
7.  **Deployment:** Dockerizar e validar os scripts de deploy na VPS.

## Checklist de Validação (Definição de Pronto)

Um sistema baseado nesta skill só é considerado PRONTO quando:
- [ ] O `operational_mode` está configurado corretamente.
- [ ] API keys possuem as permissões exatas necessárias (e nada mais).
- [ ] Testes de ordem pequena confirmam que não há erros de precisão.
- [ ] Bloqueios por risco aparecem nos logs de forma clara.
- [ ] O sistema opera em SANDBOX/TESTNET sem erros antes da mudança para LIVE.

## Armadilhas a Evitar

- Usar base de dados local como "verdade" para saldo (sempre consulte a API).
- Ignorar o `notional` mínimo exigido pela Binance em cada par.
- Misturar ativos de Hold com ativos de Trade no cálculo de banca.
- Tratar avisos de risco como erros de sistema (use `WARNING` para bloqueios lógicos).

---
© 2026 Cripto360 System Builder - Todos os direitos reservados.

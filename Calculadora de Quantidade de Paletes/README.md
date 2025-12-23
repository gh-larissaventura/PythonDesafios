# 📦 Calculadora de Quantidade de Paletes

Este repositório contém uma ferramenta de **Otimização Logística** desenvolvida em Python. O sistema calcula a quantidade exata de paletes necessários para uma carga, analisando restrições físicas e operacionais.

## 📋 O Desafio Original

A proposta inicial era simples: criar um script que recebesse o total de caixas e a capacidade de caixas por palete, retornando o número de paletes arredondado para cima.

*Exemplo simples:* Se tenho 100 caixas e cabem 10, preciso de 10 paletes.

## 🚀 Evolução: O Cenário Real (V2.0)

Percebi que o cálculo básico ignorava um fator crítico na logística: **o Peso**.
Um palete pode ter espaço para 50 caixas, mas se elas forem muito pesadas, o palete quebra antes de encher.

Por isso, evoluí o projeto para um **Simulador de Gargalos**, implementando as seguintes melhorias:

### 1. Análise de Gargalo (Bottleneck) ⚖️
O sistema agora solicita:
* Capacidade física (Quantas caixas cabem?)
* Limite de peso do palete (Quantos kg aguenta?)
* Peso unitário da caixa.

O algoritmo decide automaticamente qual é o **limite real** usando a lógica de `min(limite_volume, limite_peso)`.

### 2. Relatório de Decisão Inteligente 📊
O software não apenas cospe um número. Ele gera um relatório explicando o **motivo da limitação**:
* *"Limitação por VOLUME"* (Falta espaço).
* *"Limitação por PESO"* (O palete quebraria se enchesse mais).

### 3. Tratamento de Erros e Loops
* **Blindagem:** O sistema impede divisão por zero e números negativos.
* **Ciclo de Vida:** O usuário pode rodar múltiplas simulações sem reiniciar o programa (`while True`).

---

## 💻 Exemplo de Execução

Veja abaixo um caso onde o **Peso** foi o fator limitante (gargalo).
Note que, embora houvesse espaço para **50 caixas**, o palete quebraria com esse volume. O sistema reduziu a capacidade automaticamente para **25 caixas** para respeitar a segurança.

```text
📊 Dados da Carga:
Total de caixas: 200
Capacidade Física (Espaço): 50 caixas
Peso por caixa: 100 kg  <-- CAIXA PESADA
Peso Máx do Palete: 2500 kg

========================================
🚛 RELATÓRIO DE OTIMIZAÇÃO
========================================
Limitação Definida por: PESO (Palete quebraria)
Capacidade Real por Palete: 25 caixas
----------------------------------------
✅ TOTAL DE PALETES: 8
⚖️  Peso por Palete Cheio: 2500.00 kg
========================================
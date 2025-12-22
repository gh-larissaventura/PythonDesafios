# Desafio de Código: Cálculo de Exportação 🚢

Este repositório contém a minha solução para um desafio de lógica de programação em Python, focado em estruturas condicionais e cálculos matemáticos simples para análise de dados.

## 📋 O Desafio Original

O problema proposto consistia em criar um sistema para uma exportadora. O programa deveria receber:
1. Peso da carga (em toneladas).
2. Preço por tonelada.
3. Tipo de cliente (escrito por extenso: "Novo cliente", "Cliente fidelizado" ou "Cliente premium").

Com base nisso, o sistema deveria aplicar descontos automáticos:
* **Novo cliente:** 0% de desconto.
* **Cliente fidelizado:** 5% de desconto.
* **Cliente premium:** 10% de desconto.

## 🚀 Minha Melhoria (Feature Extra)

Ao analisar o desafio, percebi que digitar o nome do cliente ("Cliente premium") poderia gerar erros de digitação e frustrar o usuário.

Por isso, **fui além do enunciado** e implementei um **Menu Numérico Interativo**.
Em vez de digitar textos longos, o usuário agora seleciona opções simples:
* `1` para Novo Cliente
* `2` para Cliente Fidelizado
* `3` para Cliente Premium

Isso melhora a UX (Experiência do Usuário) e evita erros de execução.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Lógica de Programação:** Estruturas condicionais (`if/elif/else`).
* **Tratamento de Dados:** Conversão de tipos (`float` e `int`) e formatação de strings (f-strings).

## 💻 Como Executar
Certifique-se de ter o Python instalado. Execute o arquivo no terminal:

```bash
python calculo_exportacao.py
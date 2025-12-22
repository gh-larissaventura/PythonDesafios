# 🚢 Sistema de Cálculo de Exportação (Versão Modular)

Este repositório contém a solução aprimorada para um desafio de lógica de programação em Python, simulando o sistema de precificação de uma empresa de logística.

## 📋 O Desafio Original

O objetivo era criar um script que recebesse o peso da carga, preço por tonelada e categoria do cliente, retornando o valor final com descontos aplicados (0%, 5% ou 10%).

## 🚀 Melhorias e Evolução do Código

Para simular um ambiente de produção real, não me limitei ao básico. Refatorei o código aplicando conceitos avançados para melhorar a **Experiência do Usuário (UX)** e a **Robustez** do sistema.

As principais implementações foram:

### 1. Blindagem contra Erros (Error Handling) 🛡️
Utilizei blocos `try-except` para capturar falhas.
* **Antes:** Se o usuário digitasse texto no lugar de números, o programa "quebrava" (crash).
* **Agora:** O sistema avisa amigavelmente o erro e reinicia o processo, além de aceitar números com vírgula (padrão BR) convertendo automaticamente para ponto.

### 2. Modularização (Clean Code) 🧩
Transformei o script linear em **Funções Especializadas**:
* `obter_dados_usuario()`: Responsável apenas pela interface e validação de inputs.
* `calcular_desconto()`: Contém as regras de negócio (lógica dos descontos).
* `main()`: Função controladora que orquestra o fluxo.
Isso torna o código mais legível, testável e fácil de manter.

### 3. Loop de Execução Contínua 🔄
Implementei uma estrutura `while True`.
* O usuário pode realizar múltiplos cálculos seguidos sem precisar reiniciar o programa manualmente.
* O encerramento é controlado pelo usuário através de um menu de saída.

### 4. Menu Interativo Numérico 🔢
Substituí a entrada de texto livre (ex: "Cliente fidelizado") por um menu numérico (1, 2, 3), evitando erros de digitação.

---

## 🛠️ Tecnologias e Conceitos Aplicados
* **Linguagem:** Python 3
* **Estrutura de Dados:** Tuplas e Variáveis.
* **Controle de Fluxo:** `if/elif/else`, `while/break`.
* **Tratamento de Exceções:** `try/except ValueError`.
* **Modularização:** Definição de funções (`def`), parâmetros e retorno de valores.

## 💻 Como Executar

Certifique-se de ter o Python instalado. Clone o repositório e execute:

```bash
python calculo_exportacao.py
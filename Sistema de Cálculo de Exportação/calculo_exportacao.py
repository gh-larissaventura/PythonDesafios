print("--- Sistema de Cálculo de Exportação (Modular) ---")


def obter_dados_usuario():
    """
    Função responsável apenas por coletar e tratar os inputs do usuário.
    Retorna: peso, preco, codigo_cliente
    """
    peso_input = input("Digite o peso da carga (em toneladas): ").replace(",", ".")
    peso = float(peso_input)

    preco_input = input("Digite o preço por tonelada (em dólares): ").replace(",", ".")
    preco_por_tonelada = float(preco_input)

    print("\nSelecione o tipo de cliente:")
    print("1 - Novo cliente")
    print("2 - Cliente fidelizado")
    print("3 - Cliente premium")

    codigo_cliente = int(input("Digite a opção desejada (1, 2 ou 3): "))

    # Validação simples
    if codigo_cliente not in [1, 2, 3]:
        raise ValueError("Código de cliente inválido")

    return peso, preco_por_tonelada, codigo_cliente


def calcular_desconto(codigo):
    """
    Recebe o código do cliente e retorna a % de desconto e o nome da categoria.
    """
    if codigo == 2:
        return 0.05, "Cliente fidelizado"
    elif codigo == 3:
        return 0.10, "Cliente premium"
    else:
        return 0.00, "Novo cliente"


def main():
    """
    Função Principal (O Gerente): Controla o loop e chama os outros departamentos.
    """
    while True:
        try:
            print("\n📝 Iniciando novo cálculo...")

            # 1. Chama o departamento de Input
            # Note que recebemos 3 valores de uma vez (Desempacotamento)
            peso, preco, codigo = obter_dados_usuario()

            # 2. Chama o departamento de Estratégia
            desconto, tipo_cliente = calcular_desconto(codigo)

            # 3. Realiza os cálculos finais
            valor_total = peso * preco
            valor_final = valor_total * (1 - desconto)

            # 4. Exibe o Relatório
            print("-" * 30)
            print(f"Tipo de Cliente: {tipo_cliente}")
            print(f"Valor original: US$ {valor_total:.2f}")
            if desconto > 0:
                print(f"Desconto aplicado: {desconto * 100:.0f}%")
            print(f"Valor Final a Pagar: US$ {valor_final:.2f}")
            print("-" * 30)

        except ValueError:
            print("\n❌ ERRO: Dados inválidos. Certifique-se de usar números e pontos.")

        # Controle de saída do loop
        continuar = input("\nDeseja calcular outra remessa? (S/N): ").upper()
        if continuar != 'S':
            print("\nEncerrando o sistema... Até logo! 👋")
            break


# Esta linha verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
print("--- Sistema de Cálculo de Exportação ---")

# 1. Leitura dos dados
peso = float(input("Digite o peso da carga (em toneladas): "))
preco_por_tonelada = float(input("Digite o preço por tonelada (em dólares): "))

# 2. Menu de Seleção de Cliente
print("\nSelecione o tipo de cliente:")
print("1 - Novo cliente")
print("2 - Cliente fidelizado")
print("3 - Cliente premium")

# Aqui convertemos a entrada para número inteiro (int)
codigo_cliente = int(input("Digite a opção desejada (1, 2 ou 3): "))

# 3. Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada

# 4. Lógica do Desconto (Agora verificando o NÚMERO)
if codigo_cliente == 2:
    desconto = 0.05  # 5% para Fidelizado
    tipo_real = "Cliente fidelizado" # Só para mostrar no print final
elif codigo_cliente == 3:
    desconto = 0.10  # 10% para Premium
    tipo_real = "Cliente premium"
else:
    desconto = 0.00  # Novo cliente ou opção inválida (padrão)
    tipo_real = "Novo cliente"

# 5. Cálculo final
valor_final = valor_total * (1 - desconto)

# 6. Saída
print("-" * 30)
print(f"Tipo de Cliente: {tipo_real}")
print(f"Valor original: US$ {valor_total:.2f}")
if desconto > 0:
    print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor Final a Pagar: US$ {valor_final:.2f}")
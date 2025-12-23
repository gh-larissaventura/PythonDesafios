import math

print("--- LogiPallet: Otimizador de Cargas ---")


def obter_dados_logistica():
    """
    Coleta e valida inputs. Garante que não haja números negativos ou zero na capacidade.
    """
    while True:
        try:
            caixas_input = input("Digite o total de caixas produzidas: ").strip()
            total_caixas = int(caixas_input)

            if total_caixas < 0:
                print("❌ Erro: O número de caixas não pode ser negativo.")
                continue

            cap_input = input("Digite a capacidade de cada palete: ").strip()
            capacidade = int(cap_input)

            if capacidade <= 0:
                print("❌ Erro: A capacidade do palete deve ser maior que zero.")
                continue

            # Se chegou aqui, tudo está certo
            return total_caixas, capacidade

        except ValueError:
            print("❌ Erro: Digite apenas números inteiros.")


def calcular_paletes(total, capacidade):
    """
    Retorna:
    1. Total de paletes necessários (int)
    2. Quantidade de paletes totalmente cheios (int)
    3. Quantas caixas ficam no último palete (int)
    """
    # math.ceil arredonda para cima (ex: 7.1 -> 8)
    paletes_totais = math.ceil(total / capacidade)

    # // faz a divisão inteira (ex: 150 // 20 = 7)
    paletes_cheios = total // capacidade

    # % pega o resto da divisão (ex: 150 % 20 = 10 caixas sobrando)
    resto_caixas = total % capacidade

    # Ajuste lógico: Se não sobra nada, o último palete também é cheio
    if resto_caixas == 0 and total > 0:
        paletes_cheios = paletes_totais
        caixas_ultimo = capacidade  # O último está cheio
    else:
        caixas_ultimo = resto_caixas

    return paletes_totais, paletes_cheios, caixas_ultimo


def main():
    while True:
        print("\n🏗️  Nova Simulação de Carga...")

        # 1. Entrada
        total_caixas, capacidade = obter_dados_logistica()

        # 2. Processamento
        total_nec, cheios, ultimo_qtd = calcular_paletes(total_caixas, capacidade)

        # 3. Saída (Relatório Rico)
        print("-" * 30)
        print(f"📦 Total de Caixas: {total_caixas}")
        print(f"📏 Capacidade por Palete: {capacidade}")
        print("-" * 30)
        print(f"✅ PALETES NECESSÁRIOS: {total_nec}")
        print(f"   ├─ Paletes Completos: {cheios}")
        if total_nec > cheios:
            print(f"   └─ Palete Incompleto: 1 (com {ultimo_qtd} caixas)")
        print("-" * 30)

        # 4. Loop
        continuar = input("\nCalcular outra carga? (S/N): ").upper()
        if continuar != 'S':
            print("\nEncerrando LogiPallet... Bom trabalho! 🚛")
            break


if __name__ == "__main__":
    main()
import math

print("--- LogiPallet V2.0: Volume & Peso ---")


def obter_dados_logistica():
    """
    Coleta: Total de caixas, Capacidade (qtd), Peso da Caixa, Peso Máx Palete.
    """
    while True:
        try:
            print("\n📊 Dados da Carga:")
            total_caixas = int(input("Total de caixas produzidas: ").strip())

            print("\n📏 Restrições do Palete:")
            cap_volume = int(input("Quantas caixas cabem fisicamente (espaço)? ").strip())

            peso_caixa = float(input("Qual o peso de UMA caixa (kg)? ").strip().replace(",", "."))
            peso_max_palete = float(input("Qual o peso MÁXIMO que o palete aguenta (kg)? ").strip().replace(",", "."))

            # Validação básica
            if total_caixas < 0 or cap_volume <= 0 or peso_caixa <= 0 or peso_max_palete <= 0:
                print("❌ Erro: Valores devem ser positivos e maiores que zero.")
                continue

            return total_caixas, cap_volume, peso_caixa, peso_max_palete

        except ValueError:
            print("❌ Erro: Digite apenas números válidos.")


def calcular_cenario(total_caixas, cap_volume, peso_caixa, peso_max_palete):
    """
    Define o gargalo (limite real) e calcula os paletes.
    """
    # 1. Descobrir quantas caixas cabem pelo limite de PESO
    # Ex: Palete aguenta 1000kg / caixa de 10kg = 100 caixas
    cap_peso = int(peso_max_palete // peso_caixa)

    # 2. O limite real é o MENOR número entre o espaço e o peso
    # A função min() faz isso automaticamente pra gente
    capacidade_real = min(cap_volume, cap_peso)

    # 3. Identificar qual foi o motivo da limitação (para o relatório)
    if cap_peso < cap_volume:
        motivo_limitacao = "PESO (Palete quebraria)"
    else:
        motivo_limitacao = "VOLUME (Falta de espaço)"

    # 4. Cálculos finais com a capacidade real
    paletes_totais = math.ceil(total_caixas / capacidade_real)
    paletes_cheios = total_caixas // capacidade_real
    caixas_ultimo = total_caixas % capacidade_real

    if caixas_ultimo == 0 and total_caixas > 0:
        caixas_ultimo = capacidade_real
        paletes_cheios = paletes_totais

    return paletes_totais, capacidade_real, motivo_limitacao, caixas_ultimo


def main():
    while True:
        try:
            # 1. Entrada
            total, cap_vol, peso_cx, peso_max = obter_dados_logistica()

            # 2. Processamento
            qtd_paletes, cap_real, motivo, ultimo = calcular_cenario(total, cap_vol, peso_cx, peso_max)

            # 3. Saída Rica
            print("\n" + "=" * 40)
            print(f"🚛 RELATÓRIO DE OTIMIZAÇÃO")
            print("=" * 40)
            print(f"Limitação Definida por: {motivo}")
            print(f"Capacidade Real por Palete: {cap_real} caixas")
            print("-" * 40)
            print(f"✅ TOTAL DE PALETES: {qtd_paletes}")

            # Cálculo do peso total de um palete cheio (apenas informativo)
            peso_palete_cheio = cap_real * peso_cx
            print(f"⚖️  Peso por Palete Cheio: {peso_palete_cheio:.2f} kg")
            print("=" * 40)

            if input("\nNova simulação? (S/N): ").upper() != 'S':
                break
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
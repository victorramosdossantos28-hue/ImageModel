def calculate_statistics(numbers: list[int]) -> tuple[int, float, int, int]:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numbers: Lista de números inteiros para análise.
    
    Returns:
        Tupla contendo (total, média, máximo, mínimo).
    """
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


def main() -> None:
    """Executa o programa principal."""
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    total, average, maximum, minimum = calculate_statistics(numbers)
    
    print(f"Total:   {total}")
    print(f"Média:   {average:.2f}")
    print(f"Máximo:  {maximum}")
    print(f"Mínimo:  {minimum}")


if __name__ == "__main__":
    main()
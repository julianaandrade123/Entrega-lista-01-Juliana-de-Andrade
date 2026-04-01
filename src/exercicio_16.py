def odd_numbers(n: int) -> list[int]:
    """
    Retorna os números ímpares de 1 até n.

    Args:
        n (int): limite superior

    Returns:
        list[int]: lista de números ímpares
    """
    return [x for x in range(1, n + 1) if x % 2 != 0]

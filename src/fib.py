def fib(n):
    """フィボナッチ数列のn番目を返す

    Args:
        n (int): フィボナッチ数列の何番目か指定
    
    Returns:
        F_n (int): フィボナッチ数列のn番目の値
    """
    if n in [0, 1]:
        return 1
    
    F = [1]*(n)
    for i in range(2, n):
        F[i] = F[i-1] + F[i-2]
    
    return F[-1]

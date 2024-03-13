def recursao(n):
    if n == 1 or n == 0:
        return 1
    return n * recursao(n-1)

recursao(5)
def funcion (n, p):
    if n == 1:
        return p
    else:
        return n*p + funcion(n-1, p)
print(funcion(6,7))
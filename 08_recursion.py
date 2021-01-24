def get_factorial(n):
    if n < 2:
        return n
    else:
        return n * get_factorial(n-1)


# result = get_factorial(5)
# print(result)

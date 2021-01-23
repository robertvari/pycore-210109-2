def add_numbers(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    return a / b


# add numbers
result = add_numbers(2, 2)


# multiply result with 10
result = multiply(result, 10)


# divide result with 3
result = divide(result, 3)


print(result)

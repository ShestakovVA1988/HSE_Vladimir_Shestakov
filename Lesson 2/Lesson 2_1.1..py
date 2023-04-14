#Создайте ряд функций для проведения математических вычислений:

# 1. функция вычисления факториала числа (произведение натуральных чисел от 1 до n). Принимает в качестве аргумента число, возвращает его факториал;

def func_1_factorial(number: int) -> int | float:
    start = 1
    result = 1
    for i in range(number):
        result = result * start
        start += 1
    return result

print(f"Факториал числа a({a}) - {func_1_factorial(a)}")
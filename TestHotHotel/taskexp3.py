def is_prime(n):
    """Проверяет, является ли число простым"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_in_range(start, end):
    """Возвращает массив простых чисел в заданном диапазоне"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Пример использования функции
start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))
result = primes_in_range(start, end)
print("Простые числа в диапазоне от", start, "до", end, ":", result)

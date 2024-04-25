def find_common_divisors(numbers):
    if not numbers:
        return []

    min_number = min(numbers)
    common_divisors = []

    for divisor in range(2, min_number + 1):  # Изменил начальное значение с 1 на 2
        if all(number % divisor == 0 for number in numbers):
            common_divisors.append(divisor)

    return common_divisors

def main():
    input_str = input("Введите массив положительных целых чисел через пробел: ")
    numbers = list(map(int, input_str.split()))
    
    result = find_common_divisors(numbers)
    print("Общие делители для введенных чисел:", result)

if __name__ == "__main__":
    main()
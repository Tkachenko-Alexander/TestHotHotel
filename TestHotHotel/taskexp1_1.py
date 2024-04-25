n = int(input())

if 0 <= n <= 10000:
    if n == 1 or (n % 10 == 1 and n != 11 and n < 100) or (n % 10 % 10 == 1 and n % 100 != 11):
        print(n, 'компьютер')
    elif n == 2 or n == 3 or n == 4 or ((n % 10 == 2 or n % 10 == 3 or n % 10 == 4)
        and n != 12 and n != 13 and n != 14 and n < 100) or \
        ((n % 10 % 10 == 2 or n % 10 % 10 == 3 or n % 10 % 10 == 4) and
        (n % 100 != 12 or n % 100 != 13 or n % 100 != 14)):
        print(n, 'компьютера')
    else:
        print(n, 'компьютеров')
else:
    print('Введите число от 1 до 10000')

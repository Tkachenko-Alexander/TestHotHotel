def computer_word(count):
    if count % 10 == 1 and count % 100 != 11:
        return "компьютер"
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
        return "компьютера"
    else:
        return "компьютеров"


number = int(input("Введите число: "))
word = computer_word(number)
print(f"{number} {word}")

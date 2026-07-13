secret_number = 8 

user_guess = 0

print("Я загадал число от 1 до 10 попробуй отгадать!")

while user_guess != secret_number:

    user_guess = int(input("Введи свой вариант:"))

    if user_guess < secret_number:
        print("Не отгадал! Мое число БОЛЬШЕ!")
    elif user_guess > secret_number:
        print("Не отгадал! Мое число МЕНЬШЕ!")

print("Ура ты победил!")
import random

rps = ["камень", "ножници", "бумага"]


def determine_winner(plears, computar):
    if plears == computar:
        return "Ничья!"
    wins = {
        "камень": "ножници",
        "ножници": "бумага",
        "бумага": "камень"
    }
    if wins[plears] == computar:
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"


while True:
    pl = input("Выберите камень, ножницы или бумага:").lower().strip()

    if pl == "выход":
        print("Игра завершена")
    if pl not in rps:
        print("Некорректный ввод")
        continue

    computer_choice = random.choice(rps)
    print(f"Компьютер выбрал: {computer_choice}")
    print(determine_winner(pl, computer_choice))
    print("-" * 30)
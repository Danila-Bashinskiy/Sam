import random
import sys
import time

print("Здравствуйте, меня зовут Сэм,"
      " я исскуственный интелект созданный для 4 программ и"
      " простого разговора с людьми."
      )
print("У меня есть 4 программы, 1-ая из них - это калькулятор, чтобы его выбрать напишите 1.")
print("2-ая из них - это программа для подкидывание монетки, 'Орел и решка', чтобы ее выбрать напишите 2.")
print("3-ая из этих трёх, это мини-игра - 'Камень, Ножницы, Бумага', чтобы выбрать эту мини-игру, "
      "напишите 3.")
print("4-ая и почти последняя - это приложение Kahoot! Создатель тестов и последущее прохождение их.")
print("Иначе, если вы хотите поговорить с Сэмом, напишите '0'")
print("5-ая и конечная - это типичное приложение таймер. Чтобы его активировать напишите 'time'.")


select = input()
if select == "time":

    timer = time.time()
    for i in range(99999999999999999999999):
        timer2 = time.time()
        sum_timer = timer2 - timer
        print(round(sum_timer))
        time.sleep(1)

if select == "4":
    import time
    import sys
    points = 0
    print("Привет! Это приложение Kahoot!")
    print("Чтобы узнать почему сейчас наше приложение находится")
    print("В командной строке напишите знак '?'")
    print("Иначе, чтобы выбрать редактор теста напишите слово 'Edit'")
    print("Чтобы приложение вас поняло пишите чётко цифры, знаки"
    " или слова и без пробелов.")
    select = input()
    if select != "?" or "Edit":
        print("Извините, но я вас не понимаю!")

    if select == "?":
        print("                                    ")
        print("Из-за технических неполадок мы перешли на версию 1.0")
        print("Эта версия может показываться только в командной строке")
        print("И поддерживает только ОС Windows")
        print("Извините за представленные неудобства, но пока что по другому никак")
    elif select == "Edit":
        print("                                    ")
        print("Отлично! Вы выбрали редактор тестов.")
        print("Для начала напишите 1-ый вопрос который будет в тесте")
        one_q = input()
        print("Теперь напишите варианты ответов их всего будет 4.")
        print("Если вы хотите оставить только 1, 2 или 3 вариантов."
        "ответа просто можете поставить пробел.")
        print("P.S. После вопроса всегда пишите правильный ответ")
        one_one_answ = input()
        one_two_answ = input()
        one_three_answ = input()
        one_four_answ = input()
        print("Отлично! Теперь снова напишите вопрос, а потом ответы, и так до 5 вопросов.")
        two_q = input()
        two_one_answ = input()
        two_two_answ = input()
        two_three_answ = input()
        two_four_answ = input()
        print("Супер! Пишите вопросы дальше.")
        three_q = input()
        three_one_answ = input()
        three_two_answ = input()
        three_three_answ = input()
        three_four_answ = input()
        print("Вам осталось написать еще 2 вопроса.")
        four_q = input()
        four_one_answ = input()
        four_two_answ = input()
        four_three_answ = input()
        four_four_answ = input()
        print("Еще один вопрос.")
        five_q = input()
        five_one_answ = input()
        five_two_answ = input()
        five_three_answ = input()
        five_four_answ = input()
        print("Великолепно! Чтобы выполнить ваш тест напишите 'Go'")
    
        end = input()

    if end == "Go":
        print("             ")
        print("1-ый вопрос:", one_q)
        print("Варианты ответов:")
        print(one_four_answ, ";", one_three_answ)
        print(one_two_answ, ";", one_one_answ) 
        one_answ = input()
        if one_answ == one_one_answ:
            print("Отлично! Вы ответили правильно на первый вопрос. +1000 баллов")
            points = points + 1000
        else: 
            print("Не правильно. Повезет в следущий раз.")
            print("2-ой вопрос:", two_q)
            print("Варианты ответов:")
            print(two_two_answ, ";", two_one_answ)
            print(two_four_answ, ";", two_three_answ)
            two_answ = input()
        if two_answ == two_one_answ:
            print("Супер! Вы ответили правильно. +1000 баллов")
            points = points + 1000
        else:
            print("О нет! Вы ответили не правильно.")
            print("3-ой вопрос:", three_q)
            print("Варианты ответов:")
            print(three_one_answ, ";", three_two_answ)
            print(three_four_answ, ";", three_three_answ)
        three_answ = input()
        if three_answ == three_one_answ:
            print("Вау! Вы ответили правильно. +1000 баллов")
            points = points + 1000
        else:
            print("Как же так! Вы ответили не правильно.")
            print("4-ой вопрос:", four_q)
            print("Варианты ответов:")
            print(four_four_answ, ";", four_three_answ)
            print(four_one_answ, ";", four_two_answ)
        four_answ = input()
        if four_answ == four_one_answ:
            print("Супер! Вы ответили правильно. +1000 баллов")
            points = points + 1000
        else:
            print("Мммм как же так! Вы ответили не правильно.")
            print("5-ой вопрос:", two_q)
            print("Варианты ответов:")
            print(five_two_answ, ";", five_one_answ)
            print(five_four_answ, ";", five_three_answ)
            five_answ = input()
        if five_answ == five_one_answ:
            print("Класс! Вы ответили правильно. +1000 баллов")
            points = points + 1000
        else:
            print("Вау, хороший ответ! Но не верно.")

        if points == 1000:
            status = "Честно? Может быть и лучше..."
        elif points == 2000:
            status = "Стоит подтянуть знания!"
        elif points == 3000:
            status = "Junior!"
        elif points == 4000:
            status = "Middle!"
        elif points == 5000:
            status = "Senior!"
        elif points == 0:
            status = "I'll be back"
        print("                ")
        print("И так! Идет подсчет баллов...")
        print("*", end="")
        sys.stdout.flush()
        time.sleep(1)
        print("*", end="")
        sys.stdout.flush()
        time.sleep(0.2)
        print("*", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        print("*", end="")
        sys.stdout.flush()
        time.sleep(1)
        print("100%")
        print("Вы получили", points, "баллов!")
        print("Ваш статус:")
        sys.stdout.flush() 
        print(status)
    else:
        print("Извините, но я вас не понимаю!")
if select == "1":
    print("Отлично! Вы выбрали программу 'Калькулятор'.")
    print("Здравствуйте, вас приветствует калькулятор Сэм.")
    print("Для того чтобы выполнить какое либо действие напишите,")
    print("число №1, способ вычисления между числами, Число №2")
    print("(Пишите числа и способ вычисления без пробелов после них, ")
    print("иначе это приведёт к авто. заканчиванию программы.)")
    one = int(input())
    sposob = input()
    two = int(input())

    if sposob == "/":
        print("Сэм произвёл расчет, он составляет...")
        print(one / two)
        input()

    elif sposob == "*":
        print("Сэм произвёл расчет, он составляет...")
        print(one * two)
        input()

    elif sposob == "-":
        print("Сэм произвёл расчет, он составляет...")
        print(one - two)
        input()

    elif sposob == "+":
        print("Сэм произвёл расчет, он составляет...")
        print(one + two)
        input()
    else:
        print("Сэм вас не понял! Повторите расчет правильно!")
        input()


elif select == "2":
    print("Супер! Вы выбрали программу - 'Орел и решка'.")

    print("Здравствуйте, это симулятор подкидывания монетки, для использования приложения выберите язык.")
    print("_____________________________________________________________________________________________")
    print("Hello, this is a coin toss simulator, please select a language to use the application.")
    print("_____________________________________________________________________________________________")
    time.sleep(4)
    print("Для того чтобы выбрать Русский язык напишите 'Rus', для того чтобы выбрать английский язык напишите 'Eng'.")
    print("_____________________________________________________________________________________________")
    print("To select the Russian language write 'Rus', to select the English language write 'Eng'.")  # Начало
    lang = input()

    if lang == "Rus":
        print("Отлично! Вы выбрали русский язык.")
        print("Для того чтобы подкинуть монетку напишите 'Start'.")
    elif lang == "Eng":
        print("Excellent! You have selected English language.")
        print("To toss a coin write 'Start'.")
    # Выбор языка
    else:
        print("Сэм вас не понял! Повторите запрос.")
        print("Sam didn't get you! Please try again.")

    start = input()
    if start != "Start":
        print("Сэм вас не понял! Повторите запрос.")
        print("Sam didn't get you! Please try again.")

    if lang == "Rus" and start == "Start":  # Подкидывание монетки на русском
        print("Монетка подкидывается")
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        r = (random.randint(1, 2))
        if r == 1:
            print("Выпал орел!")
            input()
        if r == 2:
            print("Выпала Решка!")
            input()

    if lang == "Eng" and start == "Start":  # Подкидывание монетки на английском
        print("The coin is tossed")
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        sys.stdout.flush()
        print(".", end="")
        time.sleep(1)
        r = (random.randint(1, 2))
        if r == 2:
            print("The eagle fell!")
            input()
        if r == 1:
            print("Tails fell!")
            input()

elif select == "3":
    print("Великолепно! Вы выбрали мини-игру - 'Камень, Ножницы, Бумага'.")
    select_two = 0
    print("Напишите что вы выберите, 'Камень', 'Ножницы' или 'Бумага'")
    select_one = 0
    incorrect_input = True
    while incorrect_input:   #проверка
        select_one = input()
        if select_one == "Камень" or select_one == "Ножницы" or select_one == "Бумага":
            incorrect_input = False
        if incorrect_input == True:
            print("Не так! Напишите 'Камень', 'Ножницы' или 'Бумага'.")

    if select_one == "Камень" or "Ножницы" or "Бумага":
        print("Отлично вы выбрали", select_one)
        time.sleep(2)
        print("Ждем ответа от второго участника...")
        print(".", end="")
        sys.stdout.flush()
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
        time.sleep(1)
            
    select_two = random.randrange(1, 3)
    if select_two == 1:
        print("Противник выбрал Камень!")

    elif select_two == 2:
        print("Противник выбрал Бумагу!")
    elif select_two == 3:
        print("Противник выбрал Ножницы!")

    if select_two == 1 and select_one == "Камень":
        print("Ничья!")
        input()
    if select_two == 2 and select_one == "Бумага":
        print("Ничья!")
        input()
    if select_two == 3 and select_one == "Ножницы":
        print("Ничья!")
        input()
    if select_two == 1 and select_one == "Бумага":
        print("Ты выиграл!")
        input()
    if select_two == 1 and select_one == "Ножницы":
        print("Ты проиграл!")
        input()
    if select_two == 2 and select_one == "Камень":
        print("Ты проиграл!")
        input()
    if select_two == 2 and select_one == "Ножницы":
        print("Ты выиграл!")
        input()
    if select_two == 3 and select_one == "Камень":
        print("Ты выиграл!")
        input()
    if select_two == 3 and select_one == "Бумага":  # Алгоритм окончания игры
        print("Ты проиграл!")
        input()

elif select == "0":
    print("Здравствуйте, о чем Вы хотели поговорить?")
    spk = input()
    if spk == "Как дела?":
        spk_random = random.randint(1, 4)
        if spk_random == 1:
            print("Отлично!")
            input()
        elif spk_random == 2:
            print("Супер!")
            input()
        elif spk_random == 3:
            print("Великолепно!")
            print("Спасибо что спросили.")
            input()
        elif spk_random == 4:
            print("Хорошо!")
            input()
    elif spk == "Как поживаешь?":
        spk_random = random.randint(1, 4)
        if spk_random == 1:
            print("Отлично!")
            input()
        elif spk_random == 2:
            print("Супер!")
            input()
        elif spk_random == 3:
            print("Великолепно!")
            print("Спасибо что спросили.")
            input()
        elif spk_random == 4:
            print("Хорошо!")
            input()
    elif spk == "Что ты умеешь?":
        print("Немного, но все что я умею полезно.")
        input()
    else:
        print("Извините, но я вас не понимаю!")
        input()
else:
    print("Извините, но Сэм вас не понимает.")
    input()

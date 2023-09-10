
#словари формата {”слово”: “перевод”, ...}.
words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

# ранги пользователя в зависимости от успехов.
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
#словарь с записями о верных и неверных ответах.
answers = {}
difficult = {
    "1": words_easy,
    "2": words_medium,
    "3": words_hard
}
# Начало программы приветствие и выбор ответа, чтобы не набирать текст указаны цифры,
# также эта цифра запускает уровень сложности словаря
print("Добро пожаловать в игру!")
print("\nВыберите уровень сложности:")
print("1. Легкий")
print("2. Cредний")
print("3. Cложный")

# Ввод уровня сложности
user_input = input("Введите число, соответствующее уровню сложности: ").lower()
right_answers = 0 # счетчик подсчета True из словаря answers!
print(f"Выбран уровень сложности, мы предложим 5 слов, подберите перевод.")
if user_input in difficult: # Условие если совпадает со словарем difficult
    chosen_dict = difficult[user_input] # проверяет если такой уровень сложности


    for k, v in chosen_dict.items(): # перебор по ключам и знач.
        hidden = ('*' * len(v)) # скрываем правильный ответ звездами.
        print(f"{k},______   Подсказка:{len(v)}  букв,начинается на {v[:1]} {hidden}") # Вопрос
        answer_input = str(input("Введите ответ")).lower() # ответ
        if answer_input == v:  # Проверка на правильность ответа совпадает ли ввод со знач и словаря

                print(f"Правильно это {k}- это {v}.") #Правильный ответ
                answers[k] = True   #добавляем в словарь

        else:
                print(f"Неверно, это {k}- это {v}.")
                answers[k] = False



else:
    print("Неверный уровень сложности. Попробуйте снова.") #Программа остановится если выбран неверный уровень сложности

for ans in answers.values(): #Подсчет True из словаря answers!
    right_answers += int(ans)

print("Правильно отвечены слова:  ")  #Вывод True из словаря answers!
for k,v in answers.items():
    if v is True:
        print(k)

print("Неправильно отвечены слова: ") #Вывод False из словаря answers!
for k,v in answers.items():
    if v is False:
        print(k)

print(f" Ваш ранг: {levels[right_answers]}") #Ранг на основа ♂️right♂️ answers!









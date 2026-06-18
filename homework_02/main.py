#Задание 1: Получение однозначного числа
#Пользователь вводит целое число, программа складывает все цифры числа, с полученным числом — то же самое, и так до тех пор, пока не получится однозначное число.
#Примеры:
#545   -> 5
#12345 -> 6

digits = input()
while True:
    temp = 0
    for i in range(len(digits)):
        temp += int(digits[i])
    digits = str(temp)
    if len(digits) == 1:
        break
print(temp)


#Задание 2: Кинотеатр
#Дан список списков, каждый вложенный список состоит из 1 и 0, количество вложенных списков — количество рядов. Пользователь вводит, сколько билетов ему требуется. Программа должна найти ряд, где можно приобрести нужное количество билетов (места должны быть рядом). Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд). Если таких мест нет, то вывести False.
#Примеры:
#[[0,1,1,0], [1,0,0,0], [0,1,0,0]], 2 -> 1
#[[0,1,1,0], [1,0,1,0], [1,1,0,1]], 2 -> False
#lst = [[0,1,1,0], [1,0,0,0], [0,1,0,0]]
lst = [[0,1,1,0], [1,0,1,0], [1,1,0,1]]
coll = int(input())
for i in range(len(lst)):
    flag = False
    temp_coll = 0
    for j in range(len(lst[i])):
        if lst[i][j] == 0:
            temp_coll += 1
        else:
            temp_coll = 0
    if coll <= temp_coll:
        flag = True
        break
if flag:
    print(i)
else:
    print("False")


#Задание 3: Алгоритм RLE
#Необходимо написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
#Примеры:
#asssdddsssddd -> 1a3s3d3s3d
#aaabbbbccccc  -> 3a4b5c
#abcba         -> 1a1b1c1b1a

string = str(input())
result = ""
if len(string) > 0:
    coll_repeat = 0
    symbol = string[0]
    for i in range(len(string)):
        if string[i] == symbol:
            symbol = string[i]
            coll_repeat += 1
        else:
            result += symbol+str(coll_repeat)
            symbol = string[i]
            coll_repeat = 1
    result += symbol+str(coll_repeat)
print(result)



#Реализуйте программу для шифрования текста с помощью шифра Цезаря.
#Шифр Цезаря — это метод шифрования, при котором каждая буква в тексте заменяется буквой, стоящей на фиксированное число позиций дальше в алфавите.

#Требования
#Программа должна принимать на вход:
#Строку текста для шифрования
#Ключ шифра (число от 0 до 25)
#Правила шифрования:
#Шифруются только латинские буквы (a-z, A-Z)
#Сохраняется регистр букв (заглавные остаются заглавными)
#Пробелы, цифры и знаки препинания остаются без изменений
#Сдвиг циклический (после 'z' идет 'a', после 'Z' идет 'A')
#Примеры
#"Hello World", 3      -> "Khoor Zruog"
#"Python is great!", 5 -> "Udymts nx lwjfy!"
#"XYZ abc", 3          -> "ABC def"
#"Test 123", 1         -> "Uftu 123"
#Алгоритм
#Для каждого символа в строке:
#Если это латинская буква, найти её позицию в алфавите
#Добавить к позиции значение ключа
#Если результат больше 25, использовать остаток от деления на 26
#Преобразовать обратно в букву, сохранив регистр
#Если это не буква, оставить символ без изменений

alphabetLower = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = ""
result = ""
print("Введите строку:", end="")
string = input()
print("Введите ключ шифра:", end="")
key = input()
if key == "": key = 1
key = int(key)

for i in range(len(string)):
    if string[i].isupper():
        alphabet = alphabetUpper
    else:
        alphabet = alphabetLower

    flag = False
    for k in range(len(alphabet)):
        if alphabet[k] == string[i]:
            flag = True
            if k + key >= len(alphabet):
                result += alphabet[k + key - len(alphabet)]
            else:
                result += alphabet[k + key]
    if not flag:
        result += string[i]

print(result)



#Задание 5: Табель успеваемости
#Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида: 'название предмета' 'фамилия ученика' 'оценка'. После окончания ввода программа выводит в консоль название предмета, далее список учеников и все их оценки в виде таблицы.
#Примеры:
#Ввод:
#Математика Иванов  5
#Математика Иванов  4
#Литература Иванов  3
#Математика Петров  5
#Литература Сидоров 3
#Литература Петров  5
#Литература Иванов  4
#Математика Сидоров 3
#Математика Петров  5
#
#Результат:
#Математика # вводим название предмета
# выводим список учеников и их оценки
#Иванов  5 4
#Петров  5 5
#Сидоров 3
#Литература # вводим название предмета
# выводим список учеников и их оценки
#Иванов  3 4
#Сидоров 3
#Петров  5

result = {}
while True:
    string = str(input())
    if string == "" : break
    else:
        arr = string.split(" ")
        if result.get(arr[0]) is None : result[arr[0]] = {}
        if result[arr[0]].get(arr[1]) is None: result[arr[0]][arr[1]] = []
        result[arr[0]][arr[1]].append(arr[2])
for k, v in result.items():
    print(k, end=" ")
    for x, vv in v.items():
        print(x, end=" ")
        for j in vv:
            print(j, end=" ")
        print()
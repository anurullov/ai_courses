#Task 1
#23456 -> 25436
#30789 -> 38709
string = str(input())
new_str = list(string)
if len(string) != 5:
    print("число должно быть 5-и значным")
else:
    for i in range(len(string)):
        if i == 0 or i == 4 or i == 2:
            new_str[i] = string[i]
        elif i == 1:
            new_str[3] = string[i]
        elif i == 3:
            new_str[1] = string[i]
    print("".join(new_str))

#Task 2
#4  -> 0
#6  -> 1
#14 -> 4
dig = input()
holidays = 0
if dig != "":
    dig = int(dig)
    for i in range(1, dig+1):
        if not i % 7 or not i % 6:
            holidays += 1
    print(holidays)
else:
    print("вводить надо число большее 0")

#Task 3
#3, 4, 6  -> True
#5, 7, 8  -> False
#4, 5, 12 -> True
data = input().split(",")
if len(data) < 2:
    print("Чисел должно быть не меньше 3х")
else:
    width = int(data[0])
    height = int(data[1])
    cnt = int(data[2])
    match cnt % width:
        case 0:
            if cnt // width <= height:
                print("True")
            else:
                print("False")
        case _:
            print("False")

#Task 4
#3   -> III
#15  -> XV
#234 -> CCXXXIV
roman_digits = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
dig = input()
holidays = 0
result = []
if dig != "":
    dig = int(dig)
    if dig < 5000:
        for i,v in dict(reversed(roman_digits.items())).items():
            d = dig // i
            if d > 0:
                dig = dig - d*i
                for k in range(d):
                    result.append(v)
        print("".join(result))
    else:
        print("число должно быть меньше 5000")
else:
    print("вводить нужно число")


#Task 5
#5.6  -> True
#.78  -> True
#.67. -> False
#5    -> True
data = input()
coll_dot = 0
for i in data:
    if i == ".":
        if coll_dot != 0:
            print("False")
            break
        else:
            coll_dot += 1
    elif int(i) not in [1,2,3,4,5,6,7,8,9]:
        print("False")
else:
    print("True")
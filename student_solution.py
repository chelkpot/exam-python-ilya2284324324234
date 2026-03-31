# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    a="hellow,world"
    first,second =s.split(',')
    print(len(first)>len(second))
    print(first == second)
    print(second in first)
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
    ...

# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    s = input()
    print(s.strip())
    print(len(s))
    print(s.count('a'))
    print(s.replace('a', '@'))
    if s and s[0].isupper():
        print(True)
    else:
        print(False)

    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    ...

# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    s = input()
    if len(s) >= 2:
        print(s[1:-1])
    print(s[::2])
    print(s.lower()[::-1])
    # s а
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    ...

# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    number = input()
    s = list(map(int, number.split()))
    print(sorted(s))
    print(sum(s))
    print(min(s), max(s))
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    ...


# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    s = input()
    palindrome = (s.lower() == s[::-1].lower())
    no_space = (' ' not in s)
    print(palindrome and no_space)
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    ...

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    n = int(input())
    a = hex(n)[2:]
    print(a)
    print(len(a))
    print('a' in a)
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    ...

# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    a = int(input())
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    print(months[a - 1])
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
    ...

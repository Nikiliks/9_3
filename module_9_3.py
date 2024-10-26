# Cписки:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
# Создание генераторных сборок:
list_1 = list(zip(first, second))

first_result = (len(x) - len(y) for x, y in list_1 if len(x) != len(y))
print(list(first_result))

second_result = (len(first[x]) == len(second[y]) for x in range(3) for y in range(3) if x == y)
print(list(second_result))
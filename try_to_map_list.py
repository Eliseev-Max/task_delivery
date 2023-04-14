data = input("Введите первую тройку данных:\n")

handled_data = map(int, data.split())
print(tuple(handled_data))

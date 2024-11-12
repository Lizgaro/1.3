# Работа со словарём
my_dict = {
    "Vasya": 1975,
    "Egor": 1999,
    "Masha": 2002
}

# Выводим начальный словарь
print("Dict:", my_dict)

# Выводим значение по существующему ключу и по отсутствующему
existing_value = my_dict.get("Masha")  # Существующий ключ
not_existing_value = my_dict.get("Anna", None)  # Несуществующий ключ
print("Existing value:", existing_value)
print("Not existing value:", not_existing_value)

# Добавляем ещё две пары ключ-значение
my_dict["Kamila"] = 1981
my_dict["Artem"] = 1915

# Удаляем одну из пар по существующему ключу и выводим удалённое значение
deleted_value = my_dict.pop("Egor", None)
print("Deleted value:", deleted_value)

# Выводим изменённый словарь
print("Modified dictionary:", my_dict)

# Работа с множеством
my_set = {1, "Яблоко", 42.314, "Яблоко", 1}  # Множество с повторяющимися значениями

# Выводим множество с уникальными значениями
print("Set:", my_set)

# Добавляем два новых элемента
my_set.add(13)
my_set.add((5, 6, 1.6))

# Удаляем один элемент из множества
my_set.discard(1)

# Выводим изменённое множество
print("Modified set:", my_set)

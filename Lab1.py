name = "Іван"              # рядок (str)
age = 19                   # ціле число (int)
height = 1.75              # дійсне число (float)
is_student = True          # логічне значення (bool)
grades = [90, 85, 100]     # список (list)
info = {"group": "КН-23"}  # словник (dict)

# === Виведення змінних з типами ===
print("=== Змінні ===")
for n, v in {"name": name, "age": age, "height": height, "is_student": is_student, "grades": grades, "info": info}.items():
    print(f"{n}, {type(v).__name__} : {v}")  # вивід назви, типу та значення

# === Приклади операторів ===
print("\n=== Арифметичні оператори ===")
a, b = 10, 3
print(f"{a} + {b} = {a + b}")   # додавання
print(f"{a} - {b} = {a - b}")   # віднімання
print(f"{a} * {b} = {a * b}")   # множення
print(f"{a} / {b} = {a / b:.2f}") # ділення

print("\n=== Оператори порівняння ===")
print(f"{a} > {b} → {a > b}")   # більше
print(f"{a} == {b} → {a == b}") # рівність

print("\n=== Логічні оператори ===")
print(f"True and False → {True and False}")  # логічне І
print(f"True or False → {True or False}")    # логічне АБО
print(f"not True → {not True}")              # заперечення

print("\n=== Оператор присвоєння ===")
x = 5
x += 2  # додає 2 до змінної x (тепер x = 7)
print(f"x після x += 2 → {x}")
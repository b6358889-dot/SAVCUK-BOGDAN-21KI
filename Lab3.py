# === Створюємо порожній словник для збереження імен та оцінок ===
grades = {}

# === Введення даних користувачем ===
while True:
    name = input("Введіть ім'я студента (або 'stop' для завершення): ")
    if name.lower() == "stop":
        break  # зупиняємо цикл, якщо користувач ввів "stop"
    try:
        mark = int(input("Введіть оцінку (1-12): "))
        grades[name] = mark  # додаємо у словник
    except ValueError:
        print("Будь ласка, введіть число!")

# === Вивід усіх студентів та їх оцінок ===
print("\n=== Список студентів ===")
for name, mark in grades.items():
    print(f"{name} — {mark}")

# === Обчислення статистики ===
if grades:
    avg = sum(grades.values()) / len(grades)  # середній бал
    excellent = [n for n, m in grades.items() if 10 <= m <= 12]
    good = [n for n, m in grades.items() if 7 <= m <= 9]
    bad = [n for n, m in grades.items() if 4 <= m <= 6]
    failed = [n for n, m in grades.items() if 1 <= m <= 3]

    # === Вивід результатів ===
    print(f"\nСередній бал по групі: {avg:.2f}")
    print(f"Відмінники (10-12): {len(excellent)} — {excellent}")
    print(f"Хорошисти (7-9): {len(good)} — {good}")
    print(f"Відстаючі (4-6): {len(bad)} — {bad}")
    print(f"Не здали (1-3): {len(failed)} — {failed}")
else:
    print("\nДані не введено.")

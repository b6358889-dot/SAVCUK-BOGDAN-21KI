# 1 Функція для форматування ціни
def format_price(price):
    return f"ціна: {price:.2f} грн"   # округлює до 2 знаків після коми


# 2️ Функція, що перевіряє наявність товарів у магазині
def check_availability(*products):
    store = {"хліб": True, "молоко": True, "масло": False}  # наявні товари
    result = {}
    for p in products:
        result[p] = store.get(p, False)  # якщо товару немає в списку — False
    return result


# 3 Функція, що приймає замовлення користувача
def make_order():
    prices = {"хліб": 25.5, "молоко": 30.0, "масло": 80.0}  # ціни
    order = input("Введіть товари через кому: ").split(",")
    order = [o.strip() for o in order]  # прибираємо зайві пробіли

    availability = check_availability(*order)

    if all(availability.values()):  # якщо всі товари є
        total = sum(prices[p] for p in order)
        print("Усі товари є в наявності!")
        print(format_price(total))
    else:
        print("Деяких товарів немає в наявності:")
        for item, available in availability.items():
            if not available:
                print(f" - {item}")


# 🔹 Основна частина програми
if __name__ == "__main__":
    make_order()

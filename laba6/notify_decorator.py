def notify(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Готово!")
        return result
    return wrapper

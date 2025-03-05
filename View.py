
class CalculatorView:
    def display_menu(self):
        print("\n--- Калькулятор Menu ---")
        print("1. Сложение(+)")
        print("2. Вычитание(-)")
        print("3. Произведение(*)")
        print("4. Деление(÷)")
        print("5. Выход")

    def get_operation_choice(self):
        return input("Выбери действия,и напиши цифру (1-5): ")

    def get_numbers(self):
        try:
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
            return a, b
        except ValueError:
            raise ValueError("Напиши просто число  1-5")

    def display_result(self, result):
        print(f"Результат: {result}")

    def display_error(self, message):
        print(f"Ошибка!: {message}")
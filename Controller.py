from Model import *
from View import  *
class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView()

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_operation_choice()

            if choice == "5":
                print("Выход с калькулятора,Прощай!")
                break

            try:
                a, b = self.view.get_numbers()

                if choice == "1":
                    result = self.model.add(a, b)
                elif choice == "2":
                    result = self.model.subtract(a, b)
                elif choice == "3":
                    result = self.model.multiply(a, b)
                elif choice == "4":
                    result = self.model.divide(a, b)
                else:
                    self.view.display_error("Выбери и напиши число с 1-5!")
                    continue

                self.view.display_result(result)

            except ValueError as e:
                self.view.display_error(str(e))
            except Exception as e:
                self.view.display_error(f"Произошла непредвиденная ошибка!: {e}")
if __name__ == '__main__':

    if __name__ == "__main__":
            calculator = CalculatorController()
            calculator.run()
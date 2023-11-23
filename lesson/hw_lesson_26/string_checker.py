class StringChecker:
    def __init__(self):
        self.is_number = lambda s: s.replace('.', '', 1).isdigit() if s.count('.') <= 1 else False

    def check_if_number(self, input_str):
        return self.is_number(input_str)


# Приклад використання
checker = StringChecker()

while True:
    input_string = input("Введіть рядок (або введіть 'exit' для виходу): ")

    if input_string.lower() == 'exit':
        print("Програма завершена.")
        break

    if checker.check_if_number(input_string):
        print(f'"{input_string}" є числом.')
    else:
        print(f'"{input_string}" не є числом.')

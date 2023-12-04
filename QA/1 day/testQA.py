import subprocess
import os

def normalize_line_endings_and_whitespace(text):
    # Remove leading spaces and normalize line endings
    lines = [line.lstrip() for line in text.splitlines()]
    return '\n'.join(lines)

def run_code(input_file, expected_output_file, code_file):
    # Чтение входных данных
    with open(input_file, 'r') as file:
        input_data = file.read()

    # Чтение ожидаемого результата
    with open(expected_output_file, 'r') as file:
        expected_output = file.read()

    # Исполнение кода
    try:
        result = subprocess.run(['python', code_file], input=input_data, text=True, capture_output=True, timeout=5)
    except subprocess.TimeoutExpired:
        print('Ошибка: Превышено время выполнения кода')
        return

    # Получение вывода
    actual_output = result.stdout

    # Нормализация концов строк и удаление ведущих пробелов
    expected_output = normalize_line_endings_and_whitespace(expected_output)
    actual_output = normalize_line_endings_and_whitespace(actual_output)

    # Сравнение результатов
    if actual_output == expected_output:
        print('Код выполнился корректно. Результат совпадает.')
    else:
        print('Ошибка: Результат не совпадает. Ожидалось:\n', expected_output)
        print('Получено:\n', actual_output)

# Пример использования
run_code('test.txt', 'answer.txt', 'xx.py')

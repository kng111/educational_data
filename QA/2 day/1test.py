def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
        print('_')
    except AssertionError:
        print(f"expected {expected_result}, got {actual_result}")

# Пример использования:

# Тест 1
test_input_text(8, 11)

# Тест 2
test_input_text(11, 11)

# Тест 3
test_input_text(11, 15)

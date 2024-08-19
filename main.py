# Импорт необходимых библиотек и файлов
from code_generator import *
if __name__ == "__main__":
    # Входная программа
    input_program = "x := 10.5; y := (x * 2) + 3.14"
    # Вызов парсера для анализа и обработки входного программного кода
    # Результатом будет дерево разбора, представляющее структуру программы
    parsed_tree = parser.parse(input_program)
    print("parsed_tree: ", parsed_tree)
    # Вызов семантического анализатора
    # Проверка семантической корректности программы

    semantic_a=semantic_analysis(parsed_tree)
    print("semantic_analysis: ", semantic_a)
    # Вызов функции, которая преобразует дерево разбора в промежуточный код
    intermediate_code = generate_intermediate_code(parsed_tree)
    print("intermediate_code:",intermediate_code)
    # Вызов функции, которая преобразует промежуточный код в целевой код
    target_code = generate_target_code(intermediate_code)
    print("target_code:",target_code)
    # Вызов функции,  которая сохраняет целевой код в файле
    save_target_code(target_code, "output_code.txt")

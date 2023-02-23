def arithmetic_arranger(problems, show_answers=False):
    # Verificar si hay demasiados problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    # Inicializar variables
    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""

    # Procesar cada problema
    for problem in problems:
        # Separar los operandos y el operador
        operand1, operator, operand2 = problem.split()

        # Verificar si el operador es válido
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        # Verificar si los operandos son números de máximo 4 dígitos
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Convertir los operandos a números enteros
        operand1 = int(operand1)
        operand2 = int(operand2)

        # Calcular el resultado
        if operator == "+":
            result = operand1 + operand2
        else:
            result = operand1 - operand2

        # Crear las líneas del problema
        width = max(len(str(operand1)), len(str(operand2))) + 2
        first_line += str(operand1).rjust(width) + "    "
        second_line += operator + str(operand2).rjust(width - 1) + "    "
        dash_line += "-" * width + "    "
        result_line += str(result).rjust(width) + "    "

    # Concatenar las líneas del problema
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip()
    if show_answers:
        arranged_problems += "\n" + result_line.rstrip()

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(" ")
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
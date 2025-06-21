def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges arithmetic problems (addition and subtraction) in a vertical format.

    Parameters:
    problems (list): A list of strings, where each string is an arithmetic problem (e.g., "32 + 8").
    show_answers (bool): If True, includes the answers in the formatted output.

    Returns:
    str: A string that represents the formatted arithmetic problems or an error message.
    """

    # Check if there are more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Lists to store each component of the formatted output
    top_line_parts = []     # First operands
    bottom_line_parts = []  # Operators and second operands
    dash_line_parts = []    # Dashes separating problems
    answer_line_parts = []  # Answers (optional)

    # Process each arithmetic problem
    for problem in problems:
        # Split the problem into parts
        parts = problem.split()

        # Ensure the problem is correctly formatted with 3 parts
        if len(parts) != 3:
            return "Error: Problem format incorrect. Expected 'NUMBER OPERATOR NUMBER'."

        first, operator, second = parts  # Unpack into variables

        # Validate the operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Validate that both operands contain only digits
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        # Ensure operands are no more than four digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width of the formatted problem (longer operand + 2 for spacing and operator)
        width = max(len(first), len(second)) + 2

        # Format and store each line of the problem
        top_line_parts.append(first.rjust(width))
        bottom_line_parts.append(operator + second.rjust(width - 1))
        dash_line_parts.append('-' * width)

        # If answers should be shown, calculate and format the answer
        if show_answers:
            if operator == '+':
                answer = str(int(first) + int(second))
            else:
                answer = str(int(first) - int(second))
            answer_line_parts.append(answer.rjust(width))

    # Construct the final arranged output by joining the formatted parts with 4 spaces
    arranged_problems = "    ".join(top_line_parts) + "\n"
    arranged_problems += "    ".join(bottom_line_parts) + "\n"
    arranged_problems += "    ".join(dash_line_parts)

    # Add the answer line if requested
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line_parts)

    return arranged_problems

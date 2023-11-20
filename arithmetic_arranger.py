def arithmetic_arranger(problems, display_answers=False):
  # Check if the number of problems is more than the allowed limit
  if len(problems) > 5:
    return "Error: Too many problems."

  # Initialize strings to hold each line of the output
  first_line = ""
  second_line = ""
  dashes = ""
  answers = ""

  # Process each arithmetic problem in the list
  for problem in problems:
    parts = problem.split()  # Split the problem into its components
    operand1, operator, operand2 = parts[0], parts[1], parts[2]

    # Check if the operator is either addition or subtraction
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    # Check if both operands are digits
    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    # Check if operands are within the length limit
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Determine the length of the longest operand for formatting
    length = max(len(operand1), len(operand2)) + 2

    # Format the operands and the operator
    top = operand1.rjust(length)
    bottom = operator + operand2.rjust(length - 1)
    line = '-' * length
    answer = str(eval(problem)).rjust(length)

    # Add appropriate spacing between problems
    if problem != problems[0]:
      first_line += "    "
      second_line += "    "
      dashes += "    "
      answers += "    "

    # Append the current problem's lines to the overall output
    first_line += top
    second_line += bottom
    dashes += line
    answers += answer

  # Format the final output based on whether answers are to be displayed
  if display_answers:
    arranged_problems = f"{first_line}\n{second_line}\n{dashes}\n{answers}"
  else:
    arranged_problems = f"{first_line}\n{second_line}\n{dashes}"

  # Return the formatted string
  return arranged_problems

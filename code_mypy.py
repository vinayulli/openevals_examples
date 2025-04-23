from openevals.code.mypy import create_mypy_evaluator

evaluator = create_mypy_evaluator()

CODE = """
def sum_of_two_numbers(a, b): return a+b
"""

result = evaluator(outputs=CODE)

print(result)
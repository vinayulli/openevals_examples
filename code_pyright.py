from openevals.code.pyright import create_pyright_evaluator

evaluator = create_pyright_evaluator()
CODE = """
def sum_of_two_numbers(a, b): return a + b
"""
result = evaluator(outputs=CODE)
print(result)
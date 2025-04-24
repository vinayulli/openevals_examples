from openevals.code.mypy import create_mypy_evaluator

evaluator = create_mypy_evaluator(

      mypy_cli_args=[
        "--no-incremental",
        "--strict",
        "--ignore-missing-imports",
    ]
)

CODE = """
def sum_of_two_numbers(a: int, b: int) -> int:
    return a + b + c
"""

result = evaluator(outputs=CODE)

print(result)
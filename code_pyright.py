from openevals.code.pyright import create_pyright_evaluator


# test case 1 
evaluator = create_pyright_evaluator()
CODE = """
def sum_of_two_numbers(a, b): return a + b
"""
result = evaluator(outputs=CODE)
print("test case 1", result)

# test case 2 

CODE = """
def sum_of_two_numbers(a, b): return a + b + c
"""
result = evaluator(outputs=CODE)
print("test case 2", result) 

# test case 3 
CODE = """
def greet(name: str) -> int:
    return f"Hello, {name}!"  
"""
result = evaluator(outputs=CODE)
print("test case 3", result)
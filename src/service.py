from .calculator import add, multiply


def calculate(operation: str, a: int, b: int) -> int:
    if operation == "add":
        return add(a, b)

    if operation == "multiply":
        return multiply(a, b)

    raise ValueError(f"Unsupported operation: {operation}")

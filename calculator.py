#!/usr/bin/env python3
"""
Basic Calculator Program
- Prompts for two numbers and an operator: +, -, *, /
- Performs the operation and prints: a op b = result
- Includes simple validation and division-by-zero protection
"""

def to_number(s: str) -> float:
    """Convert input string to float; raise ValueError if invalid."""
    try:
        return float(s)
    except ValueError as exc:
        raise ValueError("Please enter a valid number.") from exc

def fmt(n: float) -> str:
    """Pretty-print numbers (avoid trailing .0 for whole values)."""
    return str(int(n)) if isinstance(n, float) and n.is_integer() else str(n)

def calculate(a: float, b: float, op: str) -> float:
    """Return the result of applying op to a and b."""
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    raise ValueError("Unsupported operation. Use one of +, -, *, /.")

def main() -> None:
    print("=== Basic Calculator ===")
    try:
        a = to_number(input("Enter first number: ").strip())
        b = to_number(input("Enter second number: ").strip())
        op = input("Choose operation (+, -, *, /): ").strip()

        result = calculate(a, b, op)
        print(f"\n{fmt(a)} {op} {fmt(b)} = {fmt(result)}")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    
    try:
        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid expression"

print(calculator.invoke({
    "expression": "10 + 20 * 5"
}))
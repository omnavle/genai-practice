from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

result = add_numbers.invoke({
    "a": 10,
    "b": 20
})

print(result)
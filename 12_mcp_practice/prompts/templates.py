from mcp.server.fastmcp import FastMCP


def register_prompts(mcp: FastMCP):

    @mcp.prompt()
    def explain_code(code: str) -> str:
        """Create a prompt for explaining code."""

        return f"""
You are an experienced software engineer.

Explain the following code in simple terms.

Code:

{code}

Include:

1. What the code does
2. How it works
3. Important functions
4. Possible issues
5. Suggestions for improvement
"""


    @mcp.prompt()
    def summarize_document(document: str) -> str:
        """Create a prompt for summarizing a document."""

        return f"""
You are an AI assistant.

Summarize the following document.

Document:

{document}

Provide:

1. Short summary
2. Important points
3. Key information
4. Final conclusion
"""


    @mcp.prompt()
    def review_code(code: str) -> str:
        """Create a prompt for reviewing code."""

        return f"""
You are a senior software engineer.

Review the following code:

{code}

Check for:

- Bugs
- Security problems
- Performance issues
- Code quality
- Best practices

Then provide improved suggestions.
"""
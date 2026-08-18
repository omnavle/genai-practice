from pathlib import Path

def list_files(directory: str = ".") -> list[str]:
    """List files and folders inside a directory"""
    path = Path(directory)

    if not path.exists():
        raise FileNotFoundError(
            f"Directory not found: {directory}"
        )
    
    return [
        item.name
        for item in path.iterdir()
    ]
    
def read_file(file_path: str) -> str:
    """Read the contents of a text file"""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )
    
    if not path.is_file():
        raise ValueError(
            f"Path is not a file: {file_path}"
        )
        
    return path.read_text(
        encoding="utf-8"
    )
    
def write_file(
    file_path: str,
    content: str
) -> str:
    """Write text content to a file."""

    path = Path(file_path)

    path.write_text(
        content,
        encoding="utf-8"
    )
    
    return f"File written successfully: {file_path}"
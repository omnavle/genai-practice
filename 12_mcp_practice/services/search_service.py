from pathlib import Path


DOCUMENTS_DIR = Path("documents")


def list_documents() -> list[str]:
    """Return all text documents."""

    if not DOCUMENTS_DIR.exists():
        DOCUMENTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    return [
        file.name
        for file in DOCUMENTS_DIR.iterdir()
        if file.is_file()
    ]


def read_document(filename: str) -> str:
    """Read a document."""

    file_path = DOCUMENTS_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Document not found: {filename}"
        )

    if not file_path.is_file():
        raise ValueError(
            f"Not a file: {filename}"
        )

    return file_path.read_text(
        encoding="utf-8"
    )


def save_document(
    filename: str,
    content: str
) -> str:
    """Save a document."""

    DOCUMENTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = DOCUMENTS_DIR / filename

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    return f"Document saved: {filename}"
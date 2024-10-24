from pathlib import Path


def load_text(f: str | Path) -> str:
    with open(f) as fp:
        return fp.read()


def save_text(text: str, f: str | Path) -> None:
    with open(f, "w") as fp:
        fp.write(text)

from pathlib import Path

from markdownify import markdownify as md


def main() -> None:
    path = Path("guide/gpt4-1_prompting_guide.html")
    encoding = "utf-8"

    html = path.open(encoding=encoding).read()
    markdown = md(html, strip=["a", "img"])

    path.with_suffix(".md").write_text(markdown, encoding=encoding)


if __name__ == "__main__":
    main()

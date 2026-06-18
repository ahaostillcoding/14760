from pathlib import Path
import subprocess
import tempfile


REPO = Path(__file__).resolve().parent
PAGES = [REPO / "index.html"] + sorted((REPO / "briefs").glob("*.html"))


def extract_babel_script(text: str) -> tuple[str, int, int]:
    start_marker = '<script type="text/babel">'
    start = text.index(start_marker)
    content_start = start + len(start_marker)
    end = text.index("</script>", content_start)
    return text[content_start:end], start, end + len("</script>")


def compile_jsx(source: str) -> str:
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "page.jsx"
        out = Path(tmpdir) / "page.js"
        src.write_text(source, encoding="utf-8", newline="\n")
        subprocess.run(
            [
                "npx.cmd",
                "esbuild",
                str(src),
                "--loader:.jsx=jsx",
                "--format=iife",
                "--outfile=" + str(out),
            ],
            check=True,
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        return out.read_text(encoding="utf-8")


def process_page(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    jsx, start, end = extract_babel_script(text)
    compiled = compile_jsx(jsx)
    compiled_tag = "<script>\n" + compiled.strip() + "\n    </script>"
    text = text[:start] + compiled_tag + text[end:]
    text = text.replace(
        '<script crossorigin src="https://unpkg.com/@babel/standalone/babel.min.js"></script>\n',
        "",
    )
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"compiled {path.relative_to(REPO).as_posix()}")


def main() -> None:
    for page in PAGES:
        process_page(page)


if __name__ == "__main__":
    main()

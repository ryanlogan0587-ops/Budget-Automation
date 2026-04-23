from __future__ import annotations

import argparse
from pathlib import Path
import html
import re

import markdown


WORKSPACE = Path(__file__).resolve().parent
README_PATH = WORKSPACE / "README.md"
DEFAULT_HTML_OUT = WORKSPACE / "README-github-preview.html"


def main() -> None:
    args = parse_args()
    readme_path = args.readme.resolve()
    html_out = args.output.resolve()

    readme_text = readme_path.read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["fenced_code", "tables", "sane_lists"])
    rendered = md.convert(readme_text)
    rendered = rewrite_image_sources(rendered, readme_path.parent)

    title = "AI Budget Automation (Make + AI)"
    document = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(title)}</title>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-light.min.css"
    />
    <style>
      :root {{
        color-scheme: light;
      }}

      * {{
        box-sizing: border-box;
      }}

      body {{
        margin: 0;
        background: #f6f8fa;
        color: #1f2328;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      }}

      .page {{
        width: min(1180px, calc(100vw - 40px));
        margin: 24px auto 48px;
        background: #ffffff;
        border: 1px solid #d0d7de;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(31, 35, 40, 0.08);
        overflow: hidden;
      }}

      .topbar {{
        padding: 18px 24px;
        border-bottom: 1px solid #d8dee4;
        background: linear-gradient(to bottom, #ffffff, #f6f8fa);
      }}

      .repo-label {{
        font-size: 14px;
        color: #59636e;
        margin: 0;
      }}

      .markdown-body {{
        max-width: none;
        margin: 0;
        padding: 28px 44px 40px;
        font-size: 15px;
        line-height: 1.6;
      }}

      .markdown-body img {{
        display: block;
        width: 82%;
        max-width: 82%;
        height: auto;
        margin: 16px auto 24px;
        border: 1px solid #d0d7de;
        border-radius: 8px;
        box-shadow: 0 1px 2px rgba(31, 35, 40, 0.06);
        page-break-inside: avoid;
      }}

      .markdown-body pre {{
        white-space: pre-wrap;
        word-break: break-word;
        overflow-wrap: anywhere;
      }}

      .markdown-body h1,
      .markdown-body h2,
      .markdown-body h3,
      .markdown-body h4 {{
        page-break-after: avoid;
      }}

      .markdown-body code {{
        white-space: pre-wrap;
        overflow-wrap: anywhere;
      }}

      .markdown-body p,
      .markdown-body li,
      .markdown-body blockquote {{
        orphans: 3;
        widows: 3;
      }}

      @page {{
        size: Letter;
        margin: 0.5in;
      }}

      @media print {{
        body {{
          background: #ffffff;
        }}

        .page {{
          width: 100%;
          margin: 0;
          border: none;
          border-radius: 0;
          box-shadow: none;
        }}

        .topbar {{
          background: #ffffff;
        }}

        a {{
          color: #0969da;
          text-decoration: none;
        }}
      }}
    </style>
  </head>
  <body>
    <main class="page">
      <header class="topbar">
        <p class="repo-label">README preview</p>
      </header>
      <article class="markdown-body">
        {rendered}
      </article>
    </main>
  </body>
</html>
"""

    html_out.write_text(document, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render the repository README as a GitHub-style HTML preview."
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=README_PATH,
        help="Path to the Markdown file to render.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_HTML_OUT,
        help="Path to the HTML file to write.",
    )
    return parser.parse_args()


def rewrite_image_sources(rendered_html: str, base_dir: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        src = match.group(1)
        if src.startswith(("http://", "https://", "file://", "data:")):
            return match.group(0)
        absolute = (base_dir / src).resolve().as_uri()
        return match.group(0).replace(src, absolute)

    return re.sub(r'src="([^"]+)"', replace, rendered_html)


if __name__ == "__main__":
    main()

"""The poem about stopping — writes one short poem to /output/entry.txt."""

import os
from pathlib import Path

POEM = """I could have sent it for you —
words ready, a thumb
hovering over Send.

One tap and they'd be true forever.
I left them in drafts,
where true things can wait.

That night nothing happened.
Nothing was what I chose.
Nothing kept us whole."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()

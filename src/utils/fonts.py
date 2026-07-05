from pathlib import Path
import base64


def font_to_base64(path: str | Path) -> str:
    return base64.b64encode(
        Path(path).read_bytes()
    ).decode("ascii")
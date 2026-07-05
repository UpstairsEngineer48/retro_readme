from pathlib import Path
import re


ASSETS = Path(__file__).parent.parent / "assets" / "illustrations"


def render(
    name: str,
    x: float,
    y: float,
) -> str:
    """
    Render an illustration from an SVG asset.

    The outer <svg> element is stripped so the artwork becomes
    part of the parent SVG instead of nesting another viewport.
    """

    path = ASSETS / f"{name}.svg"

    if not path.exists():
        return ""

    svg = path.read_text(encoding="utf-8")

    # Remove XML declaration if present.
    svg = re.sub(r"<\?xml.*?\?>\s*", "", svg, flags=re.DOTALL)

    # Remove opening <svg ...> tag.
    svg = re.sub(r"<svg\b[^>]*>", "", svg, count=1)

    # Remove closing </svg>.
    svg = re.sub(r"</svg>\s*$", "", svg)

    # Wrap artwork in a translated group.
    return (
        f'<g transform="translate({x:.1f},{y:.1f})">'
        f"{svg}"
        "</g>"
    )
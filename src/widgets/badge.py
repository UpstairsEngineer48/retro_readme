from ..icons import render as render_icon
from ..utils.svg import group, text


def render(
    icon: str,
    title: str,
    x: int,
    y: int,
) -> str:
    """
    Render a single achievement badge.
    """

    return group(

        render_icon(
            icon,
            x,
            y - 12,
        ),

        text(
            x + 28,
            y,
            title,
            font_family="PixelOperator",
            font_size=18,
            fill="#243000",
        ),
    )
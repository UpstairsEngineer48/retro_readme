from ..utils.svg import group, text


def render(
    title: str,
    x: int,
    y: int,
) -> str:
    """
    Render a section heading.
    """

    return group(
        text(
            x,
            y,
            title,
            font_family="PixelOperator",
            font_size=20,
            font_weight="bold",
            fill="#243000",
        ),
    )
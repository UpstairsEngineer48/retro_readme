from ..utils.svg import group, text


def render(
    label: str,
    value: str,
    x: int,
    y: int,
) -> str:
    """
    Render a label/value pair.
    """

    return group(

        text(
            x,
            y,
            label,
            font_family="PixelOperator",
            font_size=18,
            fill="#243000",
        ),

        text(
            x + 110,
            y,
            value,
            font_family="PixelOperator",
            font_size=18,
            fill="#243000",
        ),
    )
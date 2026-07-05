from ..utils.svg import group, line, text


def render(
    title: str,
    subtitle: str,
    description: str,
    x: int,
    y: int,
    width: int,
) -> str:
    """
    Render a project card.
    """

    return group(

        text(
            x,
            y,
            title,
            font_family="PixelOperator",
            font_size=18,
            font_weight="bold",
            fill="#243000",
        ),

        text(
            x,
            y + 18,
            subtitle,
            font_family="PixelOperator",
            font_size=15,
            fill="#243000",
        ),

        text(
            x,
            y + 36,
            description,
            font_family="PixelOperator",
            font_size=14,
            fill="#243000",
        ),

        line(
            x,
            y + 48,
            x + width,
            y + 48,
            stroke="#243000",
            stroke_width=1,
        ),
    )
from ..utils.svg import circle, group, line, text


def render(
    year: str,
    title: str,
    x: int,
    y: int,
) -> str:
    """
    Render a single timeline milestone.
    """

    return group(

        # Timeline node
        circle(
            x,
            y,
            3,
            fill="#243000",
        ),

        # Connector
        line(
            x,
            y,
            x + 12,
            y,
            stroke="#243000",
            stroke_width=2,
        ),

        # Year
        text(
            x + 18,
            y + 4,
            year,
            font_family="PixelOperator",
            font_size=16,
            fill="#243000",
        ),

        # Event
        text(
            x + 70,
            y + 4,
            title,
            font_family="PixelOperator",
            font_size=16,
            fill="#243000",
        ),
    )
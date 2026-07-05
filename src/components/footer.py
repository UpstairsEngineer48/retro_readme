from ..layout import LayoutEngine
from ..utils.svg import group, rect, text


def render() -> str:
    """
    Render the LCD footer help box.
    """

    layout = LayoutEngine()
    footer = layout.footer()

    center = footer.x + footer.width // 2

    return group(

        rect(
            footer.x,
            footer.y,
            footer.width,
            footer.height,
            rx=4,
            ry=4,
            fill="none",
            stroke="#526600",
            stroke_width=2,
        ),

        text(
            footer.x + footer.width * 0.25,
            footer.y + 22,
            "A: SELECT",
            text_anchor="middle",
            font_family="PixelOperator",
            font_size=18,
            fill="#243000",
        ),

        text(
            footer.x + footer.width * 0.75,
            footer.y + 22,
            "B: BACK",
            text_anchor="middle",
            font_family="PixelOperator",
            font_size=18,
            fill="#243000",
        ),
        id="footer",
    )
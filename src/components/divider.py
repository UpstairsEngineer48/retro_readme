from ..layout import LayoutEngine
from ..utils.svg import group, line, text


def render() -> str:
    """
    Render the divider with the version label.
    """

    layout = LayoutEngine()
    lcd = layout.lcd()

    y = lcd.y + 112

    center = lcd.x + lcd.width // 2

    gap = 42  # Half-width reserved for the version text

    return group(

        # Left divider
        line(
            lcd.x + 20,
            y,
            center - gap,
            y,
            stroke="#526600",
            stroke_width=2,
        ),

        # Version
        text(
            center,
            y + 5,
            "v1.0.0",
            text_anchor="middle",
            font_family="PixelOperator",
            font_size=14,
            fill="#243000",
        ),

        # Right divider
        line(
            center + gap,
            y,
            lcd.x + lcd.width - 20,
            y,
            stroke="#526600",
            stroke_width=2,
        ),

        id="divider",
    )
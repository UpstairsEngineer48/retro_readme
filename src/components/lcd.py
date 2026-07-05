from ..layout import LayoutEngine
from ..utils.svg import group, rect


def render() -> str:
    """
    Render the LCD display.
    """

    layout = LayoutEngine()
    lcd = layout.lcd()

    return group(
        rect(
            lcd.x,
            lcd.y,
            lcd.width,
            lcd.height,
            rx=10,
            ry=10,
            fill="#A6BC00",
            stroke="#6F7E20",
            stroke_width=2,
        ),
        id="lcd",
    )
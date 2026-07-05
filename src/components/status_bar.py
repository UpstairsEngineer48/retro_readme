from ..layout import LayoutEngine
from ..models import StatusBar
from ..utils.svg import group, rect, text


def render(status: StatusBar) -> str:
    """
    Render the LCD status row.
    """

    layout = LayoutEngine()
    lcd = layout.lcd()

    y = lcd.y + 18

    # Battery fill width (0–14 px)
    fill_width = max(
        0,
        min(
            14,
            round(status.battery_level * 14 / 100),
        ),
    )

    return group(

        # Time
        text(
            lcd.x + 12,
            y,
            status.time,
            font_family="PixelOperator",
            font_size=14,
            fill="#243000",
        ),

        # Battery outline
        rect(
            lcd.x + lcd.width - 36,
            lcd.y + 8,
            20,
            10,
            fill="none",
            stroke="#243000",
            stroke_width=1,
        ),

        # Battery terminal
        rect(
            lcd.x + lcd.width - 16,
            lcd.y + 11,
            2,
            4,
            fill="#243000",
        ),

        # Battery fill
        rect(
            lcd.x + lcd.width - 34,
            lcd.y + 10,
            fill_width,
            6,
            fill="#243000",
        ),

        id="status-row",
    )
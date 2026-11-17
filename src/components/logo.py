from ..layout import LayoutEngine
from ..utils.svg import group, text


def render() -> str:
    layout = LayoutEngine()
    lcd = layout.lcd()

    center = lcd.x + lcd.width // 2

    return group(

        text(
            center,
            lcd.y + 72,
            "UPSTAIRS OS",
            text_anchor="middle",
            font_family="PixelOperator",
            font_size=34,
            font_weight="bold",
            fill="#243000",
        ),

        id="logo",
    )

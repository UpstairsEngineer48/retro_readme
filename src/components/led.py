from ..layout import LayoutEngine
from ..utils.svg import circle, group


def render() -> str:
    """
    Render the power LED.
    """

    layout = LayoutEngine()
    led = layout.led_position()

    return group(
        # Outer ring
        circle(
            led.x,
            led.y,
            12,
            fill="#1A1A1A",
        ),

        # LED
        circle(
            led.x,
            led.y,
            9,
            fill="#3BFF6A",
        ),

        id="power-led",
    )
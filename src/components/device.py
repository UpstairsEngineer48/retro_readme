from ..layout import LayoutEngine
from ..utils.svg import group, rect


def render() -> str:
    """
    Render the handheld shell.
    """

    layout = LayoutEngine()

    device = layout.device()
    bezel = layout.inner_bezel()

    return group(
        # Outer shell
        rect(
            device.x,
            device.y,
            device.width,
            device.height,
            rx=36,
            ry=36,
            fill="#3C3C42",
            stroke="#1D1D22",
            stroke_width=5,
        ),

        # Inner shell
        rect(
            bezel.x,
            bezel.y,
            bezel.width,
            bezel.height,
            rx=28,
            ry=28,
            fill="#2E2E35",
            stroke="#505058",
            stroke_width=2,
        ),

        # LCD opening
        rect(
            layout.lcd().x - 10,
            layout.lcd().y - 10,
            layout.lcd().width + 20,
            layout.lcd().height + 20,
            rx=16,
            ry=16,
            fill="#4D4D53",
        ),

        id="device",
    )
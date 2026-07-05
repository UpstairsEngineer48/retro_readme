from ..layout import LayoutEngine
from ..utils.svg import group, rect


def render() -> str:
    """
    Render the top speaker grille.
    """

    layout = LayoutEngine()
    speaker = layout.speaker_area()

    slots = []

    slot_width = 18
    slot_height = 4
    gap = 8

    start_x = speaker.x
    y = speaker.y

    for i in range(8):
        slots.append(
            rect(
                start_x + i * (slot_width + gap),
                y,
                slot_width,
                slot_height,
                rx=2,
                ry=2,
                fill="#1B1B20",
            )
        )
    for i in range(8):
        slots.append(
            rect(
                start_x + i * (slot_width + gap),
                y+5,
                slot_width,
                slot_height,
                rx=2,
                ry=2,
                fill="#1B1B20",
            )
        )
    return group(
        *slots,
        id="speaker",
    )
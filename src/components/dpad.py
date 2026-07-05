from ..layout import LayoutEngine
from ..utils.svg import group, rect, link
from ..state import AppState
from ..config import BASE_URL


def _button(x, y, href, pressed=False):

    size = 34

    dx = 2 if pressed else 0
    dy = 2 if pressed else 0

    return link(
        href,
        group(
            # Shadow
            rect(
                x + 3,
                y + 3,
                size,
                size,
                rx=8,
                ry=8,
                fill="#17181C",
            ),

            # Outer shell
            rect(
                x + dx,
                y + dy,
                size,
                size,
                rx=8,
                ry=8,
                fill="#3B3E45",
                stroke="#111215",
                stroke_width=2,
            ),

            # Face
            rect(
                x + 3 + dx,
                y + 3 + dy,
                size - 6,
                size - 6,
                rx=6,
                ry=6,
                fill="#595D66",
            ),

            # Top highlight
            rect(
                x + 5 + dx,
                y + 5 + dy,
                size - 10,
                3,
                rx=1,
                fill="#666A72" if pressed else "#8A8E96",
            ),

            # Left highlight
            rect(
                x + 5 + dx,
                y + 5 + dy,
                3,
                size - 10,
                rx=1,
                fill="#666A72" if pressed else "#8A8E96",
            ),
        ),
    )


def render(state: AppState) -> str:

    layout = LayoutEngine()
    area = layout.dpad_area()

    size = 34
    gap = 10

    cx = area.x + area.width // 2
    cy = area.y + area.height // 2

    up_x = cx - size // 2
    up_y = cy - gap - size

    down_x = cx - size // 2
    down_y = cy + gap

    left_x = cx - gap - size
    left_y = cy - size // 2

    right_x = cx + gap
    right_y = cy - size // 2

    up = _button(
        up_x,
        up_y,
        f"{BASE_URL}/input?btn=UP&return_to=vercel",
        state.pressed == "UP",
    )

    down = _button(
        down_x,
        down_y,
        f"{BASE_URL}/input?btn=DOWN&return_to=vercel",
        state.pressed == "DOWN",
    )

    left = _button(
        left_x,
        left_y,
        f"{BASE_URL}/input?btn=LEFT&return_to=vercel",
        state.pressed == "LEFT",
    )

    right = _button(
        right_x,
        right_y,
        f"{BASE_URL}/input?btn=RIGHT&return_to=vercel",
        state.pressed == "RIGHT",
    )

    return group(
        up,
        down,
        left,
        right,
        id="dpad",
    )

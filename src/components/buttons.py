from ..layout import LayoutEngine
from ..utils.svg import group, circle, text, link
from ..state import AppState
from ..config import BASE_URL


def _button(cx, cy, label, href, pressed=False):

    outer_r = 24
    inner_r = 19

    dx = 2 if pressed else 0
    dy = 2 if pressed else 0

    return link(
        href,
        group(
            # Shadow
            circle(
                cx + 3,
                cy + 3,
                outer_r,
                fill="#18191D",
            ),

            # Outer shell
            circle(
                cx + dx,
                cy + dy,
                outer_r,
                fill="#3E4047",
                stroke="#111215",
                stroke_width=2,
            ),

            # Button face
            circle(
                cx + dx,
                cy + dy,
                inner_r,
                fill="#575A62",
            ),

            # Highlight
            circle(
                cx - 7 + dx,
                cy - 7 + dy,
                5,
                fill="#666A72" if pressed else "#868991",
            ),

            # Letter
            text(
                cx + dx,
                cy + 6 + dy,
                label,
                font_family="PixelOperator",
                font_size=22,
                fill="#D8E89A",
                text_anchor="middle",
            ),
        ),
    )


def render(state: AppState) -> str:

    layout = LayoutEngine()
    area = layout.buttons_area()

    ax = area.x + 90
    ay = area.y + 16

    bx = area.x + 34
    by = area.y + 62

    a_button = _button(
        ax,
        ay,
        "A",
        f"{BASE_URL}/input?btn=A&s={state.current_screen}&p={state.current_page}&m={state.menu_selection}",
        state.pressed == "A",
    )

    b_button = _button(
        bx,
        by,
        "B",
        f"{BASE_URL}/input?btn=B&s={state.current_screen}&p={state.current_page}&m={state.menu_selection}",
        state.pressed == "B",
    )

    return group(
        a_button,
        b_button,
        id="buttons",
    )

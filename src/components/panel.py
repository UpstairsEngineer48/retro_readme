from ..illustrations import render as render_illustration
from ..layout import LayoutEngine
from ..state import AppState
from ..utils.svg import group, rect, line, text


PANEL_WIDTH = 480
PANEL_HEIGHT = 820

HEADER_HEIGHT = 60
ILLUSTRATION_HEIGHT = 250
DESCRIPTION_HEIGHT = 170
PAGE_HEIGHT = 170


def render(
    data: dict,
    state: AppState,
) -> str:
    """
    Render the right-side information panel.
    """

    layout = LayoutEngine()

    x = layout.device().x + layout.device().width + 50
    y = 40

    children = []

    panel = data["panel"]

    if data["type"] == "menu":
        current = panel["pages"][state.menu_selection]
    else:
        current = panel["pages"][state.current_page]

    # ---------------------------------------------------------
    # Outer frame
    # ---------------------------------------------------------

    children.append(
        rect(
            x,
            y,
            PANEL_WIDTH,
            PANEL_HEIGHT,
            rx=18,
            ry=18,
            fill="#2F2F35",
            stroke="#17181C",
            stroke_width=4,
        )
    )

    # ---------------------------------------------------------
    # Inner frame
    # ---------------------------------------------------------

    padding = 18

    inner_x = x + padding
    inner_y = y + padding
    inner_width = PANEL_WIDTH - padding * 2

    children.append(
        rect(
            inner_x,
            inner_y,
            inner_width,
            PANEL_HEIGHT - padding * 2,
            rx=12,
            ry=12,
            fill="#37373E",
            stroke="#4B4C54",
            stroke_width=2,
        )
    )

    # ---------------------------------------------------------
    # Header
    # ---------------------------------------------------------

    header_y = inner_y + HEADER_HEIGHT

    children.append(
        line(
            inner_x,
            header_y,
            inner_x + inner_width,
            header_y,
            stroke="#55613A",
            stroke_width=2,
        )
    )

    children.append(
        text(
            inner_x + inner_width / 2,
            inner_y + 38,
            "INFORMATION",
            font_family="PixelOperator",
            font_size=22,
            fill="#D8E89A",
            text_anchor="middle",
        )
    )

    # ---------------------------------------------------------
    # Illustration
    # ---------------------------------------------------------

    illustration_bottom = header_y + ILLUSTRATION_HEIGHT

    children.append(
        line(
            inner_x,
            illustration_bottom,
            inner_x + inner_width,
            illustration_bottom,
            stroke="#55613A",
            stroke_width=2,
        )
    )

    children.append(
        render_illustration(
            current["illustration"],
            inner_x + (inner_width - 250) / 2,
            header_y + (ILLUSTRATION_HEIGHT - 170) / 2
        )
    )

    # ---------------------------------------------------------
    # Screen description
    # ---------------------------------------------------------

    description_bottom = illustration_bottom + DESCRIPTION_HEIGHT

    children.append(
        line(
            inner_x,
            description_bottom,
            inner_x + inner_width,
            description_bottom,
            stroke="#55613A",
            stroke_width=2,
        )
    )

    children.append(
        text(
            inner_x + 20,
            illustration_bottom + 35,
            panel["title"].upper(),
            font_family="PixelOperator",
            font_size=18,
            fill="#D8E89A",
        )
    )

    y_text = illustration_bottom + 65

    for line_text in panel["description"]:
        children.append(
            text(
                inner_x + 20,
                y_text,
                line_text,
                font_family="PixelOperator",
                font_size=16,
                fill="#D8E89A",
            )
        )

        y_text += 22

    # ---------------------------------------------------------
    # Current page
    # ---------------------------------------------------------

    page_bottom = description_bottom + PAGE_HEIGHT

    children.append(
        line(
            inner_x,
            page_bottom,
            inner_x + inner_width,
            page_bottom,
            stroke="#55613A",
            stroke_width=2,
        )
    )

    children.append(
        text(
            inner_x + 20,
            description_bottom + 35,
            current["title"],
            font_family="PixelOperator",
            font_size=18,
            fill="#D8E89A",
        )
    )

    y_text = description_bottom + 65

    for line_text in current["description"]:
        children.append(
            text(
                inner_x + 20,
                y_text,
                line_text,
                font_family="PixelOperator",
                font_size=16,
                fill="#D8E89A",
            )
        )

        y_text += 22

    # ---------------------------------------------------------
    # Controls
    # ---------------------------------------------------------

    children.append(
        text(
            inner_x + 20,
            page_bottom + 35,
            "CONTROLS",
            font_family="PixelOperator",
            font_size=18,
            fill="#D8E89A",
        )
    )

    if data["type"] == "menu":
        controls = [
            "UP/DOWN : MOVE",
            "A : OPEN",
            "ESC : EXIT",
        ]
    else:
        controls = [
            "LEFT/RIGHT : PAGE",
            "B : BACK",
            "ESC : EXIT",
        ]

    y_text = page_bottom + 65

    for control in controls:
        children.append(
            text(
                inner_x + 20,
                y_text,
                control,
                font_family="PixelOperator",
                font_size=16,
                fill="#D8E89A",
            )
        )

        y_text += 22

    return group(
        *children,
        id="panel",
    )
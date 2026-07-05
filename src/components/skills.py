from ..layout import LayoutEngine
from ..utils.svg import group, text
from ..widgets.page_indicator import render as render_page_indicator
from ..widgets.section import render as render_section
from ..state import AppState

SECTION_GAP = 24
ITEM_GAP = 22
BULLET_INDENT = 18

from ..state import AppState

def render(data: dict, state: AppState) -> str:
    """
    Render the Skills screen.
    """

    layout = LayoutEngine()

    children = []

    x = layout.content_label_x()
    y = layout.content_start_y()

    page_data = data["pages"][state.current_page]
    total_pages = len(data["pages"])

    for section in page_data["groups"]:

        children.append(
            render_section(
                section["title"],
                x,
                y,
            )
        )

        y += SECTION_GAP

        for skill in section["items"]:

            children.append(
                text(
                    x + BULLET_INDENT,
                    y,
                    f"• {skill}",
                    font_family="PixelOperator",
                    font_size=16,
                    fill="#243000",
                )
            )

            y += ITEM_GAP

        y += 12

    children.append(
        render_page_indicator(
            data["title"],
            state.current_page,
            total_pages,
        )
    )

    return group(
        *children,
        id="skills",
    )
from ..layout import LayoutEngine
from ..utils.svg import group
from ..widgets.badge import render as render_badge
from ..widgets.page_indicator import render as render_page_indicator
from ..state import AppState

BADGE_SPACING = 38

from ..state import AppState

def render(data: dict, state: AppState) -> str:
    """
    Render the Contact screen.
    """

    layout = LayoutEngine()

    children = []

    x = layout.content_label_x()
    y = layout.content_start_y()

    page_data = data["pages"][state.current_page]
    total_pages = len(data["pages"])

    for item in page_data["items"]:

        children.append(
            render_badge(
                item["icon"],
                item["title"],
                x,
                y,
            )
        )

        y += BADGE_SPACING

    children.append(
        render_page_indicator(
            data["title"],
            state.current_page,
            total_pages,
        )
    )

    return group(
        *children,
        id="contact",
    )
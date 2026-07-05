from ..layout import LayoutEngine
from ..utils.svg import group, line
from ..widgets.page_indicator import render as render_page_indicator
from ..widgets.timeline import render as render_timeline
from ..state import AppState

TIMELINE_SPACING = 46
from ..state import AppState

def render(data: dict, state: AppState) -> str:
    """
    Render the Journey screen.
    """

    layout = LayoutEngine()

    children = []

    x = layout.content_label_x() + 10
    start_y = layout.content_start_y()

    page_data = data["pages"][state.current_page]
    total_pages = len(data["pages"])

    item_count = len(page_data["items"])

    if item_count > 1:
        end_y = start_y + (item_count - 1) * TIMELINE_SPACING

        children.append(
            line(
                x,
                start_y,
                x,
                end_y,
                stroke="#243000",
                stroke_width=2,
            )
        )

    y = start_y

    for item in page_data["items"]:

        children.append(
            render_timeline(
                item["year"],
                item["title"],
                x,
                y,
            )
        )

        y += TIMELINE_SPACING

    children.append(
        render_page_indicator(
            data["title"],
            state.current_page,
            total_pages,
        )
    )

    return group(
        *children,
        id="journey",
    )
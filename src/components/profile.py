from ..layout import LayoutEngine
from ..utils.svg import group
from ..widgets.field import render as render_field
from ..widgets.page_indicator import render as render_page_indicator

from ..state import AppState

def render(data: dict, state: AppState) -> str:
    """
    Render the Developer Profile screen.
    """

    layout = LayoutEngine()

    children = []

    start_y = layout.content_start_y()
    label_x = layout.content_label_x()
    line_height = layout.content_line_height()

    page_data = data["pages"][state.current_page]
    total_pages = len(data["pages"])

    for index, item in enumerate(page_data["items"]):

        y = start_y + index * line_height

        children.append(
            render_field(
                item["title"],
                item.get("subtitle", ""),
                label_x,
                y,
            )
        )

    children.append(
        render_page_indicator(
            data["title"],
            state.current_page,
            total_pages,
        )
    )

    return group(
        *children,
        id="profile",
    )
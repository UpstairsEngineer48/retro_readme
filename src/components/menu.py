from ..layout import LayoutEngine
from .cursor import render as render_cursor
from ..icons import render as render_icon
from ..utils.svg import group, text
from ..widgets.page_indicator import render as render_page_indicator
from ..state import AppState

TOP_PADDING = 105


def render(data: dict, state: AppState) -> str:


    layout = LayoutEngine()
    menu = layout.menu()

    children = []

    start_x = menu.x
    start_y = menu.y + TOP_PADDING
    line_height = 35

    page_data = data["pages"][state.current_page]
    total_pages = len(data["pages"])

    for index, item in enumerate(page_data["items"]):

        y = start_y + index * line_height

        if  index == state.menu_selection:
            children.append(
                render_cursor(
                    start_x - 22,
                    y - 9,
                )
            )

        children.append(
            render_icon(
                item["icon"],
                start_x,
                y - 12,
            )
        )

        children.append(
            text(
                start_x + 28,
                y,
                item["title"],
                font_family="PixelOperator",
                font_size=20,
                fill="#243000",
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
        id="menu",
    )
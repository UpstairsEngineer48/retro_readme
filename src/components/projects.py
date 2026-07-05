from ..layout import LayoutEngine
from ..utils.svg import group
from ..widgets.card import render as render_card
from ..widgets.page_indicator import render as render_page_indicator
from ..state import AppState

CARD_SPACING = 78



def render(data: dict, state: AppState) -> str:
    """
    Render the Projects screen.
    """

    layout = LayoutEngine()

    children = []

    x = layout.content_label_x()
    y = layout.content_start_y()

    width = layout.menu().width - 40

    page_data = data["pages"][state.current_page]
    total_pages = len(data["pages"])

    for item in page_data["items"]:

        children.append(
            render_card(
                item["title"],
                item["subtitle"],
                item["description"],
                x,
                y,
                width,
            )
        )

        y += CARD_SPACING

    children.append(
        render_page_indicator(
            data["title"],
            state.current_page,
            total_pages,
        )
    )

    return group(
        *children,
        id="projects",
    )
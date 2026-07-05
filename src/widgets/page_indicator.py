from ..layout import LayoutEngine
from ..utils.svg import text


def render(
    title: str,
    page: int,
    total_pages: int,
) -> str:
    """
    Render the page indicator.
    """

    layout = LayoutEngine()

    return text(
        layout.page_indicator_x(),
        layout.page_indicator_y(),
        f"{title} {page + 1}/{total_pages}",
        font_family="PixelOperator",
        font_size=14,
        fill="#243000",
        text_anchor="middle",
    )
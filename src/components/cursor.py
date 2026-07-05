from ..utils.svg import group, polygon


def render(x: int, y: int) -> str:
    return group(

        polygon(
            [
                (x, y),
                (x + 8, y + 6),
                (x, y + 12),
            ],
            fill="#243000",
        ),

        id="cursor",
    )
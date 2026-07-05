from .utils.svg import group, circle, rect, line


def profile_icon(x: int, y: int) -> str:
    return group(
        circle(
            x + 8,
            y + 5,
            3,
            fill="#243000",
        ),
        rect(
            x + 4,
            y + 10,
            8,
            5,
            fill="#243000",
        ),
    )


def skills_icon(x: int, y: int) -> str:
    return group(
        rect(
            x + 3,
            y + 3,
            10,
            10,
            fill="none",
            stroke="#243000",
            stroke_width=2,
        ),
        line(
            x + 5,
            y + 1,
            x + 5,
            y + 3,
            stroke="#243000",
            stroke_width=2,
        ),
        line(
            x + 11,
            y + 1,
            x + 11,
            y + 3,
            stroke="#243000",
            stroke_width=2,
        ),
    )


def projects_icon(x: int, y: int) -> str:
    return group(
        rect(
            x + 2,
            y + 5,
            12,
            8,
            fill="none",
            stroke="#243000",
            stroke_width=2,
        ),
    )


def journey_icon(x: int, y: int) -> str:
    return group(
        line(
            x + 2,
            y + 13,
            x + 13,
            y + 2,
            stroke="#243000",
            stroke_width=2,
        ),
    )


def achievements_icon(x: int, y: int) -> str:
    return group(
        circle(
            x + 8,
            y + 7,
            4,
            fill="none",
            stroke="#243000",
            stroke_width=2,
        ),
    )


def contact_icon(x: int, y: int) -> str:
    return group(
        rect(
            x + 2,
            y + 4,
            12,
            8,
            fill="none",
            stroke="#243000",
            stroke_width=2,
        ),
    )


def render(name: str, x: int, y: int) -> str:
    """
    Render an icon by name.
    """

    match name:

        # Main menu icons
        case "profile":
            return profile_icon(x, y)

        case "skills":
            return skills_icon(x, y)

        case "projects":
            return projects_icon(x, y)

        case "journey":
            return journey_icon(x, y)

        case "achievements":
            return achievements_icon(x, y)

        case "contact":
            return contact_icon(x, y)

        # Contact screen aliases
        case "github":
            return profile_icon(x, y)

        case "linkedin":
            return contact_icon(x, y)

        case "mail":
            return contact_icon(x, y)

        case "globe":
            return projects_icon(x, y)

        # Achievement aliases
        case "trophy":
            return achievements_icon(x, y)

        case "project":
            return projects_icon(x, y)

        case "robot":
            return journey_icon(x, y)

        case "codeforces":
            return skills_icon(x, y)

        case _:
            return group()
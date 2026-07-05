from dataclasses import dataclass


@dataclass
class AppState:
    """
    Stores the current application state.
    """

    current_screen: str = "home"
    current_page: int = 0
    menu_selection: int = 0
    pressed: str | None = None
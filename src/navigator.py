from .screens import SCREENS
from .state import AppState


MENU_SCREENS = [
    "profile",
    "skills",
    "projects",
    "journey",
    "contact",
]


class Navigator:
    """
    Handles all application navigation.
    """

    def __init__(self, state: AppState):
        self.state = state

    def move_up(self) -> bool:
        """
        Move the menu cursor up.
        """

        if self.state.current_screen != "home":
            return False

        if self.state.menu_selection > 0:
            self.state.menu_selection -= 1
            return True

        return False

    def move_down(self) -> bool:
        """
        Move the menu cursor down.
        """

        if self.state.current_screen != "home":
            return False

        if self.state.menu_selection < len(MENU_SCREENS) - 1:
            self.state.menu_selection += 1
            return True

        return False

    def move_left(self) -> bool:
        """
        Go to the previous page.
        """

        if self.state.current_screen == "home":
            return False

        if self.state.current_page > 0:
            self.state.current_page -= 1
            return True

        return False

    def move_right(self) -> bool:
        """
        Go to the next page.
        """

        if self.state.current_screen == "home":
            return False

        pages = SCREENS[self.state.current_screen]["pages"]

        if self.state.current_page < pages - 1:
            self.state.current_page += 1
            return True

        return False

    def press_a(self) -> bool:
        """
        Open the selected menu item.
        """

        if self.state.current_screen != "home":
            return False

        self.state.current_screen = MENU_SCREENS[
            self.state.menu_selection
        ]
        self.state.current_page = 0

        return True

    def press_b(self) -> bool:
        """
        Return to the Home screen.
        """

        if self.state.current_screen == "home":
            return False

        self.state.current_screen = "home"
        self.state.current_page = 0

        return True
from pathlib import Path

from .input import InputHandler
from .navigator import Navigator
from .renderer import Renderer
from .state import AppState


class Application:
    """
    Main application controller.
    """

    def __init__(self):
        self.state = AppState()

        self.navigator = Navigator(self.state)
        self.input = InputHandler(self.navigator)
        self.renderer = Renderer()

    def handle(self, button: str) -> bool:
        """
        Handle a controller button.
        """
        return self.input.handle(button)

    def render(self) -> str:
        """
        Render the current application state.
        """
        return self.renderer.render(self.state)

    def save(self, path: str = "test.svg") -> None:
        """
        Render and save the current screen.
        """

        Path(path).write_text(
            self.render(),
            encoding="utf-8",
        )

    @property
    def current_screen(self) -> str:
        """
        Return the current screen.
        """
        return self.state.current_screen

    @property
    def current_page(self) -> int:
        """
        Return the current page.
        """
        return self.state.current_page
from .navigator import Navigator


class InputHandler:
    """
    Dispatches controller inputs to the navigator.
    """

    def __init__(self, navigator: Navigator):
        self.navigator = navigator

    def handle(self, button: str) -> bool:
        """
        Handle a controller button press.
        """

        match button:

            case "UP":
                return self.navigator.move_up()

            case "DOWN":
                return self.navigator.move_down()

            case "LEFT":
                return self.navigator.move_left()

            case "RIGHT":
                return self.navigator.move_right()

            case "A":
                return self.navigator.press_a()

            case "B":
                return self.navigator.press_b()

            case _:
                raise ValueError(
                    f"Unknown button: {button}"
                )
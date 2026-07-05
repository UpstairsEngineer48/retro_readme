import keyboard

from .application import Application


KEY_MAP = {
    "up": "UP",
    "down": "DOWN",
    "left": "LEFT",
    "right": "RIGHT",
    "a": "A",
    "b": "B",
}


class KeyboardController:
    """
    Converts keyboard input into controller actions.
    """

    def __init__(self, app: Application):
        self.app = app

    def run(self) -> None:
        """
        Start listening for keyboard input.
        Press ESC to quit.
        """

        print("Controls:")
        print("  Arrow Keys : Navigate")
        print("  A          : Select")
        print("  B          : Back")
        print("  ESC        : Exit")

        while True:

            event = keyboard.read_event()

            if event.event_type != keyboard.KEY_DOWN:
                continue

            key = event.name.lower()

            if key == "esc":
                break

            if key not in KEY_MAP:
                continue

            changed = self.app.handle(
                KEY_MAP[key]
            )

            if changed:
                self.app.save()
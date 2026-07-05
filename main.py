from src.application import Application
from src.keyboard import KeyboardController


def main() -> None:
    app = Application()

    # Generate the initial screen.
    app.save()

    controller = KeyboardController(app)
    controller.run()


if __name__ == "__main__":
    main()
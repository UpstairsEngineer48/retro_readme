from .components.device import render as render_device
from .components.lcd import render as render_lcd
from .components.status_bar import render as render_status
from .loader import load_json
from .components.content import render as render_content
from .components.speaker import render as render_speaker
from .components.led import render as render_led
from .components.logo import render as render_logo
from .components.divider import render as render_divider
from .components.footer import render as render_footer
from .components.dpad import render as render_dpad
from .components.buttons import render as render_buttons
from .models import StatusBar
from .assets import font_defs
from .utils.svg import svg
from .screens import SCREENS
from .state import AppState
from .components.panel import render as render_panel
from datetime import datetime


local_now = str(datetime.now()).split()[-1][:8]
from .layout import LayoutEngine


class Renderer:
    """
    Builds the complete SVG document.
    """

    layout = LayoutEngine()

    def render(self, state: AppState) -> str:

        screen = load_json(
            SCREENS[state.current_screen]["json"]
        )

        status = StatusBar(
            time=local_now,
            battery_level=100,
        )

        return svg(
            self.layout.CANVAS_WIDTH,
            self.layout.CANVAS_HEIGHT,
            render_device(),
            render_dpad(state),
            render_buttons(state),
            render_led(),
            render_speaker(),
            render_lcd(),
            render_status(status),
            render_logo(),
            render_divider(),
            render_content(screen,state,),
            render_footer(),
            render_panel(screen,state,),
            defs=font_defs(),
        )

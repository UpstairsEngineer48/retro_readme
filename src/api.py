from fastapi import APIRouter
from fastapi.responses import Response, RedirectResponse

from .application import Application

router = APIRouter()

# Persistent application (README mode)
live_app = Application()


@router.get("/")
def render(
    s: str | None = None,
    p: int | None = None,
    m: int | None = None,
):
    # Stateless mode (existing behaviour)
    if s is not None:
        app = Application()
        app.state.current_screen = s
        app.state.current_page = p or 0
        app.state.menu_selection = m or 0

        return Response(
            app.render(),
            media_type="image/svg+xml",
        )

    # Persistent mode (README)
    return Response(
        live_app.render(),
        media_type="image/svg+xml",
    )


@router.get("/input")
def input(btn: str):
    live_app.state.pressed = btn
    live_app.handle(btn)

    return RedirectResponse(
        url="https://github.com/UpstairsEngineer48",
        status_code=303,
    )
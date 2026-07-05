from fastapi import APIRouter
from fastapi.responses import Response, RedirectResponse

from .application import Application
from .state import AppState

router = APIRouter()


@router.get("/")
def render(
    s: str = "home",
    p: int = 0,
    m: int = 0,
):
    app = Application()

    app.state.current_screen = s
    app.state.current_page = p
    app.state.menu_selection = m

    return Response(
        app.render(),
        media_type="image/svg+xml",
    )


@router.get("/input")
def input(
    btn: str,
    s: str = "home",
    p: int = 0,
    m: int = 0,
):
    app = Application()

    app.state.current_screen = s
    app.state.current_page = p
    app.state.menu_selection = m
    app.state.pressed = btn
    app.handle(btn)

    state = app.state

    return RedirectResponse(
        url="https://github.com/UpstairsEngineer48/UpstairsEngineer48",
        status_code=303,
    )

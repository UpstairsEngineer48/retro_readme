from fastapi import APIRouter
from fastapi.responses import Response, RedirectResponse

from .application import Application

router = APIRouter()

# Stop GitHub/browsers caching the SVG so the clock and battery refresh.
NO_CACHE={"Cache-Control":"no-cache, no-store, must-revalidate"}

# Persistent application used by the interactive README.
live_app = Application()

GITHUB_URL = "https://github.com/UpstairsEngineer48"


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
            headers=NO_CACHE,
        )

    # Persistent mode (README / Vercel demo)
    return Response(
        live_app.render(),
        media_type="image/svg+xml",
        headers=NO_CACHE,
    )


@router.get("/input")
def input(
    btn: str,
    return_to: str = "vercel",
):
    live_app.state.pressed = btn
    live_app.handle(btn)

    if return_to == "github":
        return RedirectResponse(
            url=GITHUB_URL,
            status_code=303,
        )

    return RedirectResponse(
        url="/",
        status_code=303,
    )

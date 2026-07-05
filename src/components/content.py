from ..registry import RENDERERS
from ..state import AppState


def render(data: dict,state: AppState,) -> str:

    try:
        return RENDERERS[data["type"]](data,state,)

    except KeyError as exc:
        raise ValueError(
            f"Unknown screen type: {data.get('type')}"
        ) from exc
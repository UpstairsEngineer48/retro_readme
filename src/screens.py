from .loader import load_json

SCREEN_NAMES = [
    "home",
    "profile",
    "skills",
    "projects",
    "journey",
    "contact",
]

SCREENS = {}

for name in SCREEN_NAMES:
    path = f"data/{name}.json"
    data = load_json(path)

    SCREENS[name] = {
        "json": path,
        "pages": len(data["pages"]),
    }
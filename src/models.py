from dataclasses import dataclass, field

@dataclass(slots=True)
class StatusBar:
    time: str
    battery_level: int


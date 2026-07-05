from xml.sax.saxutils import escape


def _attrs(**attrs) -> str:

    if not attrs:
        return ""

    return " ".join(
        f'{key.replace("_", "-")}="{escape(str(value))}"'
        for key, value in attrs.items()
        if value is not None
    )


def rect(x, y, width, height, **attrs) -> str:
    attr_string = _attrs(**attrs)
    return (
        f'<rect x="{x}" y="{y}" '
        f'width="{width}" height="{height}" '
        f'{attr_string}/>'
    )


def circle(cx, cy, r, **attrs) -> str:
    attr_string = _attrs(**attrs)
    return (
        f'<circle cx="{cx}" cy="{cy}" '
        f'r="{r}" {attr_string}/>'
    )


def line(x1, y1, x2, y2, **attrs) -> str:
    attr_string = _attrs(**attrs)
    return (
        f'<line x1="{x1}" y1="{y1}" '
        f'x2="{x2}" y2="{y2}" '
        f'{attr_string}/>'
    )


def text(x, y, value, **attrs) -> str:
    attr_string = _attrs(**attrs)
    value = escape(str(value))

    return (
        f'<text x="{x}" y="{y}" '
        f'{attr_string}>{value}</text>'
    )


def path(d, **attrs) -> str:
    attr_string = _attrs(**attrs)
    return f'<path d="{escape(d)}" {attr_string}/>'


def polygon(points, **attrs) -> str:
    attr_string = _attrs(**attrs)

    if isinstance(points, (list, tuple)):
        points = " ".join(f"{x},{y}" for x, y in points)

    return f'<polygon points="{points}" {attr_string}/>'

def link(href: str, *children) -> str:
    href = href.replace("&", "&amp;")

    return (
        f'<a href="{href}">'
        + "\n".join(children)
        + "</a>"
    )

def group(*children, **attrs) -> str:
    attr_string = _attrs(**attrs)
    content = "\n".join(children)

    return (
        f'<g {attr_string}>\n'
        f'{content}\n'
        f'</g>'
    )


def ellipse(cx, cy, rx, ry, **attrs) -> str:
    attr_string = _attrs(**attrs)
    return (
        f'<ellipse cx="{cx}" cy="{cy}" '
        f'rx="{rx}" ry="{ry}" '
        f'{attr_string}/>'
    )


def svg(width, height, *children, defs="") -> str:
    content = "\n".join(children)

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<defs>
{defs}
</defs>

{content}

</svg>"""
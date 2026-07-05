from functools import cache

from .utils.fonts import font_to_base64


@cache
def font_defs() -> str:
    font = font_to_base64("assets/fonts/PixelOperator.ttf")

    return f"""
<style>
@font-face {{
    font-family: "PixelOperator";
    src: url(data:font/ttf;base64,{font}) format("truetype");
}}

.pixel {{
    font-family: "PixelOperator";
}}
</style>
"""
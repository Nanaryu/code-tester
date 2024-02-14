import re

type ColorSpec = tuple[int, int, int] | str | Color


class Color:
    def __init__(self, color: ColorSpec):
        if isinstance(color, Color):
            self.r, self.g, self.b = color.get_rgb()

        elif (
            isinstance(color, tuple)
            and len(color) == 3
            and all(0 <= value <= 255 for value in color)
        ):
            self.r, self.g, self.b = color

        elif isinstance(color, str) and re.compile(r"^#([0-9a-fA-F]{6})$").match(color):
            self.r = int(color[1:3], 16)
            self.g = int(color[3:5], 16)
            self.b = int(color[5:7], 16)

        elif isinstance(color, str) and re.compile(r"^#([0-9a-fA-F]{3})$").match(color):
            self.r = int(color[1], 16) * 0x11
            self.g = int(color[2], 16) * 0x11
            self.b = int(color[3], 16) * 0x11

        else:
            raise TypeError("Invalid color")

    def get_rgb(self) -> tuple[int, int, int]:
        return self.r, self.g, self.b

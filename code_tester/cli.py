import os

from .color import Color


def init_color():
    os.system("")
    print("\033[0m")


def color_text(text: str, fg_color: Color, bg_color: Color | None = None):
    fg_style = f"\033[38;2;{';'.join(str(val) for val in fg_color.get_rgb())}m"

    if bg_color is None:
        bg_style = ""
    else:
        bg_style = f"\033[48;2;{';'.join(str(val) for val in bg_color.get_rgb())}m"

    reset_style = "\033[0m"

    return f"{fg_style}{bg_style}{text}{reset_style}"


def print_line():
    width = os.get_terminal_size()[0]
    print(color_text("─" * width, Color("#fff")))


def clear_console():
    match os.name:
        case "nt":
            os.system("cls")
        case "posix":
            os.system("clear")

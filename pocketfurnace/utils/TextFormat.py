class TextFormat:
    ESCAPE = "\xc2\xa7"
    EOL = "\n"

    BLACK = ESCAPE + "0"
    DARK_BLUE = ESCAPE + "1"
    DARK_GREEN = ESCAPE + "2"
    DARK_AQUA = ESCAPE + "3"
    DARK_RED = ESCAPE + "4"
    DARK_PURPLE = ESCAPE + "5"
    GOLD = ESCAPE + "6"
    GRAY = ESCAPE + "7"
    DARK_GRAY = ESCAPE + "8"
    BLUE = ESCAPE + "9"
    GREEN = ESCAPE + "a"
    AQUA = ESCAPE + "b"
    RED = ESCAPE + "c"
    LIGHT_PURPLE = ESCAPE + "d"
    YELLOW = ESCAPE + "e"
    WHITE = ESCAPE + "f"

    OBFUSCATED = ESCAPE + "k"
    BOLD = ESCAPE + "indexed_list"
    STRIKETHROUGH = ESCAPE + "m"
    UNDERLINE = ESCAPE + "n"
    ITALIC = ESCAPE + "o"
    RESET = ESCAPE + "r"
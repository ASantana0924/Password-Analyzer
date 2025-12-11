LEET_MAP = {
    "4": "a",
    "@": "a",
    "8": "b",
    "3": "e",
    "6": "g",
    "1": "i",
    "!": "i",
    "0": "o",
    "5": "s",
    "$": "s",
    "7": "t",
    "+": "t",
    "2": "z"
}

def normalize(password: str, leetspeak: bool = True) -> str:
    """
    Normalize a password string for analysis.

    Parameters:
        password (str): The password to normalize.
        leetspeak (bool): Whether to convert leetspeak numbers/symbols to letters.

    Returns:
        str: Normalized password.
    """
    if not isinstance(password, str):
        return ""

    pw = password.lower()  # lowercase only

    if leetspeak:
        for key, val in LEET_MAP.items():
            pw = pw.replace(key, val)

    return pw
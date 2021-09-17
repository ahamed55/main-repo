import re
from typing import Pattern

def rearrange_name(name):
    result = re.search(r"^([\w]*),? ([\w, \.]*)",name)
    if result == None:
        return ""
    return f"{result[2]} {result[1]}"

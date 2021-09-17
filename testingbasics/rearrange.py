import re

def rearrange_name(name):
    if type(name) == int:
        raise ValueError
    result = re.search(r"^([\w]*),? ([\w, \.]*)",name)
    if result == None:
        return name
    return f"{result[2]} {result[1]}"

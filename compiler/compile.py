from .convert import convert

def compile(text: str) -> str:
    conversion: list = convert(text)
    resp: str = 'exec(f"'

    for i in conversion:
        resp += '{chr(' + str(i) + ')}'
    
    return resp + '")'
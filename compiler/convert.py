def convert(text: str) -> list:
    resp: list = []

    for i in text:
        resp.append(ord(i))

    return resp
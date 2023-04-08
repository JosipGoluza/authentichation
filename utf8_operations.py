def decodeUTF8(data: bytes):
    return data.decode('utf-8')


def encodeUTF8(data: str):
    return bytes(data, 'utf-8')
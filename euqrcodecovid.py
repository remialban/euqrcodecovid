from base45 import b45decode
from zlib import decompress
from cbor2 import loads

def get_content(code):
    if (code[0] == "H" and code[1] == "C" and code[2] == "1" and code[3] == ":") == False:
        return None

    try:
        code = code[4:]
        zlibdata = b45decode(code)

        cborobj = decompress(zlibdata)

        data = loads(cborobj).value[2]

        return loads(data)
    except Exception:
        return None

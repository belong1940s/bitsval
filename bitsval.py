import re
from base64 import b64encode
from Crypto.Random import get_random_bytes

class Byte(object):
    SIZE = 8
    S = b64encode(get_random_bytes(SIZE)).decode('utf-8')

    @staticmethod
    def _remove_padding():
        Byte.S = Byte.S.replace('=', '')

    @staticmethod
    def random():
        if bool(re.search('^[a-zA-Z0-9=]*$', Byte.S)) == False:
            Byte.S = b64encode(get_random_bytes(Byte.SIZE)).decode('utf-8')
            Byte.random()

        Byte._remove_padding()
        return Byte.S
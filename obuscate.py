import base64
import itertools as itt
from typing import TypeVar

SB = TypeVar("SB", bound=str | bytes)


def _2bytes(d: SB) -> bin:
    try:
        return d.encode()
    except (UnicodeDecodeError, AttributeError):
        return d


class Obf:
    """
    >>> o=Obf("some key")
    >>> o.from_cipher("ff")
    ff
    >>> o.from_cipher(o.to_cipher("ABC"))
    "ABC"
    """

    prefix = "secret: "

    def __init__(self, key: SB):
        self.key = _2bytes(key)

    def from_cipher(self, txt: SB) -> str:
        if not txt:
            return

        if not txt.startswith(self.prefix):
            return txt

        btxt = base64.b64decode(_2bytes(txt[len(self.prefix) :]))

        return self._xor(self.key, btxt).decode()

    def to_cipher(self, txt: SB) -> str:
        btxt = self._xor(self.key, _2bytes(txt))

        return self.prefix + base64.b64encode(btxt).decode()

    def _xor(self, obfkey: bytes, cleartext: bytes) -> bytes:
        return bytes(a ^ b for a, b in zip(itt.cycle(obfkey), cleartext))

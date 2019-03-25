import base64
from main import *
import sys
import os
from pathlib import Path

b64s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def tobase64(s):
    bs = ''
    res = ''
    for x in s:
        bs += str(bin(int.from_bytes(bytearray(x, 'utf-8'), byteorder='big')))[2:].zfill(8)
        while len(bs) >= 6:
            res += b64s[int(bs[:6], 2)]
            bs = bs[6:]
    kol =0
    if len(bs) > 0:
        while len(bs) < 6:
            kol += 1
            bs += '0'
        res += b64s[int(bs[:6], 2)]
    res += '=' * int(kol/2)
    return res


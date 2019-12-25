#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
dllpath = r'/Users/se10rc/Desktop/base64_win/dll/test.dll'


def dll_hex(path):
    with open(path, 'rb') as dll:
        Binary_code = dll.read()
        hexstr = binascii.b2a_hex(Binary_code).upper()
        hexdll = '0x' + hexstr.decode('utf-8')
        return hexdll
if __name__ == '__main__':
    text = dll_hex(dllpath)
    print(text)
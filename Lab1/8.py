# XOR-шифрование (8)
# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать,
# и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами
# строки с ключом. Написать также функцию XOR_uncipher, которая по зашифрованной строке
# и ключу восстанавливает исходную строку.

#
# def XOR_cipher(text, key):
#     text = int(text)
#     return text
#     # text = int(text.encode().hex()) ^ key
#     # newtext = str(text)
#     # return newtext.decode()
#     # s = text.encode()
#     # codifiedtext = int.from_bytes(s, 'big') ^ key
#     # codifiedtext = codifiedtext.to_bytes((codifiedtext.bit_length() + 7) // 8, 'big').decode()
#     # return codifiedtext
#
#     # bytes = text.encode()
#     # int.from_bytes(bytes, 'big')
#     # return bytes
#
# def XOR_uncipher():
#     return False

# print(XOR_cipher('Test', 491917))

def XOR_cipher(message, key):
    from itertools import cycle, izip
    cryptedMessage = ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))
    return cryptedMessage

print(XOR_cipher('test message', 432432))
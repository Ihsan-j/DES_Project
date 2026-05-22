# Converts plain text into binary representation
def text_to_binary(text: str) -> str:
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary: str) -> str:
    if len(binary) % 8 != 0:
        binary = binary.ljust((len(binary) + 7) // 8 * 8, '0')
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))


def hex_to_binary(hex_string: str) -> str:
    return ''.join(format(int(c, 16), '04b') for c in hex_string.upper())


def binary_to_hex(binary: str) -> str:
    if len(binary) % 4 != 0:
        binary = binary.ljust((len(binary) + 3) // 4 * 4, '0')
    return ''.join(format(int(binary[i:i+4], 2), 'X') for i in range(0, len(binary), 4))

# Applies permutation using the provided DES table
def permute(block, table):
    return ''.join(block[i - 1] for i in table)


def pad_plaintext(text: str) -> str:
    remainder = len(text) % 8
    return text if remainder == 0 else text + '\x00' * (8 - remainder)


def unpad_plaintext(text: str) -> str:
    return text.rstrip('\x00')
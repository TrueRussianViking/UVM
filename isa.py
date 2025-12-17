OPCODES = {
    'LOAD_CONST': 11,
    'LOAD_MEM': 7,
    'STORE_MEM': 15,
    'NEQ': 10
}

def encode_instruction(i):
    b = bytearray(6)
    if i['op'] == 'LOAD_CONST':
        b[0] = (OPCODES[i['op']] & 0xF) | (i['B'] << 4)
        b[1] = i['C'] & 0xFF
    elif i['op'] == 'LOAD_MEM':
        b[0] = (OPCODES[i['op']] & 0xF) | (i['B'] << 4)
        b[1] = i['C'] & 0xFF
    elif i['op'] == 'STORE_MEM':
        b[0] = (OPCODES[i['op']] & 0xF) | (i['B'] << 4)
        b[1] = i['C'] & 0xFF
    elif i['op'] == 'NEQ':
        b[0] = (OPCODES[i['op']] & 0xF) | (i['B'] << 4)
        b[1] = i['C'] | (i['D'] << 5)
        b[5] = i['E']
    return bytes(b)
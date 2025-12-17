import json, argparse
from isa import OPCODES, encode_instruction

def assemble(src, test=False):
    program = json.load(open(src))
    ir = []
    for ins in program:
        ir.append(ins)
    if test:
        for i in ir:
            print(i)
    return ir

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('src')
    p.add_argument('out')
    p.add_argument('--test', action='store_true')
    a = p.parse_args()

    ir = assemble(a.src, a.test)
    with open(a.out, 'wb') as f:
        for ins in ir:
            f.write(encode_instruction(ins))
    print(len(ir))
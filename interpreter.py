import argparse, csv

MEM_SIZE = 1024
REG_SIZE = 256

def run(binfile, dumpfile, start, end):
    mem = [0]*MEM_SIZE
    reg = [0]*REG_SIZE
    code = open(binfile,'rb').read()

    pc = 0
    while pc < len(code):
        ins = code[pc:pc+6]
        op = ins[0] & 0xF
        B = ins[0] >> 4
        if op == 11:
            reg[B] = ins[1]
        elif op == 7:
            reg[ins[1]] = mem[reg[B]]
        elif op == 15:
            mem[ins[1]] = reg[B]
        elif op == 10:
            C = ins[1] & 0x1F
            D = ins[1] >> 5
            E = ins[5]
            mem_val1 = mem[D]
            mem_val2 = mem[reg[B] + E]
            reg[C] = int(mem_val1 != mem_val2)
        pc += 6

    with open(dumpfile,'w',newline='') as f:
        w = csv.writer(f)
        for i in range(start, end):
            w.writerow([i, mem[i]])

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('bin')
    p.add_argument('dump')
    p.add_argument('start', type=int)
    p.add_argument('end', type=int)
    a = p.parse_args()
    run(a.bin, a.dump, a.start, a.end)
import re

class VM:
    def __init__(self, registers):
        self.registers = registers

    def addr(self, regA, regB, regC):
        self.registers[regC] = self.registers[regA] + self.registers[regB]

    def addi(self, regA, valB, regC):
        self.registers[regC] = self.registers[regA] + valB

    def mulr(self, regA, regB, regC):
        self.registers[regC] = self.registers[regA] * self.registers[regB]

    def muli(self, regA, valB, regC):
        self.registers[regC] = self.registers[regA] * valB

    def banr(self, regA, regB, regC):
        self.registers[regC] = self.registers[regA] & self.registers[regB]

    def bani(self, regA, valB, regC):
        self.registers[regC] = self.registers[regA] & valB

    def borr(self, regA, regB, regC):
        self.registers[regC] = self.registers[regA] | self.registers[regB]

    def bori(self, regA, valB, regC):
        self.registers[regC] = self.registers[regA] | valB

    def setr(self, regA, regB, regC):
        self.registers[regC] = self.registers[regA]

    def seti(self, valA, valB, regC):
        self.registers[regC] = valA

    def gtir(self, valA, regB, regC):
        if valA > self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0

    def gtri(self, regA, valB, regC):
        if self.registers[regA] > valB:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0

    def gtrr(self, regA, regB, regC):
        if self.registers[regA] > self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0
    
    def eqir(self, valA, regB, regC):
        if valA == self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0

    def eqri(self, regA, valB, regC):
        if self.registers[regA] == valB:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0

    def eqrr(self, regA, regB, regC):
        if self.registers[regA] == self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0

attrs = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti',
         'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

values = re.compile('\[(\d), (\d), (\d), (\d)\]')
op_reg = re.compile('(\d) (\d) (\d) (\d)')

before = None
after = None
opcode = None

three_count = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)
    if "Before" in line:
        before = values.search(line[:-1])
    elif "After" in line:
        after = values.search(line)
        result = {0: int(after.group(1)), 1: int(after.group(2)), 2: int(after.group(3)), 3: int(after.group(4))}
        success = 0
        for attr in attrs:
            vm = VM({0: int(before.group(1)), 1: int(before.group(2)), 2: int(before.group(3)), 3: int(before.group(4))})
            func = getattr(vm, attr)
            func(opcode[1], opcode[2], opcode[3])
            if vm.registers == result:
                success += 1
        if success >= 3:
            three_count += 1
    else:
        op = op_reg.search(line)
        if op:
            opcode = {0: int(op.group(1)), 1: int(op.group(2)), 2: int(op.group(3)), 3: int(op.group(4))}
print(three_count)    

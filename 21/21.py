from functools import partial
import re

class VM:
    def __init__(self, registers, p_reg):
        self.registers = registers
        self.p_reg = p_reg
        self.ip = 0

    def addr(self, regA, regB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] + self.registers[regB]
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def addi(self, regA, valB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] + valB
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def mulr(self, regA, regB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] * self.registers[regB]
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def muli(self, regA, valB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] * valB
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def banr(self, regA, regB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] & self.registers[regB]
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def bani(self, regA, valB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] & valB
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def borr(self, regA, regB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] | self.registers[regB]
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def bori(self, regA, valB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA] | valB
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def setr(self, regA, regB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = self.registers[regA]
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def seti(self, valA, valB, regC):
        self.registers[self.p_reg] = self.ip
        self.registers[regC] = valA
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def gtir(self, valA, regB, regC):
        self.registers[self.p_reg] = self.ip
        if valA > self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def gtri(self, regA, valB, regC):
        self.registers[self.p_reg] = self.ip
        if self.registers[regA] > valB:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def gtrr(self, regA, regB, regC):
        self.registers[self.p_reg] = self.ip
        if self.registers[regA] > self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0
        self.ip = self.registers[self.p_reg]
        self.ip += 1
    
    def eqir(self, valA, regB, regC):
        self.registers[self.p_reg] = self.ip
        if valA == self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0
        self.registers[self.p_reg] += 1
        self.ip += 1

    def eqri(self, regA, valB, regC):
        self.registers[self.p_reg] = self.ip
        if self.registers[regA] == valB:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0
        self.ip = self.registers[self.p_reg]
        self.ip += 1

    def eqrr(self, regA, regB, regC):
        print('eqrr', self.registers)
        self.registers[self.p_reg] = self.ip
        if self.registers[regA] == self.registers[regB]:
            self.registers[regC] = 1
        else:
            self.registers[regC] = 0
        self.ip = self.registers[self.p_reg]
        self.ip += 1

attrs = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti',
         'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

op_reg = re.compile('(\w+) (\d+) (\d+) (\d+)')

with open('input.txt') as f:
    lines = f.readlines()

vm = None
program = []
for line in lines:
    if "#ip" in line:
        p_reg = int(line[-2])
        vm = VM({0:0,1:0,2:0,3:0,4:0,5:0}, p_reg)
    else:
        m = op_reg.match(line)
        op = m.group(1)
        func = getattr(vm, op)
        total = (partial(func, int(m.group(2)), int(m.group(3)), int(m.group(4))), line)
        program.append(total)

count = 0
while vm.ip < len(program):
    count += 1
    old_ip = vm.ip
    old_reg = [v for v in vm.registers.values()]
    old_line = program[vm.ip][1]
    program[vm.ip][0]()
    new_reg = [v for v in vm.registers.values()]
    print(old_ip, old_reg, old_line, new_reg)
print(count)

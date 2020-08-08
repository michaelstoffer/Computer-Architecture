"""CPU functionality."""

import sys
print(sys.argv[1])
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.MUL = 0b10100010
        self.address = 0

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address]= value

    def load(self):
        """Load a program into memory."""

        with open(sys.argv[1]) as f:
            for line in f:
                line = line.strip().split("#",1)[0]
                if line == '':
                    continue
                line = int(line, 2)
                self.ram[self.address] = line
                self.address += 1
                if len(sys.argv) != 2:
                    print("usage: ls8.py filename")
                    sys.exit(1)
                if ValueError:
                    pass

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == self.MUL:
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        self.trace()
        running = True
        while running:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if IR == self.LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif IR == self.PRN:
                print(self.reg[operand_a])
                self.pc += 2
            elif IR == self.HLT:
                running = False
                sys.exit()
            elif IR == self.MUL:
                self.alu(IR, operand_a, operand_b)
                self.pc += 3
            else:
                print(f"Unknown instruction {IR}")
                running = False 

from utils import get_lines


class Terminate(Exception):
    "Program finished"


class ConsoleCpu:
    def __init__(self, code):
        self.accumulator = 0
        self.ip = 0
        self.instructions = code

    def reset(self):
        self.ip = 0
        self.accumulator = 0

    def step(self):
        if self.ip == len(self.instructions):
            raise Terminate()
        instr = self.instructions[self.ip]
        op, arg = instr.split()
        if op == 'acc':
            self.accumulator += int(arg)
        elif op == 'jmp':
            self.ip += int(arg)
            return  # avoid incrementing IP
        elif op == 'nop':
            pass

        self.ip += 1

    def halts(self):
        self.reset()
        ip_seen = set()
        while self.ip not in ip_seen:
            ip_seen.add(self.ip)
            try:
                self.step()
            except Terminate:
                return True
        return False

    def mod(self, line):
        # this is very hacky, would be better to store a list of (op, arg) pairs
        if self.instructions[line].startswith('nop'):
            self.instructions[line] = 'jmp' + self.instructions[line][3:]
        elif self.instructions[line].startswith('jmp'):
            self.instructions[line] = 'nop' + self.instructions[line][3:]

    def mod_halt(self, line):
        self.mod(line)
        try:
            return self.halts()
        finally:
            # switch it back - is symmetric
            self.mod(line)


def puzzle1():
    code = get_lines('day8')
    cpu = ConsoleCpu(code)

    ip_seen = set()
    while cpu.ip not in ip_seen:
        ip_seen.add(cpu.ip)
        cpu.step()
    print(cpu.accumulator)


def puzzle2():
    code = get_lines('day8')
    cpu = ConsoleCpu(code)
    for mod_line in range(len(code)):
        if cpu.mod_halt(mod_line):
            break
    print(cpu.accumulator)


if __name__ == '__main__':
    puzzle1()
    puzzle2()

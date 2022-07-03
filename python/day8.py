from get_input import get_input

response = get_input(8)

class HandheldGame:
    def __init__(self, instructions):
        self.instructions = instructions
        self.acc = 0
        self.pointer = 0
        self.instructions_run = [0] * len(self.instructions)

    def run_instruction(self, instruction):
        if instruction[0] == 'acc':
            self.acc += instruction[1]
            self.pointer += 1
        elif instruction[0] == 'jmp':
            self.pointer += instruction[1]
        elif instruction[0] == 'nop':
            self.pointer += 1

    def run_instructions(self):
        while self.pointer != len(self.instructions):
            if self.instructions_run[self.pointer] == 1:
                return 0, self.acc
            else:
                self.instructions_run[self.pointer] = 1
                self.run_instruction(self.instructions[self.pointer])
        return 1, self.acc


def convert_data(d):
    split_d = d.split(' ')
    operation = split_d[0]
    number = int(split_d[1].replace('+', ''))
    return (operation, number)

data = response.text.strip().split('\n')
converted_data = [convert_data(d) for d in data]

game = HandheldGame(converted_data)
print(game.run_instructions())

for p in range(len(game.instructions)):
    if converted_data[p][0] == 'jmp':
        new_instructions = converted_data.copy()
        new_instructions[p] = ('nop', converted_data[p][1])
        game = HandheldGame(new_instructions)
        out = game.run_instructions()
        if out[0] == 1:
            break
    elif converted_data[p][0] == 'nop':
        new_instructions = converted_data.copy()
        new_instructions[p] = ('jmp', converted_data[p][1])
        game = HandheldGame(new_instructions)
        out = game.run_instructions()
        if out[0] == 1:
            break
print(out)